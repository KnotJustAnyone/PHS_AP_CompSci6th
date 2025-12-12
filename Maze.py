import random

def generate_maze(width, height):
    # Create grid full of walls
    maze = [["#" for _ in range(width)] for _ in range(height)]

    # Choose a random starting point (must be odd)
    start_x = random.randrange(1, height, 2)
    start_y = random.randrange(1, width, 2)
    maze[start_x][start_y] = " "
    
    stack = [(start_x, start_y)]

    directions = [(2,0), (-2,0), (0,2), (0,-2)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        
        carved = False

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # Stay inside boundaries
            if 1 <= nx < height-1 and 1 <= ny < width-1:
                if maze[nx][ny] == "#":
                    # Carve a path
                    maze[x + dx//2][y + dy//2] = " "
                    maze[nx][ny] = " "
                    stack.append((nx, ny))
                    carved = True
                    break

        if not carved:
            stack.pop()

    # Place Player and Exit
    maze[start_x][start_y] = "P"
    exit_x, exit_y = height-2, width-2
    maze[exit_x][exit_y] = "E"

    return maze, [start_x, start_y]


def maze_game():
    maze, player_pos = generate_maze(15, 15)  # ← generate NEW maze every run

    def print_maze():
        for row in maze:
            print("".join(row))

    def move(dx, dy):
        x, y = player_pos
        new_x = x + dx
        new_y = y + dy

        if maze[new_x][new_y] == "#":
            print("You hit a wall!")
        elif maze[new_x][new_y] == "E":
            print("You won!")
            return True
        else:
            maze[x][y] = " "
            maze[new_x][new_y] = "P"
            player_pos[0], player_pos[1] = new_x, new_y
        return False

    print("Controls: W = up, S = down, A = left, D = right")
    print_maze()

    while True:
        move_input = input("Move: ").lower()
        if move_input == "w":
            if move(-1, 0): break
        elif move_input == "s":
            if move(1, 0): break
        elif move_input == "a":
            if move(0, -1): break
        elif move_input == "d":
            if move(0, 1): break
        else:
            print("Invalid command.")
        print_maze()

maze_game()
