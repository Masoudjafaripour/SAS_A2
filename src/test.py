import heapq
import math
import matplotlib.pyplot as plt

def octile_distance(node, goal):
    dx, dy = abs(node[0] - goal[0]), abs(node[1] - goal[1])
    D, D2 = 1, math.sqrt(2)
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def get_neighbors(grid, node):
    x, y = node
    neighbors = []
    width, height = len(grid[0]), len(grid)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < height and 0 <= ny < width and grid[nx][ny] == 0:
            # Check for corner cutting
            if abs(dx) + abs(dy) == 2:  # Diagonal move
                if grid[x][ny] == 1 or grid[nx][y] == 1:
                    continue  # Skip diagonal move if it cuts through an obstacle
            neighbors.append((nx, ny))
    return neighbors

def a_star(grid, start, goal):
    open_set = []  # Priority queue
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: octile_distance(start, goal)}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in get_neighbors(grid, current):
            temp_g_score = g_score[current] + (math.sqrt(2) if abs(current[0] - neighbor[0]) + abs(current[1] - neighbor[1]) == 2 else 1)
            
            if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + octile_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No path found

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]

def visualize_grid(grid, path, start, goal):
    fig, ax = plt.subplots(figsize=(6, 6))
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                ax.add_patch(plt.Rectangle((y, len(grid) - x - 1), 1, 1, color='black'))
    
    for (x, y) in path:
        ax.add_patch(plt.Rectangle((y, len(grid) - x - 1), 1, 1, color='blue', alpha=0.5))
    
    ax.add_patch(plt.Rectangle((start[1], len(grid) - start[0] - 1), 1, 1, color='green', label='Start'))
    ax.add_patch(plt.Rectangle((goal[1], len(grid) - goal[0] - 1), 1, 1, color='red', label='Goal'))
    
    plt.xlim(0, len(grid[0]))
    plt.ylim(0, len(grid))
    plt.xticks([])
    plt.yticks([])
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.show()

# Example grid and execution
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

start, goal = (0, 0), (5, 6)
path = a_star(grid, start, goal)

if path:
    visualize_grid(grid, path, start, goal)
    print("Optimal Path:", path)
else:
    print("No path found")
