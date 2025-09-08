import json
import os
from datetime import datetime
from typing import List, Dict, Any

class Task:
    """Represents a single task"""
    
    def __init__(self, task_id: int, description: str, status: str = "pending"):
        self.id = task_id
        self.description = description
        self.status = status  # "pending" or "completed"
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for JSON serialization"""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_date": self.created_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary"""
        task = cls(data["id"], data["description"], data["status"])
        task.created_date = data["created_date"]
        return task

class TaskManager:
    """Main task manager class"""
    
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, description: str) -> None:
        """Add a new task"""
        if not description.strip():
            print("Error: Task description cannot be empty!")
            return
        
        task = Task(self.next_id, description.strip())
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Task '{description}' added successfully!")
    
    

def display_menu():
    """Display the main menu"""
    print("\n" + "="*30)
    print("PERSONAL TASK MANAGER")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("-"*30)


def main():
    """Main program loop"""
    task_manager = TaskManager()
    
    print("Welcome to Personal Task Manager!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:  # Add Task
            description = input("Enter task description: ")
            task_manager.add_task(description)
        
        elif choice == 2:  # View Tasks
            task_manager.view_tasks()
        
        elif choice == 3:  # Complete Task
            try:
                task_id = int(input("Enter task ID to complete: "))
                task_manager.complete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID number.")
        
        elif choice == 4:  # Delete Task
            try:
                task_id = int(input("Enter task ID to delete: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Please enter a valid task ID number.")
        
        elif choice == 5:  # Exit
            print("Thank you for using Personal Task Manager!")
            break
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
