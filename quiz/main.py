from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # list object
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")