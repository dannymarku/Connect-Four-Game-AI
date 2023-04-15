import numpy as np
import random
import pygame
import sys
import math
from button import Button
import os

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

# difficulty 0 = easy, 1 = normal, 2 = hard
difficultyChoice = 1

# player choice 1 = vs. AI, 2 = vs. friend
playerChoice = 1

count = 0

WINDOW_LENGTH = 4

game_over = True
turn = 1

def options():

    # switch to handle how the buttons initialize in options
    global playerChoice, difficultyChoice
    match playerChoice:
        case 1:
            player_toggle = Button(image=pygame.image.load("assets/Long Rect.png"), pos=(350, 250),
                            text_input="PLAYERS:1", font=myfont, base_color="White", hovering_color="#d7fcd4")

        case 2:
            player_toggle = Button(image=pygame.image.load("assets/Long Rect.png"), pos=(350, 250),
                          text_input="PLAYERS:2", font=myfont, base_color="White", hovering_color="#d7fcd4")

    match difficultyChoice:
        case 0:
            difficulty_toggle = Button(image=pygame.image.load("assets/Long Rect.png"), pos=(10, 1000),
                               text_input="BOT:EASY", font=myfont, base_color="White", hovering_color="#d7fcd4")
        case 1:
            difficulty_toggle = Button(image=pygame.image.load("assets/Long Rect.png"), pos=(10, 1000),
                                text_input="BOT:NORMAL", font=myfont, base_color="White",hovering_color="#d7fcd4")

        case 2:
            difficulty_toggle = Button(image=pygame.image.load("assets/Long Rect.png"), pos=(10, 1000),
                                       text_input="BOT:HARD", font=myfont, base_color="White",
                                       hovering_color="#d7fcd4")

    return_button = Button(image=pygame.image.load("assets/Short Rect.png"), pos=(350, 550),
                           text_input="RETURN", font=myfont, base_color="White", hovering_color="#d7fcd4")

    while True:
        screen.fill("black")

        # screen.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = myfont.render("Options", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(350, 100))

        screen.blit(menu_text, menu_rect)

        for button in [player_toggle, difficulty_toggle, return_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                # if handles player count button
                if player_toggle.checkForInput(menu_mouse_pos):

                    if (player_toggle.text_input == "PLAYERS:1"):
                        player_toggle.text_input = "PLAYERS:2"
                        playerChoice = 2

                        player_toggle.update(screen)

                    else:
                        player_toggle.text_input = "PLAYERS:1"
                        playerChoice = 1

                        player_toggle.update(screen)

                # elif handles player difficulty button
                elif difficulty_toggle.checkForInput(menu_mouse_pos):
                    if (difficulty_toggle.text_input == "BOT:NORMAL"):
                        difficulty_toggle.text_input = "BOT:HARD"
                        difficultyChoice = 2

                        difficulty_toggle.update(screen)


                    elif (difficulty_toggle.text_input == "BOT:HARD"):
                        difficulty_toggle.text_input = "BOT:EASY"
                        difficultyChoice = 0

                        difficulty_toggle.update(screen)

                    elif (difficulty_toggle.text_input == "BOT:EASY"):
                        difficulty_toggle.text_input = "BOT:NORMAL"
                        difficultyChoice = 1

                        difficulty_toggle.update(screen)

                        print("changed position")

                # else return to main menu
                elif return_button.checkForInput(menu_mouse_pos):
                    main_menu()


        if (player_toggle.text_input == "PLAYERS:1"):
            difficulty_toggle.rect = difficulty_toggle.image.get_rect(center=(350, 400))
            difficulty_toggle.text_rect = difficulty_toggle.text.get_rect(center=(350, 400))
        else:
            difficulty_toggle.rect = difficulty_toggle.image.get_rect(center=(350, 1000))
            difficulty_toggle.text_rect = difficulty_toggle.text.get_rect(center=(350, 1000))

            print("changed position")
        pygame.display.update()


def launch_game():
    global playerChoice, difficultyChoice

    if playerChoice == 1:
        if difficultyChoice == 0:
            print("launching easy")
            os.system('python easy_mode.py')
            # launch easy
        elif difficultyChoice == 1:
            print("launching normal")
            os.system('python normal_mode.py')
            # launch normal
        else:
            print("launching hard")
            os.system('python hard_mode.py')
            # launch hard
    elif playerChoice == 2:
        print("launching 2-player")
        os.system('python twop_mode.py')
        # launch 2-player




def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board

def print_board(board):
    print(np.flip(board, 0))

def load_music():
    pygame.mixer.music.load("assets/A Lonely Cherry Tree.wav")
    pygame.mixer.music.play(-1)
    print("music started playing...")

def main_menu():
    while True:
        pygame.display.set_caption("Menu")
        screen.fill("black")

        # screen.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()
        menu_text = myfont.render("Connect Four", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(350, 100))

        play_button = Button(image=pygame.image.load("assets/Mid Rect.png"), pos=(350, 250),
                             text_input="PLAY", font=myfont, base_color="White", hovering_color="#d7fcd4")

        options_button = Button(image=pygame.image.load("assets/Long Rect.png"), pos=(350, 400),
                                text_input="OPTIONS", font=myfont, base_color="White", hovering_color="#d7fcd4")

        quit_button = Button(image=pygame.image.load("assets/Short Rect.png"), pos=(350, 550),
                             text_input="QUIT", font=myfont, base_color="White", hovering_color="#d7fcd4")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    print("clicked on play button")
                    launch_game()
                elif options_button.checkForInput(menu_mouse_pos):
                    options()
                elif quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


board = create_board()
print_board(board)

pygame.init()

myfont = pygame.font.Font("assets/font.ttf", 50)
BG = pygame.image.load("assets/Background.png")

SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
RADIUS = int(SQUARESIZE / 2 - 5)

size = (width, height)
screen = pygame.display.set_mode(size)

load_music()
main_menu()

