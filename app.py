def main():
    
    class Task:
        #Task object creation
        def __init__(self, id, description, status, priority, date):
            pass

    class TaskList:
        #Task list of objects creation
        def __init__(self):
            self.tasks = []
            
            
        def addTask(self, task):
            #Add task to list
            self.tasks.append(task)
            
        def removeTask(self, taskID):
            #Remove task from list
            self.tasks.remove(taskID)
            
