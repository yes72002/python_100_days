from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

# new_q1 = Question(question_data[0]["text"], question_data[0]["answer"])
# print(new_q1.text)
# print(new_q1.answer)

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_qestion = Question(question_text, question_answer) # object
    question_bank.append(new_qestion) # append object
    # ddd = {} # dictionary
    # ddd["text"] = new_qestion.text
    # ddd["answer"] = new_qestion.answer
    # question_bank.append(ddd) # append dictionary

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question() # call method

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")