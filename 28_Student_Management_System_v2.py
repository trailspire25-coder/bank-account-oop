def get_student_range():
    while True:
        try:
            student_range = int(input("\nEnter the number of students: "))
            if student_range < 1 or student_range > 100:
                print("Please enter between 1 and 100.")

            else:
                return student_range

        except ValueError:
            print("Please enter a valid number.")
    

def register_students(student_range):
    all_students = []
    students_grades = []

    for i in range(student_range):
        student_name = input("\nEnter student name: ")
        all_students.append(student_name)

        while True:
            try:
                student_score = int(input("Enter student score: "))
                if student_score < 0 or student_score > 100:
                    print("Please enter a number between 0 and 100.")
                else:
                    break
            except ValueError:
                print("Please enter a number.")

        students_grades.append(student_score)

    return all_students, students_grades


def get_grade(score):
    if score >= 90:
        return "Grade A"
    
    elif score >= 80:
        return"Grade B"
    
    elif score >= 70:
        return "Grade C"
    
    elif score >= 60:
        return "Grade D"
    
    elif score >= 50:
        return "Grade E"
    
    else:
         return "Grade F"


def view_students(all_students, students_grades):
    print("\n==== ALL STUDENTS ====")
    for i in range(len(students_grades)):
        grade = get_grade(students_grades[i])
        print(f"\n{all_students[i]}")
        print(f"Student: {students_grades[i]}")
        print(grade)


def search_student(all_students, students_grades):
    search = input("\nEnter the name you want to search: ").lower()
    
    if not search:
        print("Please enter a student name.")
        return
    found = False

    for i in range(len(all_students)):
        grade = get_grade(students_grades[i])
        if search in all_students[i].lower():
            print(f"\n{all_students[i]}")
            print(f"Score: {students_grades[i]}")
            print(grade)
            found = True
    
    if not found:
            print("Student not found")


def class_statistics(all_students, students_grades):
    top_scorers = []

    passed_students = 0
    failed_students = 0

    grade_a = 0
    grade_b = 0
    grade_c = 0
    grade_d = 0
    grade_e = 0
    grade_f = 0

    highest_score = max(students_grades)
    lowest_score = min(students_grades)
    average_score = sum(students_grades) / len(students_grades)
    
    lowest_index = students_grades.index(lowest_score)
    lowest_scorer = all_students[lowest_index]
    
    highest_index = students_grades.index(highest_score)
    top_scorer = all_students[highest_index]

    for i in range(len(all_students)):
        if students_grades[i] == highest_score:
            top_scorers.append(all_students[i])

    for i in students_grades:
        if i > 50:
            passed_students += 1
    
        else:
            failed_students += 1

    for i in range(len(students_grades)):
        grade = get_grade(students_grades[i])

        if grade == "Grade A":
            grade_a += 1

        elif grade == "Grade B":
            grade_b += 1
        
        elif grade == "Grade C":
            grade_c += 1
        
        elif grade == "Grade D":
            grade_d += 1
        
        elif grade == "Grade E":
            grade_e += 1

        else:
            grade_f += 1


    print("\n===== CLASS STATISTICS =====")
            
    print(f"\nTotal students: {student_range}")
            
    print(f"\nPassed: {passed_students}")
    print(f"Failed: {failed_students}")
        
    print(f"\nGrade A: {grade_a}")
    print(f"Grade B: {grade_b}")
    print(f"Grade C: {grade_c}")
    print(f"Grade D: {grade_d}")
    print(f"Grade E: {grade_e}")
    print(f"Grade F: {grade_f}")
                            
    print(f"\nHighest score: {highest_score}")
    print(f"lowest score: {lowest_score}")
            
    print(f"\nTop scorer: {top_scorer}")
    print(f"Score: {highest_score}")
            
    print(f"\nLowest scorer: {lowest_scorer}")
    print(f"Score: {lowest_score}")
            
    print(f"\nAverage Score: {average_score:.2f}")


def student_ranking(all_students, students_grades):

    student_data = list(zip(all_students, students_grades))
    student_data.sort(key=lambda x: x[1], reverse=True)

    for i, student in enumerate(student_data, start=1):
        print(f"{i}. {student[0]} - {student[1]} - {get_grade(student[1])}")


student_range = get_student_range()
all_students, students_grades = register_students(student_range)

while True:
    print("\n==== STUDENT GRADING SYSTEM ====")
    print("1. View Students")
    print("2. Search Students")
    print("3. Show Class Statistics")
    print("4. Students Ranking")
    print("5. Exit")

    choice = input("\nEnter Option: ")

    if choice == "1":
        view_students(all_students, students_grades)

    elif choice == "2":
        search_student(all_students, students_grades)

    elif choice == "3":
        class_statistics(all_students, students_grades)

    elif choice == "4":
        student_ranking(all_students, students_grades)

    elif choice == "5":
        print("\nGoodbye!!!")
        break

    else:
        print("\nInvalid Input!!!")
    


