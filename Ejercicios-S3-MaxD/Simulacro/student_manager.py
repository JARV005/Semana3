
# student_manager.py
# Student Management System for a University
# Author: [Your Name]
# Description: This script allows a university director to manage student records, including registration, search, update, deletion, and performance analysis.

# ANSI color variables for better message display
COLOR_DANGER = "\033[91m"   # Light red for errors
COLOR_WARNING = "\033[93m"  # Light yellow for warnings
COLOR_SUCCESS = "\033[92m"  # Light green for success
COLOR_RESET = "\033[0m"     # Reset to default color

# Initial student database with at least 5 students
students_db = {
    "1001": {"name": "Alice Johnson", "age": 20, "grade": 4.5},
    "1002": {"name": "Bob Smith", "age": 22, "grade": 3.8},
    "1003": {"name": "Carlos Diaz", "age": 21, "grade": 2.9},
    "1004": {"name": "Diana Gomez", "age": 19, "grade": 4.1},
    "1005": {"name": "Evelyn Martinez", "age": 23, "grade": 3.2}
}

# ------------------ Core Functions ------------------ #

def add_student():
    """Add a new student if the ID is unique and data is valid."""
    student_id = input("Enter student ID: ").strip()
    if student_id in students_db:
        print(f"{COLOR_DANGER}Error: Student with ID {student_id} already exists.{COLOR_RESET}")
        return
    name = input("Enter full name: ").strip()
    try:
        age = int(input("Enter age: ").strip())
        if age <= 0:
            print(f"{COLOR_DANGER}Error: Age must be a positive integer.{COLOR_RESET}")
            return
        grade = float(input("Enter grade (0.0 - 5.0): ").strip())
        if not (0.0 <= grade <= 5.0):
            print(f"{COLOR_DANGER}Error: Grade must be between 0.0 and 5.0.{COLOR_RESET}")
            return
    except ValueError:
        print(f"{COLOR_DANGER}Error: Invalid input type for age or grade.{COLOR_RESET}")
        return

    students_db[student_id] = {"name": name, "age": age, "grade": grade}
    print(f"{COLOR_SUCCESS}Student added successfully.{COLOR_RESET}")

def search_student_by_id():
    """Search a student by their unique ID."""
    student_id = input("Enter student ID to search: ").strip()
    student = students_db.get(student_id)
    if student:
        print(f"{COLOR_SUCCESS}Found: {student_id} - {student}{COLOR_RESET}")
    else:
        print(f"{COLOR_WARNING}Student with ID {student_id} not found.{COLOR_RESET}")

def search_student_by_name():
    """Search for students by partial or full name."""
    name_query = input("Enter name or part of name to search: ").strip().lower()
    found = False
    for sid, data in students_db.items():
        if name_query in data['name'].lower():
            print(f"{COLOR_SUCCESS}Match: {sid} - {data}{COLOR_RESET}")
            found = True
    if not found:
        print(f"{COLOR_WARNING}No students found with the name '{name_query}'.{COLOR_RESET}")

def update_student():
    """Update a student's age or grade."""
    student_id = input("Enter student ID to update: ").strip()
    student = students_db.get(student_id)
    if not student:
        print(f"{COLOR_WARNING}Student with ID {student_id} does not exist.{COLOR_RESET}")
        return

    print("What would you like to update?")
    print("1. Age")
    print("2. Grade")
    choice = input("Select an option: ").strip()

    if choice == "1":
        try:
            new_age = int(input("Enter new age: ").strip())
            if new_age > 0:
                student["age"] = new_age
                print(f"{COLOR_SUCCESS}Age updated successfully.{COLOR_RESET}")
            else:
                print(f"{COLOR_DANGER}Error: Age must be a positive integer.{COLOR_RESET}")
        except ValueError:
            print(f"{COLOR_DANGER}Error: Invalid age format.{COLOR_RESET}")
    elif choice == "2":
        try:
            new_grade = float(input("Enter new grade (0.0 - 5.0): ").strip())
            if 0.0 <= new_grade <= 5.0:
                student["grade"] = new_grade
                print(f"{COLOR_SUCCESS}Grade updated successfully.{COLOR_RESET}")
            else:
                print(f"{COLOR_DANGER}Error: Grade must be between 0.0 and 5.0.{COLOR_RESET}")
        except ValueError:
            print(f"{COLOR_DANGER}Error: Invalid grade format.{COLOR_RESET}")
    else:
        print(f"{COLOR_WARNING}Invalid option selected.{COLOR_RESET}")

def delete_student():
    """Remove a student from the database."""
    student_id = input("Enter student ID to delete: ").strip()
    if student_id in students_db:
        del students_db[student_id]
        print(f"{COLOR_SUCCESS}Student {student_id} deleted successfully.{COLOR_RESET}")
    else:
        print(f"{COLOR_WARNING}Student with ID {student_id} not found.{COLOR_RESET}")

def calculate_average_grade():
    """Calculate and display the average grade of all students."""
    if not students_db:
        print(f"{COLOR_WARNING}No students to calculate average.{COLOR_RESET}")
        return
    avg = sum(s["grade"] for s in students_db.values()) / len(students_db)
    print(f"{COLOR_SUCCESS}Average grade: {avg:.2f}{COLOR_RESET}")

def list_students_below_threshold():
    """List students with grades below a given threshold."""
    try:
        threshold = float(input("Enter threshold grade (default is 3.0): ").strip() or 3.0)
    except ValueError:
        print(f"{COLOR_DANGER}Error: Invalid threshold input.{COLOR_RESET}")
        return

    found = False
    for sid, data in students_db.items():
        if data["grade"] < threshold:
            print(f"{COLOR_SUCCESS}Below Threshold: {sid} - {data}{COLOR_RESET}")
            found = True
    if not found:
        print(f"{COLOR_WARNING}No students below threshold {threshold}.{COLOR_RESET}")

# ------------------ Menu System ------------------ #

def menu():
    """Display the main menu and handle user selections."""
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Search Student by ID")
        print("3. Search Student by Name")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Calculate Average Grade")
        print("7. List Students Below Grade Threshold")
        print("8. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student_by_id()
        elif choice == "3":
            search_student_by_name()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_average_grade()
        elif choice == "7":
            list_students_below_threshold()
        elif choice == "8":
            print(f"{COLOR_SUCCESS}Exiting system. Goodbye!{COLOR_RESET}")
            break
        else:
            print(f"{COLOR_WARNING}Invalid choice. Please try again.{COLOR_RESET}")

# ------------------ Entry Point ------------------ #
if __name__ == "__main__":
    menu()
