# --- Day 2: Rock Paper Scissors ---

#Loads in input-file and iterates through it
with open('input.txt') as f:
    rounds = [i for i in f.read().strip().split("\n")]

# --- Part One ---
#Possible outcomes

# A vs X = DRAW = 1 + 3 = 4
# A vs Y = WIN  = 2 + 6 = 8
# A vs Z = LOSS = 3 + 0 = 3
# B vs X = LOSS = 1 + 0 = 1
# B vs Y = DRAW = 2 + 3 = 5
# B vs Z = WIN  = 3 + 6 = 9
# C vs X = WIN  = 1 + 6 = 7
# C vs Y = LOSS = 2 + 0 = 2
# C vs Z = DRAW = 3 + 3 = 6

# Dictionary over the possible outcomes from matches of Rock, Paper, Scissors
results = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

# Iterates through the Rock, Paper, Scissors dictionary with the help of the input file
# and print the results
totalScore = 0
for round in rounds:
    totalScore += results[round]

print(totalScore)

# --- Part Two ---

# In the second part the ruleset is changed as seen below
# Therefore we change the scoreset of the dictionary and run it through the same way as above
# In the end we display the results

# X = LOSS
# Y = DRAW
# Z = WIN

manipulatedResults = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}

manipulatedTotalScore = 0
for round in rounds:
    manipulatedTotalScore += manipulatedResults[round]

print(manipulatedTotalScore)
