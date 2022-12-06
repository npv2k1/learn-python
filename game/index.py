import os
from tabulate import tabulate

from pynput import keyboard

board = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, '']]
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '':
                return (i, j)
    return None

def check_outline(board, i, j):
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return True
    return False

def handle_keyboard(key):
    x,y = find_empty(board)
    if key == 'w':
        return (x-1,y)
    elif key == 's':
        return (x+1,y)
    elif key == 'a':
        return (x,y-1)
    elif key == 'd':
        return (x,y+1)
    else:
        return None


def clear(): return os.system('cls')

print(tabulate(board, tablefmt="grid"))

def on_press(key):
    try:
        key = key.char
        if key == 'w' or key == 's' or key == 'a' or key == 'd':
            clear()
            print(tabulate(board, tablefmt="grid"))
            new_pos = handle_keyboard(key)
            if new_pos is None:
                print("Invalid move")
                return
            if check_outline(board, new_pos[0], new_pos[1]):
                print("Invalid move")
                return
            x, y = find_empty(board)
            board[x][y] = board[new_pos[0]][new_pos[1]]
            board[new_pos[0]][new_pos[1]] = ''
        else:
            clear()
            print(tabulate(board, tablefmt="grid"))
    except AttributeError:
        pass
        # print('special key pressed: {0}'.format(
        #     key))


def on_release(key):
    # print('Key released: {0}'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


   
    


