#add things to collection of something, or other

grades = [50, 100, 80, 90]
#correct number is 90.6

# add them together
# divide for our average grade

total = 0  # the accumulator variable
for grade in grades:
    total = total + grade
    # # add each of our grades to the total
    # print(f'grade: {grade}')

    # # first time through the loop:
    # # total + grade: 0 + 50 = 50
    # # 2nd time through the loop:
    # # total + grade: 50 + 100 = 150
    # print(f'total + grade: {total} + {grade} = {total + grade}')
    # total += grade # 150

print(total)

# total = sum(grades)
avg_grade = total / len(grades)
print(avg_grade)

words = ['This', 'is', 'a', 'sentence!']

sentence = ''
for word in words:
    sentence = sentence + word + ' '

print(sentence)