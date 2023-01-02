student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
# not particyularly useful
# for (key, value) in student_data_frame.items():
    # print(key)
    # print(value)

# Loop through rows a data frame
# iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
for (index, row) in student_data_frame.iterrows():
    print(index) # 0, 1, 2
    print(row) # row object
    print(row.student) # student
    if row.student == "Angela":
        print(row.score)
