**Scenario**
During a disaster drill, emergency teams report the number of
resources requested by different zones. However, reports may contain:
1. Invalid values
2. Unrealistic requests
3. Duplicate demands
4. Critical shortages

**Problem Statement**
Write a Python program that:
1. Accepts a list of integers representing resource requests
2. Uses a for loop to process each request
3. Categorizes requests
4. Applies personalized filtering using PLI
5. Produces a final dispatch report


**Base Classification Rules**
For each request value:
1. <0 → Invalid Request
2. 0 → No Demand
3. 1–20 → Low Demand
4. 21–50 → Moderate Demand
5. 50 → High Demand

**Logic / Approach Used**
Firstly, I have taken the string variable and assigned it with my name. I have taken a list (Requests) to initially get the demand requests from the user. Initialized four empty lists namely low_demand, medium_demand, high_demand and invalid_requests. I have initialized four integer variables to zero namely low, medium, high and valid. Using a for loop I have concatenated the scores to their respective lists using the given conditions. Coming to the personalized logic, I have used conditional statements to deal with that. It depends on the remainder I get when the length of my name (excluding spaces) is divided by 3., I removed the elements from low_demand if the remainder is zero, I removed the elements from high_demand if the remainder is one. Otherwise, I have removed elements from both low_demand and high_demand lists. Finally, I displayed the number of valid, invalid demands and number of demands deleted due to personalization prior to printing the lists after getting personalized.
**Personalization Applied (Mandatory)**
Personalization completely depends on the remainder I get when the length of my name (excluding spaces) is divided by 3. To exclude spaces from length of my name count number of spaces using count () function and assign the value to a variable.
The core logic is: if (len(Name)-spaces)%3==0, then empty low_demand. if (len(Name)-spaces)%3==1, the empty high_demand. if (len(Name)-spaces)%3==2, then empty both low_demand and high_demand.
Example:
•	My Name is: “Gowtham Reddy”
•	Hence, I applied above mentioned logic.
**Sample output:**
Enter the number of resource requests to be added to list:7
Enter the score 1:10
Enter the score 2:25
Enter the score 3:60
Enter the score 4:-3
Enter the score 5:0
Enter the score 6:45
Enter the score 7:80
[10, 25, 60, -3, 0, 45, 80] 

My Name: Gowtham Reddy 

-3 is Invalid request.
0 has no demand.
Low Demand: [10]
Medium Demand: [25, 45]
High Demand: [60, 80]
Invalid Demand: [-3] 

Number of demands removed due to Personalization: 1
After Personalized Filtering:
Low Demand: []
Medium Demand: [25, 45]
High Demand: [60, 80]
Invalid Demand: [-3] 

Total Valid Entries: 6

