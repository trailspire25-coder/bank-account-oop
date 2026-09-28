student_names = []
student_scores = []


while True:
    try:
        student_range = int(input("How many students do you want to enter: "))

        if student_range < 1 or student_range > 100:
            print("Please enter between 0 and 100.")

        else:
            break

    except ValueError:
        print("Please enter a number.")



for i in range(student_range):
    names = input("\nEnter Student Name: ")
    student_names.append(names)

    while True:
        try:
            scores = int(input("Enter Student Score: "))

            if scores < 0 or scores > 100:
                    print("Score must be between 0 to 100")
            
            else:
                break

        except ValueError:
            print("Please enter a number.")

    student_scores.append(scores)


while True:
    print("\n==== STUDENTS ====")
    print("1. View Students")
    print("2. Search Students")
    print("3. Show Class Statistics")
    print("4. Students Ranking")
    print("5. Exit")

    choice = input("\nEnter Option: ")

    if choice == "1":
        for i in range(student_range):
            print(f"\n{student_names[i]}")
            print(f"Score: {student_scores[i]}")

            if student_scores[i] >= 90:
                print("Grade A")

            elif student_scores[i] >= 80:
                print("Grade B")

            elif student_scores[i] >= 70:
                print("Grade C")

            elif student_scores[i] >= 60:
                print("Grade D")

            elif student_scores[i] >= 50:
                print("Grade E")

            else:
                print("Grade F")

            

    elif choice == "2":
        search = input("\nEnter the name you want to search: ").lower()
        if not search:
            print("Please enter a student name.")
            continue
        found = False
        for i in range(student_range):
            if search in student_names[i].lower():
                print(f"\n{student_names[i]}")
                print(f"Score: {student_scores[i]}")
                found = True

        if not found:
            print("Student not found")

    elif choice == "3":
        top_scorers = []

        passed_students = 0
        failed_students = 0

        grade_a = 0
        grade_b = 0
        grade_c = 0
        grade_d = 0
        grade_e = 0
        grade_f = 0

        highest_score = max(student_scores)
        lowest_score = min(student_scores)
        average = sum(student_scores) / len(student_scores)

        lowest_index = student_scores.index(lowest_score)
        lowest_scorer = student_names[lowest_index]

        highest_index = student_scores.index(highest_score)
        top_scorer = student_names[highest_index]

        for i in range(student_range):
            if student_scores[i] == highest_score:
                top_scorers.append(student_names[i])


        for i in range(student_range):
            if student_scores[i] >= 90:
                grade_a += 1
            
            elif student_scores[i] >= 80:
                grade_b += 1
            
            elif student_scores[i] >= 70:
                grade_c += 1
            
            elif student_scores[i] >= 60:
                grade_d += 1
            
            elif student_scores[i] >= 50:
                grade_e += 1
            
            else:
                grade_f += 1


        for score in student_scores:
            if score >= 50:
                passed_students += 1

            else:
                failed_students += 1

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

        print("\nTop scorers:")
        for i in top_scorers:
            print(i)
        print(f"\nScore: {highest_score}")
        

        print(f"\nLowest scorer: {lowest_scorer}")
        print(f"Score: {lowest_score}")

        print(f"\nAverage Score: {average:.2f}")

    elif choice == "4":
        student_grades = []

        for i in range(student_range):
            if student_scores[i] >= 90:
                student_grades.append("Grade A")

            elif student_scores[i] >= 80:
                student_grades.append("Grade B")

            elif student_scores[i] >= 70:
                student_grades.append("Grade C")

            elif student_scores[i] >= 60:
                student_grades.append("Grade D")

            elif student_scores[i] >= 50:
                student_grades.append("Grade E")

            else:
                student_grades.append("Grade F")        

        students = list(zip(student_names, student_scores, student_grades))
        students.sort(key=lambda student: student[1], reverse=True)

        for i, student in enumerate(students, start=1):
            print(f"{i}. {student[0]} - {student[1]} - {student[2]}")


    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid Input. Try again.")
            
