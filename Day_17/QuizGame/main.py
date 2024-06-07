from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []



for question in question_data:
    question_question = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_question, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

i = 0

while quiz.still_has_questions():
    i += 1
    quiz.next_question()
    if i == 12:
        print("You've completed the quiz")
        print(f"Your final score was: {quiz.score}")

