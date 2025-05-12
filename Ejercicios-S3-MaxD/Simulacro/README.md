
# Student Management System

## 📋 Description
This is a Python-based system designed for university administrators to manage student data. It allows the user to:
- Add students
- Search students by ID or name
- Update student information
- Delete students
- Calculate the average grade
- List students below a certain grade threshold

## 🚀 How to Run

Make sure you have Python 3 installed. Then run:

```bash
python student_manager.py
```

## 📦 Features and Examples

### 1. Add a Student
- Input: ID = 1006, Name = John Doe, Age = 21, Grade = 4.0
- Output: ✅ Student added successfully.

### 2. Search by ID
- Input: 1001
- Output: ✅ Found: 1001 - {'name': 'Alice Johnson', 'age': 20, 'grade': 4.5}

### 3. Search by Name
- Input: "Diana"
- Output: ✅ Match: 1004 - {'name': 'Diana Gomez', 'age': 19, 'grade': 4.1}

### 4. Update Student
- Input: Update grade for 1002 to 4.5
- Output: ✅ Grade updated successfully.

### 5. Delete Student
- Input: 1005
- Output: ✅ Student 1005 deleted successfully.

### 6. Calculate Average Grade
- Output: ✅ Average grade: 3.70

### 7. List Students Below Threshold
- Input: Threshold = 3.0
- Output: ✅ Below Threshold: 1003 - {'name': 'Carlos Diaz', 'age': 21, 'grade': 2.9}

## 🧱 Code Structure

- `student_manager.py`: The main program with all functionality.
  - Uses a dictionary to store student data.
  - Each operation is encapsulated in a function.
  - Input validation and colored output for better UX.

## 🎨 Message Colors

- ✅ Green: Success
- ⚠️ Yellow: Warning (e.g. not found)
- ❌ Red: Error (e.g. invalid input)

## 📌 Requirements

- Python 3.x
- No external libraries required
