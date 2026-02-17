Name="Gowtham Reddy"
x=int(input("Enter the number of resource requests to be added to list:"))
Requests=[0]*x
low_demand=[];low=0
medium_demand=[];medium=0
high_demand=[];high=0
invalid_requests=[]
valid=0
for i in range(x):
    Requests[i]=int(input(f"Enter the score {i+1}:"))
print(Requests,"\n")
print("My Name:",Name,"\n")
for i in Requests:
    if i<0:
        print(i,"is Invalid request.")
        invalid_requests=invalid_requests+[i]
    elif i==0:
        print(i,"has no demand.")
        valid=valid+1
    elif (i>=1) and (i<=20):
        low_demand=low_demand+[i]
        low=low+1
        valid=valid+1
    elif (i>=21) and (i<=50):
        medium_demand=medium_demand+[i]
        valid=valid+1
        medium=medium+1
    else:
        high_demand=high_demand+[i]
        high=high+1
        valid=valid+1
print("Low Demand:",low_demand)
print("Medium Demand:",medium_demand)
print("High Demand:",high_demand)
print("Invalid Demand:",invalid_requests,"\n")
space=Name.count(" ")
if (len(Name)-space)%3==0:
    low_demand=[]
    print("Number of demands removed due to Personalization:",low)
elif (len(Name)-space)%3==1:
    high_demand=[]
    print("Number of demands removed due to Personalization:",high)
else:
    high_demand=[]
    low_demand=[]
    print("Number of demands removed due to Personalization:",low+high)
print("After Personalized Filtering:")
print("Low Demand:",low_demand)
print("Medium Demand:",medium_demand)
print("High Demand:",high_demand)
print("Invalid Demand:",invalid_requests,"\n")
print("Total Valid Entries:",valid)
