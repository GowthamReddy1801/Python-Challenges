
# Digital Payment Risk Detection

## Problem Description
The problem statement is about analysing the transactions and to generate a risk report. This helps in preventing fraud and making the transaction with safer measures in the perspective of bank.

---

## Logic / Approach Used
To solve this problem, I used a list to initially store the transaction amounts of any particular user. Using dictionary consisting of 4 lists I categorized the amounts into their respective lists based on the conditions mentioned in the question using list comprehension method. List comprehension method helps a lot here instead of writing conditional statements. I found valid transactions, sum of those transactions and using some given conditions I have applied my personalization to categorize into low risk or moderate risk or high risk. 

---

## Personalization Applied
I used the following conditions in my personalization to judge the risk in the transactions:
1.	If the number of valid transactions are less than or equal to three I considered it as low risk.
2.	If sum of transaction amounts is greater than 2500 or number of amounts in the high risk amounts is greater than 3 and number of valid transaction amounts are 4 then I assigned it as moderate risk.
3.	For high risk to be achieved frequency>4 and  sum of those transactions now should be greater than 3000, then I assigned it as high risk.
For summary irrespective of what risk is present I just mentioned whether a user have a risk or not upon his transactions. 


---

## Test Case 1
[-5, 1200, 1300, 50, 18]
Invalid Amounts: [-5]
Normal Amounts: [50, 18]
Large Amounts: [1200, 1300]
High Risk Amounts: []
The sum of all transaction amounts: $ 2568
The number of transactions: 5
The number of valid transactions: 4
The user is under moderate risk.
The final summary about the transaction details (total transactions, valid transactions, sum of transactions, risk)
(5, 4, 2568, True)


---

## Test Case 2
Input:
[300, -80, 450, 600, 1250, 1340]
Invalid Amounts: [-80]
Normal Amounts: [300, 450]
Large Amounts: [600, 1250, 1340]
High Risk Amounts: []
The sum of all transaction amounts:$ 3940
The number of transactions: 6
The number of valid transactions: 5
The user is under high risk.
The final summary about the transaction details (total transactions, valid transactions, sum of transactions, risk)
(6, 5, 3940, True)

---

## How to run the code
1. Install Python on your system.
2. Save the program as .py file.
3. Open terminal or command prompt.
4. Go to the folder where the file is saved.
5. Run the command:python file_name.py
6. Enter the transaction values when asked.
7. The program will display the categorized transactions and risk level.
