import question_model
import data
questionbank = []
for question in data.question_data:
    questiont = question["text"]
    questiona = question["answer"]
    questionbank.append(question)
print(questionbank)
