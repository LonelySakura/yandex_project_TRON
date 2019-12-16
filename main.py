import pygame
from board import Board
import time


class TRON(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.colors = [None, pygame.Color('blue'), pygame.Color('red')]
        self.select = None
        self.board[12][0] = 1
        self.board[12][24] = 2
        self.direction_first = 'right'
        self.direction_second = 'left'

    def next_move(self):
        pass

    def change_direction(self, player, direction):
        if player == 1:
            if direction == 'up':
                self.direction_first = 'up'
            elif direction == 'down':
                self.direction_first = 'down'
            elif direction == 'right':
                self.direction_first = 'right'
            elif direction == 'left':
                self.direction_first = 'left'
        elif player == 2:
            if direction == 'up':
                self.direction_second = 'up'
            elif direction == 'down':
                self.direction_second = 'down'
            elif direction == 'right':
                self.direction_second = 'right'
            elif direction == 'left':
                self.direction_second = 'left'

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size, self.cell_size
                )
                color = self.colors[self.board[row][col]]
                if color:
                    pygame.draw.rect(screen, color, rect)
        super().render(screen)


pygame.init()
w, h = 25, 25
size = width, height = 40 + w * 10, 40 + h * 10
screen = pygame.display.set_mode(size)
board = TRON(w, h)
running = True
while running:
    for event in pygame.event.get():
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
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
