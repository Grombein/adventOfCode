#--- Day 5: Supply Stacks ---

with open('input.txt') as file:
    stackStrings, instructions = [i.splitlines() for i in file.read().strip("\n").split("\n\n")]

stacks = {int(digit):[] for digit in stackStrings[-1].replace(" ", "")}
indexes = [index for index, char in enumerate(stackStrings[-1]) if char != " "]

def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

displayStacks()


def loadStacks():
    for string in stackStrings[:-1]:
        stackNum = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stackNum].insert(0, string[index])
            stackNum += 1

loadStacks()
displayStacks()

                