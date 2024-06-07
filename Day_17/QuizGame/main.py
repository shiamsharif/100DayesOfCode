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

iter = 0

while quiz.still_has_questions():
    iter += 1
    quiz.next_question()
    if iter == 12:
        print("You've completed the quiz")
        print(f"Your final score was: {quiz.score}")

