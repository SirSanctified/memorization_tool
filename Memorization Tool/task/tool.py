from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy import Column, String, Integer, create_engine

engine = create_engine("sqlite:///flashcard.db?check_same_thread=False")
Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box_num = Column(Integer)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_flashcard():
    while True:
        q = input('Question: ')
        if q.strip() != "":
            break
    while True:
        a = input('Answer: ')
        if a.strip() != "":
            break
    flashcard = Flashcard(question=q, answer=a, box_num=0)
    session.add(flashcard)
    session.commit()


def practice_flashcards(session_number):
    results = session.query(Flashcard).filter(Flashcard.box_num <= session_number).all()
    if not results:
        print('There is no flashcard to practice!')
        print()
    else:
        for result in results:
            print('Question:', result.question)
            print('press "y" to see the answer:')
            print('press "n" to skip:')
            print('press "u" to update:')
            option = input()
            if option == 'y' or option == 'Y':
                print('Answer:', result.answer)
                print('press "y" if your answer is correct:')
                print('press "n" if your answer is wrong:')
                res = input()
                if res == 'y' or res == 'Y':
                    card_to_move = session.query(Flashcard).filter(Flashcard.question == result.question)
                    if card_to_move[0].box_num < 2:
                        card_to_move.update({'box_num': card_to_move[0].box_num + 1})
                        session.commit()
                    elif card_to_move[0].box_num == 2:
                        card_to_move.delete()
                        session.commit()
                elif res == 'n' or res == 'N':
                    card_to_move = Query(Flashcard, session).filter(Flashcard.question == result.question)
                    if card_to_move[0].box_num > 0:
                        card_to_move.update({'box_num': card_to_move[0].box_num - 1})
                        session.commit()
                else:
                    print(f'{res} is not an option')

                print()
            elif option == 'n' or option == 'N':
                print()
            elif option == 'u' or option == 'U':
                print('press "d" to delete the flashcard:')
                print('press "e" to edit the flashcard:')
                inp = input()
                query = session.query(Flashcard).filter(Flashcard.question == result.question)
                if inp == 'd' or inp == "D":
                    query.delete()
                    session.commit()
                    print()
                elif inp == 'e' or inp == 'E':
                    print('current question:', result.question)
                    new_question = input("please write a new question:")
                    if new_question.strip():
                        query.update({"question": new_question})
                        session.commit()
                    print('current answer:', result.answer)
                    new_answer = input('please write a new answer:')
                    if new_answer.strip():
                        query = session.query(Flashcard).filter(Flashcard.answer == result.answer)
                        query.update({"answer": new_answer})
                        session.commit()
                else:
                    print(f"{inp} is not an option")


while True:
    session_num = 0
    print('1. Add flashcards\n2. Practice flashcards\n3. Exit')
    choice = input()
    if choice == '1':
        while True:
            print('1. Add a new flashcard\n2. Exit')
            opt = input()
            if opt == '1':
                add_flashcard()
            elif opt == '2':
                break
            else:
                print(opt, 'is not an option')
    elif choice == '2':
        practice_flashcards(session_num)
        session_num += 1
    elif choice == '3':
        print('Bye!')
        break
    else:
        print(choice, 'is not an option')
