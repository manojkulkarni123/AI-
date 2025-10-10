
import random

# Environment setup: D = Dirty, C = Clean
environment = [
    ['D', 'C'],
    ['C', 'D']
]

# Agent position (starts randomly)
vacuum_pos = [random.randint(0, 1), random.randint(0, 1)]

def perceive_and_act(i, j):
    print(f"Vacuum at position ({i},{j}) - Status: {environment[i][j]}")
    if environment[i][j] == 'D':
        print("Percept: Dirty -> Action: Clean the cell.")
        environment[i][j] = 'C'
    else:
        print("Percept: Clean -> Action: Move to next cell.")
    print()

print("Initial Environment:")
for row in environment:
    print(row)
print("\nStarting Cleaning Process...\n")

# Agent goes through each cell and acts
for i in range(2):
    for j in range(2):
        perceive_and_act(i, j)

print("Final Environment:")
for row in environment:
    print(row)
