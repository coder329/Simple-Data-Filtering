# Simple Data Filtering
# Task 8 - Level 1 - Day 8

students = [
    {"id": "S001", "name": "Rahul", "age": 20, "marks": 85, "department": "AI & ML"},
    {"id": "S002", "name": "Priya", "age": 21, "marks": 91, "department": "Data Science"},
    {"id": "S003", "name": "Aman", "age": 19, "marks": 72, "department": "Computer Science"},
    {"id": "S004", "name": "Neha", "age": 20, "marks": 88, "department": "AI & ML"},
    {"id": "S005", "name": "Riya", "age": 22, "marks": 95, "department": "Data Science"},
    {"id": "S006", "name": "Arjun", "age": 21, "marks": 67, "department": "Computer Science"}
]

print("===== ALL STUDENTS =====")
for student in students:
    print(student)

marks_filtered = [s for s in students if s["marks"] >= 85]
age_filtered = [s for s in students if s["age"] <= 20]
department_filtered = [s for s in students if s["department"] == "AI & ML"]
multiple_filtered = [s for s in students if s["marks"] >= 80 and s["age"] <= 20]

print("\n===== MARKS >= 85 =====")
for student in marks_filtered: print(student)

print("\n===== AGE <= 20 =====")
for student in age_filtered: print(student)

print("\n===== DEPARTMENT: AI & ML =====")
for student in department_filtered: print(student)

print("\n===== MARKS >= 80 AND AGE <= 20 =====")
for student in multiple_filtered: print(student)

print("\n===== FILTER COUNTS =====")
print("Marks Filter:", len(marks_filtered))
print("Age Filter:", len(age_filtered))
print("Department Filter:", len(department_filtered))
print("Multiple Condition Filter:", len(multiple_filtered))
