from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# This is going to be a list of question objects
question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # Created new_question obj. from Question class in model file
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# New obj quiz

quiz = QuizBrain(question_bank)

# if quiz has still remaining questions.
while quiz.still_has_question():
    quiz.new_question()

print("You have completed the Quiz !")
print(f"Your final score is: {quiz.score}/ {len(question_bank)}")
