import os
import csv
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Task A1 — Check File and Create Output Folder
print("Checking file...")
if not os.path.exists("students.csv"):
    print("Error: students.csv not found. Please download the file from LMS.")
    exit()
print("File found: students.csv")

print("Checking output folder...")
if not os.path.exists("output"):
    os.makedirs("output")
    print("Output folder created: output/")
else:
    print("Output folder already exists: output/")

# Task A2 — Read CSV and Preview Data
with open("students.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    students = list(reader)

print(f"Total students: {len(students)}")
print("First 5 rows:")
print("-" * 30)
for student in students[:5]:
    print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
print("-" * 30)

# Task A3 — GPA Analysis
gpas = []
high_performers = 0

for student in students:
    gpa = float(student["GPA"])
    gpas.append(gpa)
    if gpa > 3.5:
        high_performers += 1

avg_gpa = round(sum(gpas) / len(gpas), 2)
max_gpa = max(gpas)
min_gpa = min(gpas)

print("-" * 30)
print("GPA Analysis")
print("-" * 30)
print(f"Total students : {len(students)}")
print(f"Average GPA    : {avg_gpa}")
print(f"Highest GPA    : {max_gpa}")
print(f"Lowest GPA     : {min_gpa}")
print(f"Students GPA>3.5 : {high_performers}")
print("-" * 30)

# Task A4 — Save Results to JSON and Print Summary
result = {
    "analysis": "GPA Statistics",
    "total_students": len(students),
    "average_gpa": avg_gpa,
    "max_gpa": max_gpa,
    "min_gpa": min_gpa,
    "high_performers": high_performers
}

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print("=" * 30)
print("ANALYSIS RESULT")
print("=" * 30)
print(f"Analysis       : GPA Statistics")
print(f"Total students : {len(students)}")
print(f"Average GPA    : {avg_gpa}")
print(f"Highest GPA    : {max_gpa}")
print(f"Lowest GPA     : {min_gpa}")
print(f"High performers: {high_performers}")
print("=" * 30)
print("Result saved to output/result.json")