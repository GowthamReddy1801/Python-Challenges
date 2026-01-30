print("**********Credential Validator***********")
Student_ID=input("Enter the ID of the student:")
Email_ID=input("Enter the email id:")
Password=input("Enter the password:")
Referral_code=input("Enter the referral code:")
a=0
b=0
c=0
d=0
# If the conditions are true assign a=1.
if Student_ID[0:3]=="CSE" and Student_ID[3]=='-' and Student_ID[4:7].isdigit():
    a=1
# If the conditions are true assign b=1.
if '@'in Email_ID and '.'in Email_ID and Email_ID[0]!='@' and Email_ID[len(Email_ID)-1]!='@' and Email_ID[-4:]=='.edu':
    b=1
# If the conditions are true assign c=1.
if len(Password)>=8 and 'A'<=Password[0]<='Z' and ('0'in Password or '1'in Password or '2'in Password or '3'in Password or '4'in Password or '5'in Password or '6'in Password or '7'in Password or '8'in Password or '9'in Password):
    c=1
# If the conditions are true assign d=1.
if Referral_code[0:3]=="REF" and '0'<=Referral_code[3:5]<='9' and Referral_code[5]=='@':
    d=1
if a==1 and b==1 and c==1 and d==1:
    print("APPROVED")
else :
    print("REJECTED")