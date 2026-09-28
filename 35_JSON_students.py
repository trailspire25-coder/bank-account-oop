import json

with open("students.json", "r") as file:
    students = json.load(file)
    print(type(students))
    print(type(students[0]))
    print(type(students[0]["age"]))
    print(f'{students[1]["name"]} is {students[1]["age"]} years old')
    total = 0
    for student in students:
        print(f'{student["name"]} is {student["age"]} years old')
        total += student["age"]
        average = total / len(students)
    print(total)
    print(average)

    students[1]['age'] = 23

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
print(students[1]["age"])


data = {"name": "Ama", "age": 20}
data2 = '{"name": "Ama", "age": 20}'
json.loads(data2)
json.dumps(data)
print(data2)
print(data)
