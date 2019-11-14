from Board import Board
from pynput import keyboard
from time import sleep

b = Board()


def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    elif key == keyboard.Key.up:
        b.board, b.empty_locations = b.move_up(b.board, b.empty_locations)
    elif key == keyboard.Key.down:
        b.board, b.empty_locations = b.move_down(b.board, b.empty_locations)
    elif key == keyboard.Key.left:
        b.board, b.empty_locations = b.move_left(b.board, b.empty_locations)
    elif key == keyboard.Key.right:
        b.board, b.empty_locations = b.move_right(b.board, b.empty_locations)
    elif key == keyboard.Key.shift:
        print("It can take some time")
        sleep(1)
        for m in path_to_victory:
            b.moves[m](b.board, b.empty_locations)
            b.refresh()
            sleep(0.8)

    return b.refresh()


def main():
    global path_to_victory
    b.randomize_board()
    b.refresh()
    path_to_victory = b.game_solve()
    print("Steps to win this game, spoilers!!!")
    for num, steps in enumerate(path_to_victory):
        print("The {} step is: {}".format(num + 1, b.repr_moves[steps]))

    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()