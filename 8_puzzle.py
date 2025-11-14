import heapq

# ---------- STEP 1: Define Start and Goal States ----------
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

# ---------- STEP 2: Manhattan Distance Heuristic ----------
def manhattan_distance(state, goal):
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

def to_tuple(state):
    return tuple(sum(state, []))

# ---------- STEP 4: A* Search Algorithm ----------
def a_star(start, goal):
    pq = []
    heapq.heappush(pq, (manhattan_distance(start, goal), 0, start, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)
        if to_tuple(current) in visited:
            continue
        visited.add(to_tuple(current))

        print(f"Step {len(path)+1}:")
        for row in current:
            print(row)
        print()

        if current == goal:
            print("Goal reached!\n")
            return path + [current]

        for neighbor in get_neighbors(current):
            new_cost = g + 1
            heapq.heappush(pq, (new_cost + manhattan_distance(neighbor, goal),
                                 new_cost, neighbor, path + [current]))
    return None

# ---------- STEP 5: Run the A* Algorithm ----------
solution = a_star(start_state, goal_state)

# ---------- STEP 6: Display Final Solution ----------
if solution:
    print("STEPS TO REACH THE GOAL:\n")
    for step in solution:
        for row in step:
            print(row)
        print()
    print("Total Steps:", len(solution)-1)
else:

    print("No solution found.")

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

Step 1:
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 2:
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 3:
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

Goal reached!

STEPS TO REACH THE GOAL:

[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

[1, 2, 3]
[4, 5, 6]
[7, 8, 0]

Total Steps: 2


"""
