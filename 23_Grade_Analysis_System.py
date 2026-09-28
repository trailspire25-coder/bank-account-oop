grades = []

total_scores = 0
passed_scores = 0
failed_scores = 0
grade_A = 0
grade_B = 0
grade_C = 0
grade_D = 0
grade_E = 0
grade_F = 0

range_score = int(input("How many students score do you want to enter: "))

while range_score <= 0:
    range_score = int(input("How many students score do you want to enter: "))

for i in range(range_score):
    score = int(input("Enter student grades: "))

    while score < 0 or score > 100:
        score = int(input("Enter student grades again: "))
    grades.append(score)

for grade_score in grades:
    total_scores += grade_score

for grades_score in grades:
    if grades_score >= 50:
       passed_scores += 1 

    else:
        failed_scores += 1

for grades_scores in grades:
    if grades_scores >= 90:
        gradeA = grades_scores
        grade_A += 1

    elif grades_scores >= 80:
        gradeB = grades_scores
        grade_B += 1

    elif grades_scores >= 70:
        gradeC = grades_scores
        grade_C += 1

    elif grades_scores >= 60:
        gradeD = grades_scores
        grade_D += 1

    elif grades_scores >= 50:
        gradeE = grades_scores
        grade_E += 1

    else:
        gradeF = grades_scores
        grade_F += 1
        

average = total_scores / range_score
highest = max(grades)
lowest = min(grades)
passed_percentage = passed_scores / range_score * 100

print("\n============ GRADE ANALYSIS ===========")
print(f"\nGrades: {grades}")
print(f"\nHighest Grade: {highest}")
print(f"Total Grade: {total_scores}")
print(f"Lowest Grade: {lowest}")
print(f"Average Grade: {average}")
print(f"\nPassed Grades: {passed_scores}")
print(f"Failed Grades: {failed_scores}")
print(f"Pass Percentage: {passed_percentage}%")
print(f"\nA Grade: {grade_A}")
print(f"B Grade: {grade_B}")
print(f"C Grade: {grade_C}")
print(f"D Grade: {grade_D}")
print(f"E Grade: {grade_E}")
print(f"F Grade: {grade_F}")
