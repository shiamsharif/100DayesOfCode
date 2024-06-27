"""  new_dict = {new_key:new_value for item in list}  """
# import random
# names = ['Shiam', 'Jonh', 'Denver', 'Cena', 'Farhana', 'Fariha', 'Zarifah']
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

# passed_Students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_Students)

""" Exercise-1 """
sentence = "What is the airspeed velocity of an unladen swallow?"
result = {sentence:len(sentence) for sentence in sentence.split()}
print(result)