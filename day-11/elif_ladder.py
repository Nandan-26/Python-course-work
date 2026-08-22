'''
3. if-elif-else Statement Programs 
Q1. Weekend Planner Based on Budget 
Write a Python program to suggest a weekend plan based on the user's budget. 
Conditions: 
● Budget > 10000 → Trip 
● Budget > 5000 → Resort Stay 
● Budget > 3000 → Movie and Dinner 
● Budget > 1000 → Cafe and Shopping 
● Budget > 500 → Street Food and Park Visit 
● Otherwise → Stay Home  
Test Case 1 
Input: 
12000 
Output: 
Plan: Trip 
Test Case 2 
Input: 
5000 
Output: 
Plan: Movie and Dinner 
Test Case 3 
Input: 
1000 
Output: 
Plan: Stay Home '''

budget=int(input(" Enter the budget: "))
if budget>10000:
    print("Trip")
elif budget>5000:
    print("Resort stay")
elif budget>3000:
    print("Movie and Dinner")
elif budget>1000:
    print("Cafe and Shopping")
elif budget>500:
    print("Street Food and Park Visit")
else:
    print("Stay Home")                
