import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_dict = {new_key:new_value for item in list}
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
passed_scores = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_scores)


