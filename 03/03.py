# --- Day 3: Rucksack Reorganization ---

from string import ascii_letters

#Loads in input-file and iterates through it
with open('input.txt') as f:
    data = [i for i in f.read().strip().split("\n")]

# --- Part One ---

#Looping trough the data and finding the unique character that exists in both sets
totalSum = 0
for rucksack in data:
    half = len(rucksack)//2

    left = set(rucksack[:half])
    right = set(rucksack[half:])

    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            totalSum += priority + 1

# --- Part Two ---

jump = 3
totalSum = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:jump]
    jump += 3

    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            totalSum += priority +1

print(totalSum)