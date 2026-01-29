# User-Profile-Validation-System
**Algorithm / Steps**
1. Start 
2. Take four variables namely Full_Name, Email_ID, Mobile_Number, Age of datatypes 
string, string, string, integer respectively and take inputs from the user using input 
function. 
3. Consider four variables a,b,c,d of integer datatype and initialize them with zero. 
4. Use if conditional statement to write the logic for each of the Full_Name, Email_ID, 
Mobile_Number, Age. If the conditions give true then update the values of each a,b,c,d to 
One. 
5. Now using if-else conditional statement: if all of the a,b,c,d are equal to one print the user 
is valid else print the user is invalid. 
6. End
**Approach / Logic Used**
Coming to the logic of each: 
**1. Full Name:**
It is given there should be two words, so there must be a space. So Full_Name.count(“ 
“)>=1 and it is also given space must not be at starting and ending. So Full_Name[0]!=“ “ 
and Full_name[len(Full_Name)-1]!= “ “. 
**2. Email ID:**
It is given ‘@’ and ‘.’ Must me present in Email_ID. So ‘@’ in Email_ID and ‘.’ In 
Email_ID is the logic here. It is also given first character should not be ‘@’. So 
Email_ID[0]!= ‘@’. 
**3. Mobile Number:**
A mobile number must contain 10 characters and each character should be a digit 
between 0-9. So len(Mobile_Number)==10 and Mobile_Number.isdigit() conditions 
must be true. isdigit() is a inbuilt function in python which gives true if a string contains 
only digits between 0-9. And a mobile number should not start with Zero. So 
Mobile_Number[0]!= ‘0’. 
**4. Age validation:** 
If the Age of the user is between 18-60(inclusive) then it is valid. So Age>=18 and 
Age<=60 is the logic here.
**Sample Outputs:**
<img width="561" height="186" alt="Screenshot 2026-01-29 160247" src="https://github.com/user-attachments/assets/85212037-d3d1-4d90-8464-774dac75e497" />
<img width="554" height="194" alt="Screenshot 2026-01-29 160507" src="https://github.com/user-attachments/assets/fa455978-4696-435f-bb00-2971c092c723" />
