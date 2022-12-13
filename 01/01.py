# --- Day 1: Calorie Counting - --

with open('input.txt') as f:
    lines = f.read().strip().split("\n")

calories = 0
totalCals = []

#Looping trough every "calorie" and resetting the count whenever an empty space in the document occurs
for i in lines:
    if i == '':
        totalCals.append(calories)
        calories = 0
        
#Changing every count in the input document from string to int so that we can summarize them
    else:
        num = int(i)
        calories += num

#Sorting the list and summarize the three highest values 
totalCals.sort()
print(totalCals[-1]+totalCals[-2]+totalCals[-3])