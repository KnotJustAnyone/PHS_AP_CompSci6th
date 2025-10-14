def maze_game():
    maze = [
        ["#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#"],
        ["#", " ", "#", "E", "#"],
        ["#", "P", "#", "#", "#"]
    ]

    player_pos = [4, 1]

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

maze_game()
