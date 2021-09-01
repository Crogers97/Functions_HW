tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# 1

def uncompleted_tasks(list, completed):
    uncompleted = []
    for task in list:
        if task["completed"] == False:
            uncompleted.append(task)
    return uncompleted

print(uncompleted_tasks(tasks, False))  

# 2
def completed_tasks(list, completed):
    completed = []
    for task in list:
        if task["completed"] == True:
            completed.append(task)
    return completed

print(completed_tasks(tasks, True))

# 3
def task_descriptions(list):
    task_description = []
    for task in list:
        task_description.append(task["description"])
    return task_description

print(task_descriptions(tasks))


# 4
def task_time(list):
    task_time = []
    for task in list:
        if task["time_taken"] > 0:
            task_time.append(task)
    return task_time 

print(task_time(tasks))


# 5
def given_description(list, description):
    given_description = []
    for task in list:
        if task["description"] == "Wash Dishes":
            given_description.append(task)
    return given_description

print(given_description(tasks, "wash Dishes"))

# 6
tasks[3]["completed"] = True
print(tasks)

# 7
tasks.append({
    "description": "Feed Fish",
    "completed": True ,
    "time_taken": 2
})

print(tasks)

# 8
menu= input("Input a number")
def menu(number)
i = 0
numbers = []

while menu = 1:
    numbers.append(menu)
print()








            











        
