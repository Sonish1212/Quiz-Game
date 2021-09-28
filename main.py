from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)


quiz_question = QuizBrain(question_bank)
while quiz_question.still_has_question():
    quiz_question.next_question()

