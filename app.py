#this library is going to be used to track when the task was created
from datetime import datetime

#Reminder to create unit tests
class Task:
    #Task object creation
    def __init__(self, id, description, status, priority, date):
        self.id = id
        self.description = description
        self.status = status
        self.priority = priority
        self.date = date
    #this will give a good print to screen version of a task for the user to see
    def __str__(self):
        return f"ID: {self.id}, Desc: {self.description}, Status: {self.status}, Priority: {self.priority}, Date: {self.date}"
            
class TaskList:
    #Task list of objects creation
    def __init__(self):
        self.tasks = []
            
    def addTask(self, description= " ", priority=None):
        #Console version functionality for user input of a new task     
        #Add task to list
        #Assign id to task based off of the count of the list
        task = Task(len(self.tasks), description, status=False, priority=priority, date=datetime.now())
        self.tasks.append(task)
        
        #display task through __str__
        f"Added task: {task}"

    def removeTask(self, taskId):
        #loop through tasks
        for task in self.tasks[:]: #[:] slice creates temp tasks list to iterate through without bugging out
            #if task has same id has user input
            if taskId == task.id:
                #remove task from list
                self.tasks.remove(task)
                return f"Removed task: {task}" #Confirm remove
            #If user inputs the wrong id or wrong format
            return f"Task ID {taskId} not found"

    def showList(self):
        for task in self.tasks:
            print(f"\n{task}\n")
def main():
    """
    
    Console and GUI version of the application
    
    Set to True for application window
    Set to False for simplified console version
    
    """
    user_gui = False
    #Create instance of TaskList so main can access functions
    todo = TaskList()
    #False for simplified console version
    while user_gui == False:
        #simple user interface
        print("--------------")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show Tasks")
        print("4. Exit")
        print("--------------")
        #grabs input from user
        user_input = input("\nInput Number: ")
        #instead of elif, I like this better
        #takes user input and matches it to a case
        match user_input:
            case "1":   
                
                print("--------------")
                task_descr = input("Task Description:\n\n")

                while True:
                    print("--------------")
                    print("Enter Priority")
                    print("--------------")
                    print("1. Low")
                    print("2. Medium")
                    print("3. High")
                    print("--------------")
                    task_prio = input("\nInput(Low/Medium/High): ")
                    if task_prio == "Low" or task_prio == "Medium" or task_prio == "High":
                        print(todo.addTask(task_descr, task_prio))
                        break
                    else:
                        print(f"{task_prio} is not a valid priority")
                

                
                #Call addTask function in TaskList class
                #Send user input
                #print needed to display task
            case "2":
                print("--------------")
                print("Enter Task Id")
                print("--------------")
                task_id = input("\nInput Number: ")
                print(todo.removeTask(int(task_id)))
            case "3":
                todo.showList()
            case "4":
                break
if __name__ == "__main__":
    main()    
