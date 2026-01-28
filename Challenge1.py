print("*******User Profile Validation System*******")
Full_Name=input("Enter the full name of the user:")
Email_ID=input("Enter the Email ID of the user:")
Mobile_Number=input("Enter the phone number of the user:")
Age=int(input("Enter the age of the user:"))
a=0
b=0
c=0
d=0
# If the conditions satisfy assign a=1.
if Full_Name.count(' ')>=1 and Full_Name[0]!=' 'and Full_Name[len(Full_Name)-1]!=' ':
    a=1
# If the conditions satisfy assign b=1.
if '@'in Email_ID and '.' in Email_ID and Email_ID[0]!='@':
    b=1
# If the conditions satisfy assign c=1.
if len(Mobile_Number)==10 and Mobile_Number.isdigit() and Mobile_Number[0]!='0':
    c=1
# If the conditions satisfy assign d=1.
if Age>=18 and Age<=60:
    d=1
# If all a,b,c,d are equal to one then user profile is valid.
if a==1 and b==1 and c==1 and d==1:
    print("User profile is VALID.")
else:
    print("User Profile is INVALID.")
