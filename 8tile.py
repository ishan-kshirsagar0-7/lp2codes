from queue import PriorityQueue

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def calculate_manhattan_distance(state):
    return sum(abs(i // 3 - (value - 1) // 3) + abs(i % 3 - (value - 1) % 3)
               for i, row in enumerate(state) for value in row if value != 0)

def solve_puzzle(start_state):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start_state))
    
    while not queue.empty():
        _, current_state = queue.get()
        
        if current_state == goal_state:
            return current_state
        
        visited.add(tuple(map(tuple, current_state)))
        empty_row, empty_col = next((i, j) for i in range(3) for j in range(3) if current_state[i][j] == 0)
        
        for move in moves:
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_state = [list(row) for row in current_state]
                new_state[empty_row][empty_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[empty_row][empty_col]
                
                if tuple(map(tuple, new_state)) not in visited:
                    priority = calculate_manhattan_distance(new_state)
                    queue.put((priority, new_state))
                    visited.add(tuple(map(tuple, new_state)))
    
    return None

start_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
solution = solve_puzzle(start_state)

if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found.")