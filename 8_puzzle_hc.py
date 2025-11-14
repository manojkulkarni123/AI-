import random

# ---------- STEP 1: Define Start and Goal ----------
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

print("START STATE:")
for row in start_state:
    print(row)
print("\nGOAL STATE:")
for row in goal_state:
    print(row)
print("\n--------------------------------\n")

# ---------- STEP 2: Heuristic Function (Manhattan Distance) ----------
def heuristic(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == value:
                            distance += abs(x - i) + abs(y - j)
    return distance

# ---------- STEP 3: Helper Functions ----------
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# ---------- STEP 4: Hill Climbing Algorithm ----------
def hill_climbing(start, goal):
    current = start
    current_h = heuristic(current, goal)
    steps = [current]

    while True:
        neighbors = get_neighbors(current)
        next_state = None
        next_h = float('inf')

        # Choose the neighbor with lowest heuristic value
        for neighbor in neighbors:
            h = heuristic(neighbor, goal)
            if h < next_h:
                next_state = neighbor
                next_h = h

        print("Current State (h =", current_h, "):")
        for row in current:
            print(row)
        print()

        # Stop if no better neighbor
        if next_h >= current_h:
            print("Reached local minimum or goal.\n")
            break

        current = next_state
        current_h = next_h
        steps.append(current)

        if current == goal:
            print("Goal reached!\n")
            break

    return steps

# ---------- STEP 5: Run Hill Climbing ----------
solution = hill_climbing(start_state, goal_state)

# ---------- STEP 6: Display Steps ----------
print("STEPS TO REACH (OR CLOSE TO) GOAL:\n")
for step in solution:
    for row in step:
        print(row)
    print()

print("Total Steps Taken:", len(solution)-1)

"""
START STATE:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

GOAL STATE:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

--------------------------------

Current State (h = 2 ):
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Current State (h = 1 ):
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Goal reached!

STEPS TO REACH (OR CLOSE TO) GOAL:

[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

Total Steps Taken: 2
"""
