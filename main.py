import pygame
from board import Board
import time


class TRON(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.direction_first = 'right'
        self.direction_second = 'left'
        self.posFirst = [self.height // 2, 0]
        self.posSecond = [self.height // 2, self.height - 1]

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
        # print(self.board[self.posFirst[0]][self.posFirst[1]])
        # if self.board[self.posFirst[0]][self.posFirst[1]] != 0:
        #    print("Первый Луз")
        # if self.board[self.posSecond[0]][self.posSecond[1]] != 0:
        #    print("Второй Луз")

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
size = width, height = 40 + w * 20, 40 + h * 20
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
    board.next_move()
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
    time.sleep(0.20)
pygame.quit()
