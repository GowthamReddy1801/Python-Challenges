#                           SMART TRANSACTION RISK DETECTOR
amounts=[]
n=int(input("Enter the number of transactions:"))
for i in range(n):
    x=int(input(f"Enter the amount {i+1}:"))
    amounts.append(x)
transactions={
    "Invalid_amounts":[i for i in amounts if i<=0],
    "Normal_amounts":[i for i in amounts if (i>0) and (i<=500)],
    "Large_amounts":[i for i in amounts if (i>500) and (i<=2000)],
    "High_risk_amounts":[i for i in amounts if (i>2000)]
}
valid_amounts=[i for i in amounts if i>0]
frequency=len(valid_amounts)
amount_sum=0
for i in range(len(valid_amounts)):
    amount_sum=amount_sum+valid_amounts[i]
suspicious=len(transactions["High_risk_amounts"])>=3
low_risk=frequency<=3
moderate_risk=(amount_sum>2500 or suspicious)and((frequency>3)and(frequency<=4))
high_risk=frequency>4 and amount_sum>3000
print("The list of transaction amounts:")
print(amounts)
print("Invalid Amounts:",transactions["Invalid_amounts"])
print("Normal Amounts:",transactions["Normal_amounts"])
print("Large Amounts:",transactions["Large_amounts"])
print("High Risk Amounts:",transactions["High_risk_amounts"])
print("The sum of all transaction amounts:$",amount_sum)
print("The number of transactions:",len(amounts))
print("The number of valid transactions:",frequency)
risk=False
if low_risk:
    print("The user is under low risk.")
    risk=True
elif moderate_risk:
    print("The user is under moderate risk.")
    risk=True
elif high_risk:
    print("The user is under high risk.")
    risk=True
summary=(len(amounts),frequency,amount_sum,risk)
print("The final summary about the transaction details(total transactions,valid transactions,sum of transactions,risk)")
print(summary)
