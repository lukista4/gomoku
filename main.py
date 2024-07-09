import sys
import pygame

pygame.init()

WHITE = (255, 255, 255)
GREY = (180, 180, 180)
RED = (255, 0, 0)
GREEN = (0, 190, 0)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 4
BOARD_ROWS = 15
BOARD_COLS = 15
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GOMOKU")
screen.fill(ORANGE)

board = [[0 for i in range(BOARD_ROWS)] for j in range(BOARD_COLS)]

def draw_lines(color=BLACK):
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, color, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, color, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, WHITE, (int(col*SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS)
                pygame.draw.circle(screen, BLACK, (int(col*SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, BLACK, (int(col*SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS)

def mark_square(row, col, player):
    board[row][col] = player
    return (row, col)

def available_square(row, col):
    return board[row][col] == 0
def is_board_full(check_board = board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if check_board[row][col] == 0:
                return False
    return True


def five_in_a_row(structure, player):
    comp = [player]*5
    for i in range(len(structure) - 4):
        test = list(structure[i:i+5])
        if test == comp:
            return True
    return False



def check_win(player, last_move, check_board=board):
    Y = last_move[0]
    X = last_move[1]
    left = max(0, X - 4)
    right = min(BOARD_COLS, X + 5)
    up = max(0, Y - 4)
    down = min(BOARD_ROWS, Y + 5)

    horizontal = check_board[Y][left:right]
    vertical = [check_board[i][X] for i in range(up, down)]
    start_UL = min(Y-up, X-left)
    end_DR = min(down-Y,right-X)
    UL_DR = [check_board[Y-start_UL+i][X-start_UL+i] for i in range(start_UL+end_DR)]
    start_DL = min(down-Y-1, X-left)
    end_UR = min(Y-up,right-X-1)
    DL_UR = [check_board[Y+start_DL-i][X-start_DL+i] for i in range(start_DL+end_UR+1)]
    
    return five_in_a_row(horizontal,player) or five_in_a_row(vertical,player) or five_in_a_row(UL_DR,player) or five_in_a_row(DL_UR,player)


def restart_game():
    screen.fill(ORANGE)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

draw_lines()

player = 1
winner = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if available_square(mouseY, mouseX):
                square = mark_square(mouseY, mouseX, player)
                if check_win(player, square):
                    game_over = True
                    winner = player
                player = player % 2 + 1

                if not game_over:
                    if is_board_full():
                        game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False
                player = 1

    if not game_over:
        draw_figures()
    else:
        draw_figures()
        if winner == 1:
            draw_lines(GREEN)

        elif winner == 2:
            draw_lines(RED)
        else:
            draw_lines(GREY)

    pygame.display.update()