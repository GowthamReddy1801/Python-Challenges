#                           ****Student Performance Analyser****
n=int(input("Enter the number of students marks to be entered:"))
student_marks=[0.0]*n
register_number=609
name="Gowtham_Reddy"
valid_students=0;failed_students=0
for i in range(n):
    student_marks[i]=float(input(f"Enter the marks of student {i+1}:")) + register_number%len(name)
    if (student_marks[i]>=90.0) and (student_marks[i]<=100.0):
        print(f"Student {i+1} --> Excellent grade")
    elif (student_marks[i]>=75.0) and (student_marks[i]<=89.0):
        print(f"Student {i+1} --> Very Good grade")
    elif (student_marks[i]>=60.0) and (student_marks[i]<=74.0):
        print(f"Student {i+1} --> Good grade")
    elif (student_marks[i]>=40.0) and (student_marks[i]<=59.0):
        print(f"Student {i+1} --> Average grade")
    elif (student_marks[i]>=0.0) and (student_marks[i]<=39.0):
        print(f"Student {i+1} --> Failed")
        failed_students += 1
    else:
        print(f"Student {i+1} --> Invalid marks")
    if (student_marks[i]>=0.0) and (student_marks[i]<=100.0):
        valid_students+=1
print("Total Summary:")
print("The number of valid students are:",valid_students)
print("The number of failed students are:",failed_students)