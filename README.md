# memorization_tool

A good memorizing tool can boost your short and long-term memory. If you tried to learn a foreign language, you probably know what a flashcard is. It is an excellent device to remember facts. Flashcards alone are not enough, we need a special technique.
A flashcard is a piece of paper with a question on one side and the answer on the other. Let's assume we need to memorize the capital cities of various countries. Write the country name on one side and the capital on the other.

When the program starts, it should print the menu below. It is our main menu (1):

1. Add flashcards
2. Practice flashcards
3. Exit

If 1 is entered, the program should print the following sub-menu (2):

1. Add a new flashcard
2. Exit

By choosing the Add a new flashcard option, a user is prompted to enter a Question and an Answer. Once they are entered, the program automatically returns to the sub-menu (2). Iterate this process every time a user wants to add a new flashcard.
The Practice flashcards option in the main menu (1) should print all the questions and answers that have been added previously. If there are no flashcards, print There is no flashcard to practice! and return to the main menu (1).

Your flashcard should appear on the screen in the following way:

press "y" to see the answer:
press "n" to skip:
press "u" to update:

If y is entered, the program should output Answer: {your answer} and go to the next flashcard. If there are no flashcards to show, return to the main menu (1).

If n is entered, skip to the next flashcard. If there are no flashcards to show, return to the main menu (1).

After displaying each question, the program  asks users whether their answers are correct or not. To do this we need to create another menu, let's call it the learning menu (5):

press "y" if your answer is correct:
press "n" if your answer is wrong:

This will correspond to Session 1 for these cards. New flashcards and cards with wrong answers should go to the first box. Once you reach Session 3 for them, you can remove them from the database.

The skipped questions remain in the same boxes. Do not display a learning menu (5) for them.

A user advances to another menu by entering u. Let's call it the update menu (4).

press "d" to delete the flashcard:
press "e" to edit the flashcard:

d deletes a flashcard, the e option offers a way to edit the current flashcard. First, we need to edit the question:

current question: 
please write a new question: 

Once the question has been edited, proceed to the answer:

current answer: 
please write a new answer:

If the user leaves the question or the answer field empty, keep the original question or answer value unchanged. 

Once the program has reached the end of a flashcard list, return to the main menu (1).

We are going to implement the Leitner system in our program. In short, it introduces the concept of spaced repetition proposed by Sebastian Leitner, a German scientist. Leitner's system suggests reviewing cards at increased intervals.

We can divide the memorization process into several parts. First, you create several boxes (usually from 3 to 5) that will store your flashcards. You mark each box with time periods that show how frequently the cards should be reviewed. For example, Box 1 will contain the most difficult cards, so they should be reviewed every day; Box 2 will have easier cards that you will check more rarely, every two days, and so on.

Next, you start learning and arranging the flashcards. You go through multiple Sessions. During Session 1, all your cards are in Box 1. You answer questions on these cards. If you are right, the card moves to Box 2 — that means that you don't need to repeat the information on the card so often. If your answer is wrong, your card stays in Box 1 — that means that you will see this card more frequently. When you reach Session 2, you answer questions on the cards both in Box 1 and Box 2. During Session 3, you study the cards in all three boxes. Again, every time you get a card wrong, you move it to Box 1. If you get the card right, you move it to the next box.

[image](https://user-images.githubusercontent.com/63302923/186325069-90e4c9ec-41f6-4277-aeec-482a2cc81dcc.png)

In this stage, there are three boxes, and if you give the correct answers to the cards in the third box, it means you've learned them, and you don't need those cards anymore, so you can remove them from the database.

Example 1:


1. Add flashcards
2. Practice flashcards
3. Exit
> 2
There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 1
1. Add a new flashcard
2. Exit
> 1

Question:
> What is the Capital of Turkey?
Answer:
> Ankara

1. Add a new flashcard
2. Exit
> 1

Question:
> What is the capital of Croatia?
Answer:
> Zagreb

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> n

1. Add flashcards
2. Practice flashcards
3. Exit
>> 2

Question: What is the Capital of Turkey?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Ankara
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y


Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: What is the capital of Croatia?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Zagreb
press "y" if your answer is correct:
press "n" if your answer is wrong:
> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 2
There is no flashcard to practice!

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!



Example 2:



1. Add flashcards
2. Practice flashcards
3. Exit
> 6
6 is not an option

1. Add flashcards
2. Practice flashcards
3. Exit
> 1
1. Add a new flashcard
2. Exit
> 3
3 is not  an option

1. Add a new flashcard
2. Exit
> 1

Question:
>
Question:
> what is the capital of Iran?
Answer:
> Tehran

1. Add a new flashcard
2. Exit
> 2

1. Add flashcards
2. Practice flashcards
3. Exit
> 2

Question: what is the capital of Iran?
press "y" to see the answer:
press "n" to skip:
press "u" to update:
> 6
6 is not an option

press "y" to see the answer:
press "n" to skip:
press "u" to update:
> y

Answer: Tehran
press "y" if your answer is correct:
press "n" if your answer is wrong:
>>
 is not an option

press "y" if your answer is correct:
press "n" if your answer is wrong:
>> b
b is not an option

press "y" if your answer is correct:
press "n" if your answer is wrong:
>> y

1. Add flashcards
2. Practice flashcards
3. Exit
> 3

Bye!
