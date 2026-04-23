import random
import numpy as g
import pandas as r
import math
def generate_data(number):
    students_data = []
    for i in range(1, number+1):
        student_id = f"Student{i}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        # Performance Index
        performance_index = (marks * 0.7 + assignment * 0.3) * math.log(attendance + 2)
        students_data.append((student_id, marks, attendance, assignment, performance_index))
    return students_data

def classify_students(d):
    category = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }
    for student in d:
        sid, marks, attendance, assignment, pi = student
        if marks > 90 and attendance > 80:
            category["Top Performer"].append(sid)
        elif marks < 40 or attendance < 50:
            category["At Risk"].append(sid)
        elif 71 <= marks <= 90:
            category["Good"].append(sid)
        elif 40 <= marks <= 70:
            category["Average"].append(sid)
    return category

def analyze_data(student_data):
    marks_array = g.array(student_data['Marks'])
    total = sum(marks_array)
    mean_marks = total / len(marks_array)
    median_marks = g.median(marks_array)
    std_dev = g.std(marks_array)
    max_marks = g.max(marks_array)
    correlation = g.corrcoef(student_data['Marks'], student_data['Attendance'])[0][1]
    min_marks = g.min(marks_array)
    maxi_marks = g.max(marks_array)
    if maxi_marks == min_marks:
        student_data['Normalized Marks'] = [0 for _ in marks_array]
    else:
        student_data['Normalized Marks'] = [(x - min_marks) / (maxi_marks - min_marks) for x in marks_array]
    consistency = std_dev < 20
    attendance_risk = len([x for x in student_data['Attendance'] if x < 50]) > 3
    top_performers = len([i for i in range(len(student_data))
        if student_data['Marks'][i] > 90 and student_data['Attendance'][i] > 80]) >= 2
    if consistency and top_performers:
        in_sight = "Excellent Performance"
    elif attendance_risk:
        in_sight = "Critical Attention Required"
    else:
        in_sight = "Moderate Performance"

    summary_tuple = (mean_marks, std_dev, max_marks)
    return summary_tuple, median_marks, correlation, student_data, in_sight

n = 9  # my last 3 digits of roll number are 609
data = generate_data(n)
dataframe = r.DataFrame(data, columns=[
    "Student_ID", "Marks", "Attendance", "Assignment", "Performance_Index"
])
categories = classify_students(data)
summary, median, corr, df, insight = analyze_data(dataframe)
# OUTPUT
print("\n--- Student DataFrame ---")
print(dataframe)
print("\n--- Classification Dictionary ---")
print(categories)
print("\n--- Statistical Summary ---")
print("Mean:", summary[0])
print("Median:", median)
print("Standard Deviation:", summary[1])
print("Max Marks:", summary[2])
print("Correlation (Marks vs Attendance):", corr)
print("\n--- Final System Insight ---")
print(insight)
