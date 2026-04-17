import data
import random
full_question = random.choice(data.question_data)
text_only = full_question['text']
answer_only = full_question['answer']
class Question:
    def __init__(self):
        self.text = text_only
        self.answer = answer_only


q1 = Question()
