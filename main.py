import time
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
        self.blue_image = pygame.transform.scale(load_image('blue.png'), (20, 20))
        self.red_image = pygame.transform.scale(load_image('red.png'), (20, 20))
        self.blue_direction_arr = [self.blue_image,
                                   pygame.transform.rotate(self.blue_image, 180),
                                   pygame.transform.rotate(self.blue_image, 90),
                                   pygame.transform.rotate(self.blue_image, 270)]
        self.red_direction_arr = [self.red_image,
                                  pygame.transform.rotate(self.red_image, 180),
                                  pygame.transform.rotate(self.red_image, 90),
                                  pygame.transform.rotate(self.red_image, 270)]
        self.posFirst = [height // 2, 0]
        self.posSecond = [height // 2, width - 1]
        self.all_sprites = pygame.sprite.Group()

    def win_screen(self, win):
        self.render(screen)
        if win == 2:
            win_text = "Выиграл гонщик с оранжевым цветом"
            winner_color = pygame.Color('orange')
            rect = pygame.Rect(
                self.left + self.posFirst[1] * self.cell_size,
                self.top + self.posFirst[0] * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            for i in range(5):
                if i % 2 == 0:
                    pygame.draw.rect(screen, pygame.Color('white'), rect)
                elif self.direction_first == 'up':
                    screen.blit(self.blue_direction_arr[0], rect)
                elif self.direction_first == 'down':
                    screen.blit(self.blue_direction_arr[1], rect)
                elif self.direction_first == 'right':
                    screen.blit(self.blue_direction_arr[3], rect)
                else:
                    screen.blit(self.blue_direction_arr[2], rect)
                pygame.display.flip()
                time.sleep(1)
        elif win == 1:
            win_text = "Выиграл гонщик с голубым цветом"
            winner_color = pygame.Color('cyan')
            rect = pygame.Rect(
                self.left + self.posSecond[1] * self.cell_size,
                self.top + self.posSecond[0] * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            for i in range(5):
                if i % 2 == 0:
                    pygame.draw.rect(screen, pygame.Color('white'), rect)
                elif self.direction_second == 'up':
                    screen.blit(self.red_direction_arr[0], rect)
                elif self.direction_second == 'down':
                    screen.blit(self.red_direction_arr[1], rect)
                elif self.direction_second == 'right':
                    screen.blit(self.red_direction_arr[3], rect)
                elif self.direction_second == 'left':
                    screen.blit(self.red_direction_arr[2], rect)
                pygame.display.flip()
                time.sleep(1)
        else:
            win_text = "Ничья"
            winner_color = pygame.Color('white')
            rect_second = pygame.Rect(
                self.left + self.posSecond[1] * self.cell_size,
                self.top + self.posSecond[0] * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            rect_first = pygame.Rect(
                self.left + self.posFirst[1] * self.cell_size,
                self.top + self.posFirst[0] * self.cell_size,
                self.cell_size,
                self.cell_size
            )
            for i in range(5):
                if i % 2 == 0:
                    pygame.draw.rect(screen, pygame.Color('white'), rect_first)
                elif self.direction_first == 'up':
                    screen.blit(self.blue_direction_arr[0], rect_first)
                elif self.direction_first == 'down':
                    screen.blit(self.blue_direction_arr[1], rect_first)
                elif self.direction_first == 'right':
                    screen.blit(self.blue_direction_arr[3], rect_first)
                else:
                    screen.blit(self.blue_direction_arr[2], rect_first)
                if i % 2 == 0:
                    pygame.draw.rect(screen, pygame.Color('white'), rect_second)
                elif self.direction_second == 'up':
                    screen.blit(self.red_direction_arr[0], rect_second)
                elif self.direction_second == 'down':
                    screen.blit(self.red_direction_arr[1], rect_second)
                elif self.direction_second == 'right':
                    screen.blit(self.red_direction_arr[3], rect_second)
                else:
                    screen.blit(self.red_direction_arr[2], rect_second)
                pygame.display.flip()
                time.sleep(1)
        screen.fill((0, 0, 0))
        fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text = font.render(win_text, 1, winner_color)
        text_pos = (700 // 2 - text.get_width() // 2, 700 // 2 - text.get_height() // 2 )
        screen.blit(text, text_pos)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    return
            pygame.display.flip()

    def restart(self, win):
        if win != 'restart':
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
            self.restart(0)
        if self.board[self.posFirst[0]][self.posFirst[1]] != 0:
            self.restart(2)
        if self.board[self.posSecond[0]][self.posSecond[1]] != 0:
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
                    if self.direction_first == "up":
                        screen.blit(self.blue_direction_arr[0], rect)
                    if self.direction_first == "down":
                        screen.blit(self.blue_direction_arr[1], rect)
                    if self.direction_first == "left":
                        screen.blit(self.blue_direction_arr[2], rect)
                    if self.direction_first == "right":
                        screen.blit(self.blue_direction_arr[3], rect)
                if row == self.posSecond[0] and col == self.posSecond[1]:
                    color = pygame.Color('orange')
                    pygame.draw.rect(screen, color, rect)
                    if self.direction_second == "up":
                        screen.blit(self.red_direction_arr[0], rect)
                    if self.direction_second == "down":
                        screen.blit(self.red_direction_arr[1], rect)
                    if self.direction_second == "left":
                        screen.blit(self.red_direction_arr[2], rect)
                    if self.direction_second == "right":
                        screen.blit(self.red_direction_arr[3], rect)
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
                  "Управление голубым гонщиком WASD",
                  "Управление оранжевым гонщиком Стрелочки",
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
                board.restart('restart')
    if not restart_pressed:
        board.next_move()
    screen.fill((27, 53, 52))
    board.render(screen)
    pygame.display.flip()
    clock.tick(FPS_game)
pygame.quit()
