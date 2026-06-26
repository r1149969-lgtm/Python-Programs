tasks=[]

while True:

    print("\n===== To-Do App =====")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choise = input("Enter your choise: ")
    if choise == "1":
       task = input("Enter a task:")
       tasks.append(task)
       print("Task added successfully!")

    elif choise == "2":
       if len(tasks) == 0:
          print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print("{i + 1}.{tasks[i]}")
    elif choice == "3": 
    print("Delete option will be added next.")
    elif choise == "4":
    print("Thank you! Goodbye.")
    break
else:
    print("Invalid choice.Try again.")    