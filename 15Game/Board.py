from copy import deepcopy
from os import system
from queue import Queue
from random import randint, seed

MAX_COL = 3
MAX_RAW = 3
RANDOM_STEPS_NUMBER = 20


class Board:
    def __init__(self):
        self.goal = [['x', 'a', 'm'],
                     ['e', 'l', 'e'],
                     ['o', 'n', '_']]
        self.board = deepcopy(self.goal)

        self.empty_locations = [MAX_RAW - 1, MAX_COL - 1]

        self.moves = {0: self.move_up, 1: self.move_down, 2: self.move_left, 3: self.move_right}
        self.repr_moves = {0: 'move_up ', 1: 'move_down ', 2: 'move_left ', 3: 'move_right '}

    def __repr__(self):
        for i in range(MAX_RAW):
            for j in range(MAX_COL):
                print(self.board[i][j], end=' ')
            print()
        return ""

    def refresh(self):
        system("clear")
        # user friendly text message
        print("Hi, this is game of fifteen! Let's play!")
        self.possible_steps()
        # print updated board
        print(self)

        if self.board == self.goal:
            print("\nThe game is over, you won!")
            return False
        return True

    def randomize_board(self):
        seed()

        for i in range(RANDOM_STEPS_NUMBER):
            m = randint(0, 3)
            self.moves[m](self.board, self.empty_locations)

    def game_solve(self):
        def possible_moves(board, e_loc):
            boards_list = [deepcopy(board), deepcopy(board), deepcopy(board), deepcopy(board)]
            empty_loc_list = [list(e_loc), list(e_loc), list(e_loc), list(e_loc)]

            boards_list[0], empty_loc_list[0] = self.move_up(boards_list[0], empty_loc_list[0])
            boards_list[1], empty_loc_list[1] = self.move_down(boards_list[1], empty_loc_list[1])
            boards_list[2], empty_loc_list[2] = self.move_left(boards_list[2], empty_loc_list[2])
            boards_list[3], empty_loc_list[3] = self.move_right(boards_list[3], empty_loc_list[3])

            # return a possible board view, empty location and value that indicate the move
            # value refers to self.moves dict as a key value
            return [[boards_list[0], empty_loc_list[0], 0], [boards_list[1], empty_loc_list[1], 1],
                    [boards_list[2], empty_loc_list[2], 2], [boards_list[3], empty_loc_list[3], 3]]
        visited = set()
        queue = Queue()

        queue.put({"board": self.board, "e_loc": self.empty_locations, "path": []})

        while True:
            # quit if there is no solution
            if queue.empty():
                return []

            node = queue.get()

            if node["board"] == self.goal:
                return node["path"]

            if str(node["board"]) not in visited:
                visited.add(str(node["board"]))
                for child in possible_moves(node["board"], node["e_loc"]):
                    if str(child[0]) not in visited:
                        queue.put({"board": child[0], "e_loc": child[1], "path": node["path"] + [child[2]]})

    def possible_steps(self):
        print("Well, you have 4 possible steps\n"
              "1.Move down by keyboard key 'down'\n"
              "2.Move up by keyboard key 'up'\n"
              "3.Move right by keyboard key 'right'\n"
              "4.Move left by keyboard key 'left'\n"
              "5.Show the solution visualization by keyword 'shift'\n"
              "6.Exit the game 'esc'\n")

    def move(self, board, empty_locations, raw, col):
        # check if move is correct
        if empty_locations[0] + raw < 0 or empty_locations[0] + raw > 2 \
                                        or empty_locations[1] + col > 2 or empty_locations[1] + col < 0:
            return board, empty_locations

        board[empty_locations[0]][empty_locations[1]], board[empty_locations[0] + raw][empty_locations[1] + col] =\
        board[empty_locations[0] + raw][empty_locations[1] + col], board[empty_locations[0]][empty_locations[1]]

        empty_locations[0] += raw
        empty_locations[1] += col

        return board, empty_locations

    def move_up(self, board, empty_locations):
        return self.move(board, empty_locations, -1, 0)

    def move_down(self, board, empty_locations):
        return self.move(board, empty_locations, 1, 0)

    def move_right(self, board, empty_locations):
        return self.move(board, empty_locations, 0, 1)

    def move_left(self, board, empty_locations):
        return self.move(board, empty_locations, 0, -1
                         )