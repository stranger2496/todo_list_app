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
    #Shows the task in string form
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
        for task in self.tasks[:]:
            #if task has same id has user input
            if taskId == task.id:
                #remove task from list
                self.tasks.remove(task)
                return f"Removed task: {task}" #Confirm remove
            return f"Task ID {taskId} not found"

    def showList(self):
        for task in self.tasks:
            print(f"\n{task}\n")
def main():
    print("working")
    """
    
    Console and GUI version of the application
    Set to True for application window
    Set to False for simplified console version
    
    """
    user_gui = False
    #Create instance of TaskList so main can access functions
    todo = TaskList()
    
    #Testing
    while user_gui == False:
        print("--------------")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show Tasks")
        print("4. Exit")
        print("--------------")
        
        user_input = input("\nInput Number: ")
        #instead of elif, I like this better
        #takes user input and matches it to a case
        match user_input:
            case "1":   
                task_input = []
                print("--------------")
                task_input.append(input("Task Description:\n"))
                print("--------------")
                print("Enter Priority")
                print("--------------")
                print("1. Low")
                print("2. Medium")
                print("3. High")
                print("--------------")
                task_input.append(input("\nInput(Low/Medium/High): "))
                
                #Call addTask function in TaskList class
                #Send user input
                #print needed to display task
                print(todo.addTask(task_input[0], task_input[1]))
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
