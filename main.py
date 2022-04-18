from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer)
# for q in question_bank:
#     print(q.text)
#     print(q.answer)

quiz = QuizBrain(question_bank)
points = 0
for _ in question_bank:
    user_ans = quiz.next_question()
    if user_ans == "C":
        points += 1

print(f"You got {points} answers right..")
