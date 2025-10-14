#To-do list outline
#Needs to be able to:
#store a list of tasks, add, edit, and remove tasks, mark tasks as completed 
#or incomplete, and sort tasks by deadline or priority
#Variable needed and type:
#tasks: list of dictionaries, task title: string, task completed/incomplete: boolean
#due date: string, and task priority: integer

class to_do_list:
  def __init__(self):
    #makes an empty list to store tasks
    self.tasks=[]
    #list to store tasks as dictionaries with parameters/details
    #title, description, completion status, due date, priority, etc
    self.next_id=1
    #way to differentiate between tasks
    
  def add_task(self, title, description="", priority="Medium", due_date=None):
    #adds a new task to the to-do-list
    #set parameters:
    #title (str) = title of task
    #description (str) = description of task
    #due_date (str)= task deadline 
    pass
  
  def remove_task(self, task_id):
    #removes task from to-do list using its id
    pass
  
  def complete(self, task_id):
    #marks task with the given id as completed
    pass
  
  def view_tasks(self):
    #displays all the tasks and details (including complete/incomplete)
    pass
  
  def update_task(self, task_id, title=None, description=None, 
  priority=None, deadline=None):
    #updates parameters of the given task
    #only parameters made (not None) will be updated
    pass
    
  def clear_completed(self):
    #removes completed tasks
    pass
    
    
    