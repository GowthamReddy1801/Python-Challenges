Multi-Dimensional Academic Intelligence System
Overview

This project analyzes student performance using multiple factors such as marks, attendance, and assignment scores. Instead of using basic lists, it leverages structured data and statistical tools to generate deeper insights into academic performance.

Features
Generates student data using the random module
Stores data using lists, tuples, and dictionaries
Converts data into a Pandas DataFrame for structured analysis
Uses NumPy for numerical computations
Applies math functions for feature engineering
Classifies students into performance categories
Performs statistical analysis including mean, median, standard deviation, and correlation
Implements normalization of marks
Detects patterns such as consistency and attendance risk
Produces a final system insight based on analysis
Data Structure

Each student record contains:

Student_ID
Marks (0–100)
Attendance Percentage (0–100)
Assignment Score (0–50)
Performance Index (custom feature)
Classification Criteria
At Risk: marks < 40 OR attendance < 50
Average: marks between 40 and 70
Good: marks between 71 and 90
Top Performer: marks > 90 AND attendance > 80
Performance Index

The performance index is calculated as:
performance_index = (marks * 0.7 + assignment * 0.3) * log(attendance + 2)

This formula combines academic performance with assignment contribution and adjusts it using attendance through a logarithmic function to avoid extreme scaling.

Analysis Performed
Mean (manually calculated)
Median (NumPy)
Standard Deviation (NumPy)
Maximum Marks
Correlation between marks and attendance
Min-Max Normalization of marks
Pattern Detection
Consistency: standard deviation < 15
Attendance Risk: more than 3 students with attendance < 50
High Achievement: at least 2 top performers
Final Insight

Based on the above conditions, the system outputs:

Excellent Performance
Moderate Performance
Critical Attention Required
Technologies Used
Python
NumPy
Pandas
math module
random module
How to Run
Ensure Python is installed
Install required libraries:
pip install numpy pandas
Run the script:
python filename.py
