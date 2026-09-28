
def get_grade(student_scores):
    if student_scores >= 90:
        return "Grade A"
    elif student_scores >= 80:
        return "Grade B"
    elif student_scores >= 70:
        return "Grade C"
    elif student_scores >= 60:
        return "Grade D"
    elif student_scores >= 50:
        return "Grade E"
    else:
        return "Grade F"
    
student_names = ["Joshua", "Ama", "Kojo"]
student_scores = [85, 92, 67]

for i in range(len(student_names)):
    grade = get_grade(student_scores[i])
    print(student_names[i], grade)





def add_bonus(score):
    return score + 5

def double_score(score):
    return score * 2

final_answer = double_score(add_bonus(75))
print(final_answer)





scores =[85, 92, 67, 74]

def get_total(scores):
    total = 0
    for i in range(len(scores)):
        total += scores[i]
    return total

def get_average(scores):
    total = get_total(scores)
    average = total /len(scores)
    return average
    
result = get_total(scores)
print(result)
print(get_average(scores))





def check_result(score):
    if score >= 50:
        return "Pass"

    else:
        return "Fail"

print(check_result(67))
print(check_result(42))




def calculate_bonus(score, bonus=5):
    return score + bonus

print(calculate_bonus(80))
print(calculate_bonus(80, 10))




def calculate_total(*marks):
    total = 0
    
    for mark in marks:
        total += mark
    return total
    
print(calculate_total(80, 90, 75))



def student_info(**details):
    for key, value in details.items():
        print(f"{key} {value}"),

student_info(name = "Joshua", score = 85, grade = "A")




def create_student(name, score):
    return{
        "name": name,
        "score": score,
        "grade":  "A" if score >= 90 else "B"
    }

print(create_student("Joshua", 92))
