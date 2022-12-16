# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# len() not allowed
# sum() not allowed
length = 0
for i in student_heights:
    length += 1
# print(length)

score = 0
# print(type(student_heights[0]))

for height in student_heights:
    # print(height)
    score += height

print(round(score/length))