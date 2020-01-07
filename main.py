import pygame
from board import Board
import sys
import os


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class TRON(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.direction_first = 'right'
        self.direction_second = 'left'
        self.posFirst = [height // 2, 0]
        self.posSecond = [height // 2, width - 1]

    def win_screen(self, win):
        pass

    def restart(self, win):
        self.win_screen(win)
        start_screen()
        self.__init__(self.width, self.height)

    def next_move(self):
        self.board[self.posFirst[0]][self.posFirst[1]] = 1
        self.board[self.posSecond[0]][self.posSecond[1]] = 2
        if self.direction_first == 'up':
            self.posFirst[0] -= 1
        elif self.direction_first == 'down':
            self.posFirst[0] += 1
        elif self.direction_first == 'left':
            self.posFirst[1] -= 1
        elif self.direction_first == 'right':
            self.posFirst[1] += 1
        if self.direction_second == 'up':
            self.posSecond[0] -= 1
        elif self.direction_second == 'down':
            self.posSecond[0] += 1
        elif self.direction_second == 'left':
            self.posSecond[1] -= 1
        elif self.direction_second == 'right':
            self.posSecond[1] += 1
        self.posSecond[0] %= 33
        self.posSecond[1] %= 33
        self.posFirst[0] %= 33
        self.posFirst[1] %= 33
        if self.posFirst == self.posSecond or \
                (self.board[self.posFirst[0]][self.posFirst[1]] != 0
                 and self.board[self.posSecond[0]][self.posSecond[1]] != 0):
            print("Ничья")
            self.restart(0)
        if self.board[self.posFirst[0]][self.posFirst[1]] != 0:
            print("Первый проиграл")
            self.restart(2)
        if self.board[self.posSecond[0]][self.posSecond[1]] != 0:
            print("Второй проиграл")
            self.restart(1)

    def change_direction(self, player, direction):
        if player == 1:
            if direction == 'up' and self.direction_first != 'down':
                self.direction_first = 'up'
            elif direction == 'down' and self.direction_first != 'up':
                self.direction_first = 'down'
            elif direction == 'right' and self.direction_first != 'left':
                self.direction_first = 'right'
            elif direction == 'left' and self.direction_first != 'right':
                self.direction_first = 'left'
        elif player == 2:
            if direction == 'up' and self.direction_second != 'down':
                self.direction_second = 'up'
            elif direction == 'down' and self.direction_second != 'up':
                self.direction_second = 'down'
            elif direction == 'right' and self.direction_second != 'left':
                self.direction_second = 'right'
            elif direction == 'left' and self.direction_second != 'right':
                self.direction_second = 'left'

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size, self.cell_size
                )
                if row == self.posFirst[0] and col == self.posFirst[1]:
                    color = pygame.Color('dark cyan')
                    pygame.draw.rect(screen, color, rect)

                if row == self.posSecond[0] and col == self.posSecond[1]:
                    color = pygame.Color('red')
                    pygame.draw.rect(screen, color, rect)

                if self.board[row][col] == 1:
                    color = pygame.Color('cyan')
                    pygame.draw.rect(screen, color, rect)

                if self.board[row][col] == 2:
                    color = pygame.Color('dark orange')
                    pygame.draw.rect(screen, color, rect)
        super().render(screen)


pygame.init()
w, h = 33, 33
clock = pygame.time.Clock()
size = width, height = 40 + w * 20, 40 + h * 20
screen = pygame.display.set_mode(size)
board = TRON(w, h)
FPS_menu = 50
FPS_game = 5
running = True
WIDTH = HEIGHT = h * 20 + 40


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["*основные правила*", "",
                  "Управление голубым гонщиком *картинка_нейм*",
                  "Управление оранжевым гонщиком *картинка_нейм*",
                  "Нажмите любую кнопку чтобы начать игру"]
    screen.fill((0, 0, 0))
    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS_menu)


start_screen()


while running:
    restart_pressed = False
    for event in pygame.event.get():
        restart_pressed = False
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 119:
                board.change_direction(1, 'up')
            elif event.key == 115:
                board.change_direction(1, 'down')
            elif event.key == 100:
                board.change_direction(1, 'right')
            elif event.key == 97:
                board.change_direction(1, 'left')
            elif event.key == 273:
                board.change_direction(2, 'up')
            elif event.key == 274:
                board.change_direction(2, 'down')
            elif event.key == 275:
                board.change_direction(2, 'right')
            elif event.key == 276:
                board.change_direction(2, 'left')
            elif event.key == 114:
                restart_pressed = True
                board.restart()
    if not restart_pressed:
        board.next_move()
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
    clock.tick(FPS_game)
pygame.quit()
