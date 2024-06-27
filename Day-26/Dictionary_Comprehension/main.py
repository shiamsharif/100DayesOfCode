"""  new_dict = {new_key:new_value for item in list}  """
# import random
# names = ['Shiam', 'Jonh', 'Denver', 'Cena', 'Farhana', 'Fariha', 'Zarifah']
# students_scores = {student:random.randint(1,100) for student in names}
# print(students_scores)

# passed_Students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_Students)

""" Exercise-1 """
# sentence = "What is the airspeed velocity of an unladen swallow?"
# result = {sentence:len(sentence) for sentence in sentence.split()}
# print(result) 

# x = {name:((value * 9 / 5) + 32) for (name, value) in result.items()}
# print(x)


""" How to iterate over a pandas dateframe """
Students = {
    "student" : ["shiam", "CR7", "Messi"],
    "score" : [84,3,2]
}

for (key, value) in Students.items():
    print(value)


import pandas

students_data_frame = pandas.DataFrame(Students)
""" Create a file and append data in this file """
# stringdata = students_data_frame.to_string()
# with open("../Dictionary_Comprehension/file.txt", mode='w') as file1:
#     file1.write(stringdata) 
for (index, row) in students_data_frame.iterrows():
    if row.student == "shiam":
        print(row.score)