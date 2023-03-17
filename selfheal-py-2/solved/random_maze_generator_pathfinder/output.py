import random
import heapq

def generate_maze(n):
    maze = [['#' for _ in range(n)] for _ in range(n)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n

    def carve(x, y):
        if not is_valid(x, y) or maze[y][x] == ' ':
            return

        maze[y][x] = ' '
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if is_valid(nx, ny) and maze[ny][nx] == '#':
                maze[y + dy][x + dx] = ' '
                carve(nx, ny)

    carve(1, 1)
    maze[1][0] = 'S'
    maze[n - 2][n - 1] = 'E'
    return maze

def a_star_search(maze, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def neighbors(pos):
        x, y = pos
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[ny][nx] != '#':
                yield (nx, ny)

    g = {start: 0}
    h = {start: heuristic(start, end)}
    f = {start: h[start]}
    open_set = [(f[start], start)]
    came_from = {}

    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in neighbors(current):
            tentative_g = g[current] + 1
            if neighbor not in g or tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                h[neighbor] = heuristic(neighbor, end)
                f[neighbor] = g[neighbor] + h[neighbor]
                heapq.heappush(open_set, (f[neighbor], neighbor))

    return []

def main():
    n = int(input("Enter the size of the maze (n x n): "))
    maze = generate_maze(n)
    for row in maze:
        print(''.join(row))

    start = None
    end = None
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)

    path = a_star_search(maze, start, end)
    for pos in path[1:-1]:
        x, y = pos
        maze[y][x] = '*'

    print("Shortest path:")
    for row in maze:
        print(''.join(row))

if __name__ == "__main__":
    main()