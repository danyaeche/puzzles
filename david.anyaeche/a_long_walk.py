import sys
from collections import deque

def longest_hike(grid):
    rows, cols = len(grid), len(grid[0])
    start, target = find_start_and_target(grid)
    
    # Define valid movements (up, down, left, right)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Helper function to check if a move is valid
    def is_valid_move(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == '.' and not visited[x][y]

    # Helper function to find the neighbors of a node
    def get_neighbors(x, y, visited):
        neighbors = []
        for move in moves:
            nx, ny = x + move[0], y + move[1]
            if is_valid_move(nx, ny, visited):
                neighbors.append((nx, ny))
        return neighbors

    # BFS to find the longest hike
    max_steps = 0
    queue = deque([(start, 1, {(start[0], start[1])})])  # Queue stores (current node, steps, visited nodes)
    
    while queue:
        current, steps, visited_nodes = queue.popleft()
        max_steps = max(max_steps, steps)
        
        for neighbor in get_neighbors(current[0], current[1], visited_nodes):
            nx, ny = neighbor
            if neighbor not in visited_nodes:
                new_visited = visited_nodes.copy()
                new_visited.add(neighbor)
                queue.append(((nx, ny), steps + 1, new_visited))
    
    return max_steps

def find_start_and_target(grid):
    start = None
    target = None  # Initialize target variable
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            start = (0, i)
            break  # Found 'S', no need to continue the loop
            
    if start is None:
        raise ValueError("Start position not found in the grid.")

    for i in range(len(grid[0])):
        if grid[-1][i] == '.':
            target = (len(grid) - 1, i)
            break  # Found target, no need to continue the loop

    print("\n".join(grid))  # Print the grid for debugging purposes
    
    if target is None:
        raise ValueError("Target position not found in the grid.")
    
    return start, target

if __name__ == "__main__":
    # Take the grid as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py 'grid_input'")
        sys.exit(1)

    grid_input = sys.argv[1]
    grid_lines = grid_input.strip().split('\n')
    
    result = longest_hike(grid_lines)
    print("The longest hike is {} steps.".format(result))
