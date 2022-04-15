"""
-------------------------------
    TIC TAC TOE WITH PYTHON
    -----------------------
      HASIBUL HASAN NIROB
-------------------------------
"""

import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH//BOARD_COLS
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55
RGB = (131, 111, 255)
RGB_2 = (79, 79, 79)
RGB_3 = (244, 244, 244)
RGB_4 = (30, 30, 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(RGB)

# BOARD
board = np.zeros((BOARD_ROWS, BOARD_COLS))


# print(board)


# pygame.draw.line(screen, RGB_2, (10, 10), (300, 300), 10)
def draw_lines():
    # horizontal
    pygame.draw.line(screen, RGB_2, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, RGB_2, (0, 400), (600, 400), LINE_WIDTH)
    # vertical
    pygame.draw.line(screen, RGB_2, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, RGB_2, (400, 0), (400, 600), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, RGB_3, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, RGB_4, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, RGB_4, (col * 200 + SPACE, row * 200 + SPACE),
                                 (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE),
                                 CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    # vertical win check
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    # horizontal win check
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True
    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False


def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = RGB_3
    elif player == 2:
        color = RGB_4

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15)


def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100
    if player == 1:
        color = RGB_3
    elif player == 2:
        color = RGB_4

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15)


def draw_asc_diagonal(player):
    if player == 1:
        color = RGB_3
    elif player == 2:
        color = RGB_4
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


def draw_desc_diagonal(player):
    if player == 1:
        color = RGB_3
    elif player == 2:
        color = RGB_4
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart():
    screen.fill(RGB)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


# false
# print(is_board_full())
# marking all squares
# for row in range(BOARD_ROWS):
#     for col in range(BOARD_COLS):
#         mark_square(row, col, 1)
# board is full
# print(is_board_full())
# print(available_square(1, 1))
# mark_square(0, 0, 1)
# mark_square(1, 1, 2)
# print(board)


draw_lines()
player = 1
game_over = False
# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]
            mouseY = event.pos[1]
            # print(mouseX)
            # print(mouseY)
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            # print(clicked_row)
            # print(clicked_col)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
                # print(board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
