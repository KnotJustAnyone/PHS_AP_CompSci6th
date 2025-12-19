import io
import sys

def print_maze(maze):
    for row in maze:
        print("".join(row))

def test_print_maze():
    maze = [
        ["#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#"],
        ["#", " ", "#", "E", "#"],
        ["#", "P", "#", "#", "#"]
    ]

    captured = io.StringIO()
    sys.stdout = captured

    print_maze(maze)

    sys.stdout = sys.__stdout__

    expected = (
        "#####\n"
        "#   #\n"
        "# # #\n"
        "# #E#\n"
        "#P###\n"
    )

    assert captured.getvalue() == expected
