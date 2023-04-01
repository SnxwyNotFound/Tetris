import pygame
import random
import blocks

window = pygame.display.set_mode((500,1000))

clock = pygame.time.Clock()
run = True


class Block():
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color
    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)

blockss = []

for j in range(20):
    for i in range(10):
        blockss.append(Block(pygame.Rect(5 + 50 * i, 5 + 50 * j, 40, 40), ((0,0,0))))


while run:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    window.fill((255,255,255))

    for b in blockss:
        b.draw()

    pygame.display.update()
    clock.tick(40)
