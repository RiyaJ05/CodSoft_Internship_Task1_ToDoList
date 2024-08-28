import os

class Task:
  """
  A class representing a task in the to-do list.

  Attributes:
      desc (str): Description of the task.
      status (str): Status of the task, e.g., "Backlog", "Ongoing", "Done".
      priority (str): Priority of the task, e.g., "Low", "Med", "High".
  """

  tasks_dict = {
    "Backlog": [],
    "Ongoing": [],
    "Done": []
  }
  STATUS_LEVELS = ("Backlog", "Ongoing", "Done")
  PRIORITY_LEVELS = ("Low", "Med", "High")

  def __init__(self, desc, status, priority):
    """
    Initialize a Task instance.

    Args:
        desc (str): Description of the task.
        status (str): Status of the task.
        priority (str): Priority of the task.
    """
        
    self.desc = desc
    self.status = status
    self.priority = priority

  def add_task(self):
    """
    Add the current task to the appropriate category in tasks_dict.
    """

    if self.status.lower() == "backlog":
      Task.tasks_dict["Backlog"].append(self)
    
    elif self.status.lower() == "ongoing":
      Task.tasks_dict["Ongoing"].append(self)

    elif self.status.lower() == "done":
      Task.tasks_dict["Done"].append(self)

  @staticmethod
  def display_all_tasks():
    """
    Display all tasks grouped by their status in a formatted manner.
    """

    for category in Task.tasks_dict:
      task_num = 1
      
      if category.lower() == "backlog":
        print("\n" + "=" * 61)
        print(f"|  {f"{len(Task.tasks_dict['Backlog'])} Backlog Task(s)" :^55s}  |")
        print("-" * 61)
        for task in Task.tasks_dict[category]:
          print(f"|  {f"{task_num}. {task}" :^55s}  |")
          task_num += 1
        print("=" * 61)

      elif category.lower() == "ongoing":
        print("\n\n" + "=" * 61)
        print(f"|  {f"{len(Task.tasks_dict['Ongoing'])} Ongoing Task(s)" :^55s}  |")
        print("-" * 61)
        for task in Task.tasks_dict[category]:
          print(f"|  {f"{task_num}. {task}" :^55s}  |")
          task_num += 1
        print("=" * 61)

      elif category.lower() == "done":
        print("\n\n" + "=" * 61)
        print(f"|  {f"{len(Task.tasks_dict['Done'])} Done Task(s)" :^55s}  |")
        print("-" * 61)
        for task in Task.tasks_dict[category]:
          print(f"|  {f"{task_num}. {task}" :^55s}  |")
          task_num += 1
        print("=" * 61)

  def remove_task(self):
    """
    Remove the current task from its category in tasks_dict.
    """

    Task.tasks_dict[self.status].remove(self)

  def update_task(self, new_desc, new_status, new_priority):
    """
    Update the task with new description, status, and priority.

    Args:
        new_desc (str): New description for the task.
        new_status (str): New status for the task.
        new_priority (str): New priority for the task.
    """

    new_task = Task(new_desc, new_status, new_priority)
    self.remove_task()

    if new_status.lower() == "backlog":
      Task.tasks_dict["Backlog"].append(new_task)
    elif new_status.lower() == "ongoing":
      Task.tasks_dict["Ongoing"].append(new_task)
    elif new_status.lower() == "done":
      Task.tasks_dict["Done"].append(new_task)
      
  @staticmethod
  def status_validator(task_status):
    """
    Validate and correct the task status input.

    Args:
        task_status (str): Status to validate.

    Returns:
        str: Validated status.
    """

    while task_status.capitalize() not in Task.STATUS_LEVELS:
      task_status = input(f"Invalid Status! Please select a suitable task status ({Task.STATUS_LEVELS}): ")
    return task_status.capitalize()

  @staticmethod
  def priority_validator(task_priority):
    """
    Validate and correct the task priority input.

    Args:
        task_priority (str): Priority to validate.

    Returns:
        str: Validated priority.
    """

    while task_priority.capitalize() not in Task.PRIORITY_LEVELS:
      task_priority = input(f"Invalid Priority! Please select a suitable task priority ({Task.PRIORITY_LEVELS}): ")
    return task_priority.capitalize()

  def __str__(self):
    """
    Return a string representation of the task.

    Returns:
        str: Formatted string of the task.
    """

    return f"Task: {self.desc:<25s} Priority: {self.priority:<5s}"


def menu():
  """
  Display the main menu of the To-Do List application.
  """

  print("\n" + "=" * 21)
  print("To-Do List")
  print("=" * 21)
  print("1. View all the Tasks")
  print("2. Add a Task")
  print("3. Delete a Task")
  print("4. Update a Task")
  print("5. Exit \n")


def load_list_from_file(file_path):
  """
  Load tasks from a file and populate the tasks_dict.

  Args:
      file_path (str): Path to the file containing tasks.
  """

  try:
    with open(file_path) as file:
      line = file.readline()
      while line:
        line_list = line.strip().split(",")
        task_status = line_list[1]
        task_obj = Task(line_list[0], task_status, line_list[2])

        if (task_status.lower() == "backlog"):
          Task.tasks_dict["Backlog"].append(task_obj)

        elif (task_status.lower() == "ongoing"):
          Task.tasks_dict["Ongoing"].append(task_obj)

        elif (task_status.lower() == "done"):
          Task.tasks_dict["Done"].append(task_obj)
        
        line = file.readline()

  except FileNotFoundError:
    # Starting with an empty tasks list
    pass

  except Exception as e:
    print(f"Error: {e}")


def write_list_to_file(file_path):
  """
  Write all tasks from tasks_dict to a file.

  Args:
      file_path (str): Path to the file to write tasks.
  """

  try:
    with open(file_path, "w") as file:
      for category in Task.tasks_dict:
        for task in Task.tasks_dict[category]:
          file.write(f"{task.desc},{task.status},{task.priority}\n")
  
  except Exception as e:
    print(f"Error: {e}")


def main():
  """
  Main function to run the To-Do List application.
  """

  # Define file path for tasks data
  file_name = "Tasks.txt"
  file_path = os.path.join(os.getcwd(), file_name)

  # Load existing tasks from file
  load_list_from_file(file_path)

  run = True
  while run:
    # Display main menu
    menu()

    # Get user input for menu option
    menu_op = input("Select a menu option: ")

    # View all tasks
    if menu_op == "1":
      Task.display_all_tasks()

    # Add a new task
    elif menu_op == "2":
      task_desc = input("\nEnter a task description: ")
      task_status = input(f"Select a task status ({Task.STATUS_LEVELS}): ")
      task_status = Task.status_validator(task_status)
      task_priority = input(f"select a task priority level ({Task.PRIORITY_LEVELS}): ")
      task_priority = Task.priority_validator(task_priority)

      task = Task(task_desc, task_status.capitalize(), task_priority.capitalize())
      task.add_task()

      print("\nTask added successfully!")


    # Delete an existing task
    elif menu_op == "3":
      Task.display_all_tasks()

      try:
        del_task_category = input(f"\nSelect the task status of the task you want to delete ({Task.STATUS_LEVELS}): ")
        del_task_category = Task.status_validator(del_task_category)
        del_task_num = int(input("Enter the task number of the task you want to delete: "))
        idx_to_del = del_task_num - 1
        Task.tasks_dict[del_task_category].pop(idx_to_del)
        print("\nTask deleted successfully!")
    
      except Exception as e:
        print(f"ERROR: {e}")
        

    # Update an existing task
    elif menu_op == "4":
      print("\n" + "*" * 30)
      print("What would you like to update?")
      print("*" * 30)
      print("1. Task Description \n2. Task Status \n3. Task Priority")
      upd_op = input("\nEnter your update selection: ")

      # Update task description
      if upd_op == "1":
        Task.display_all_tasks()
        
        try:
          upd_task_category = input(f"\nSelect the task status of the task you want to update ({Task.STATUS_LEVELS}): ")
          upd_task_category = Task.status_validator(upd_task_category)
          upd_task_num = int(input("Enter task number of the task you want to update: "))
          idx_to_upd = upd_task_num - 1
          old_task = Task.tasks_dict[upd_task_category][idx_to_upd]
          new_desc = input("Enter the new task description: ")
          old_task.update_task(new_desc, old_task.status, old_task.priority)
          print("\nTask updated successfully!")

        except Exception as e:
          print(f"Error: {e}")

      # Update task status
      elif upd_op == "2":
        Task.display_all_tasks()

        try:
          upd_task_category = input(f"\nSelect the task status of the task you want to update ({Task.STATUS_LEVELS}): ")
          upd_task_category = Task.status_validator(upd_task_category)
          upd_task_num = int(input("Enter task number of the task you want to update: "))
          idx_to_upd = upd_task_num - 1
          old_task = Task.tasks_dict[upd_task_category][idx_to_upd]
          new_status = input(f"Enter the new task status ({Task.STATUS_LEVELS}): ")
          new_status = Task.status_validator(new_status)
          old_task.update_task(old_task.desc, new_status, old_task.priority)
          print("\nTask updated successfully!")
        
        except Exception as e:
          print(f"ERROR: {e}")

      # Update task priority
      elif upd_op == "3":
        Task.display_all_tasks()

        try:
          upd_task_category = input(f"\nSelect the task status of the task you want to update ({Task.STATUS_LEVELS}): ")
          upd_task_category = Task.status_validator(upd_task_category)
          upd_task_num = int(input("Enter task number of the task you want to update: "))
          idx_to_upd = upd_task_num - 1
          old_task = Task.tasks_dict[upd_task_category][idx_to_upd]
          new_priority = input(f"Enter the new task priority ({Task.PRIORITY_LEVELS}): ")
          new_priority = Task.priority_validator(new_priority)
          old_task.update_task(old_task.desc, old_task.status, new_priority)
          print("\nTask updated successfully!")
        
        except Exception as e:
          print(f"ERROR: {e}")

      else:
        upd_op = input("\nInvalid option! Please enter a suitable update selection: ")


    # Exit the program and save tasks to file
    elif menu_op == "5":
      run = False
      print("\nTHANK YOU FOR USING THIS TO-DO LIST APPLICATION! Exiting... \n")


    # Handle invalid menu option
    else:
      print("\nInvalid option! Please try again...")
    
  write_list_to_file(file_path)


if __name__ == "__main__":
  main()