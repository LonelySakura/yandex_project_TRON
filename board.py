import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 20
        self.top = 20
        self.cell_size = 20
        self.color = pygame.Color('white')

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                pygame.draw.rect(screen, self.color, rect, 1)

    def get_cell(self, mouse_pos):
        col = (mouse_pos[0] - self.left) // self.cell_size
        row = (mouse_pos[1] - self.top) // self.cell_size
        if 0 <= col < self.width and 0 <= row < self.height:
            return col, row

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)
