
def IDDFS(start_state, goal_state):
   
    for depth in range(0, 100): 
        print(f"Exploring depth: {depth}")
        result = DLS(start_state, goal_state, depth)
        if result != "FAILURE":
            return result, depth  
    return "FAILURE", None  


def DLS(state, goal_state, depth_limit):
    if state == goal_state:
        return state  

    if depth_limit == 0:
        return "FAILURE"  

    for neighbor in Expand(state):
        result = DLS(neighbor, goal_state, depth_limit - 1)
        if result != "FAILURE":
            return result  

    return "FAILURE"  


def Expand(state):
    neighbors = []
    blank_pos = FindBlank(state)  
    
    for direction in ['up', 'down', 'left', 'right']:
        new_state = MoveBlank(state, blank_pos, direction)
        if new_state:
            neighbors.append(new_state) 
    return neighbors


    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                return (i, j)  
    return None


def MoveBlank(state, blank_pos, direction):
    row, col = blank_pos
    new_state = [row[:] for row in state]  
    if direction == 'up' and row > 0:  
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
        return new_state
    elif direction == 'down' and row < 2:  
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
        return new_state
    elif direction == 'left' and col > 0:  
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
        return new_state
    elif direction == 'right' and col < 2: 
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
        return new_state

    return None  


def PrintState(state):
    for row in state:
        print(" ".join([str(x) if x != '_' else ' ' for x in row]))
    print()


start_state = [
    [1, 2, 3],
    ['_', 4, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, '_']
]

# Solve the 8-Puzzle using IDDFS
solution, depth_found = IDDFS(start_state, goal_state)

if solution != "FAILURE":
    print("Solution found!")
    PrintState(solution)
    print(f"Solution found at depth: {depth_found}")
else:
    print("No solution found.")
