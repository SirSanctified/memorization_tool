from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer, create_engine

engine = create_engine("sqlite:///flashcard.db?check_same_thread=False")
Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column('id', Integer, primary_key=True)
    question = Column('question', String)
    answer = Column('answer', String)


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
    flashcard = Flashcard(question=q, answer=a)
    session.add(flashcard)
    session.commit()


def practice_flashcards():
    results = session.query(Flashcard).all()
    if results:
        for result in results:
            print('Question:', result.question)
            print('press "y" to see the answer:')
            print('press "n" to skip:')
            print('press "u" to update:')
            option = input()
            if option == 'y' or option == 'Y':
                print('Answer:', result.answer)
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

    else:
        print('There is no flashcard to practice')


while True:
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
        practice_flashcards()
    elif choice == '3':
        print('Bye!')
        break
    else:
        print(choice, 'is not an option')
