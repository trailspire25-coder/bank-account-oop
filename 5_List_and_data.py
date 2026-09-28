tasks = []

while True:
    task = input("Enter a task (or type'done' to finish): ")
    
    if task == "done":
        break
    else:
        tasks.append(task)

print("\nYour Task:")
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")
    

