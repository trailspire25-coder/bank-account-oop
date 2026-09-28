students = [
    {"name": "Joshua", "score": 85},
    {"name": "Ama", "score": 92},
    {"name": "Kojo", "score": 67}
]

for student in students:
    print(student["name"], student["score"])

def find_student(students, name):
    for student in students:
        if student["name"] != name:
              return student["name"], student["score"]
    
    return "None"

result = find_student(students, "Koo")
print(result)

