import pygame
import sys
import time
from collections import deque

pygame.init()

pygame.display.set_icon(pygame.image.load('icon.png'))
screen = pygame.display.set_mode((810, 880))
pygame.display.set_caption("Sieve of Eratosthenes (By Fares Manai)")
font = pygame.font.Font('font.ttf', 36)


class Cell:
    cols = {-1: (135, 135, 135), 0: (200, 90, 84), 1: (50, 180, 137)}

    def __init__(self, n, coords):
        self.n = n
        self.state = -1 if (n != 1) else 0
        self.coords = coords
        self.chosencol = (255, 255, 255)
    
    def change_state(self, state):
        self.state = state
        
    def draw_cell(self):
        x, y = self.coords[0], self.coords[1]
        pygame.draw.rect(screen, self.chosencol, (x, y, 70, 70))
        pygame.draw.rect(screen, Cell.cols[self.state], (x + 2, y + 2, 66, 66))
        val = font.render(str(self.n), 1, "WHITE")
        val_rect = val.get_rect(center=(x + 35, y + 35))
        screen.blit(val, val_rect)


cells = []
for i in range(100):
    x = 10 + 80 * (i % 10)
    y = 80 + 80 * (i // 10)
    cells.append(Cell(i + 1, (x, y)))
    
        
def draw_cells():
    for i in range(100):
        cells[i].draw_cell()
        

def draw_title():
    title = font.render("Sieve of Eratosthenes", 1, "WHITE")
    title_rect = title.get_rect(center=(405, 40))
    screen.blit(title, title_rect)


def main():
    animate = False
    elapsed_time = time.time()
    delay = elapsed_time
    while True:
        screen.fill((50, 50, 50))
        draw_cells()
        draw_title()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (not animate) and (event.type == pygame.KEYDOWN):
                for i in range(100):
                    cells[i].chosencol = (255, 255, 255)
                prime = 0
                for i in range(100):
                    if cells[i].state == -1:
                        cells[i].change_state(1)
                        prime = i + 1
                        break
                if prime:
                    animate = True
                    if prime <= 10:
                        change = deque(range(2 * prime, 101, prime))
                        cells[prime - 1].chosencol = (160, 0, 255)
                    else:
                        change = deque([(x + 1) for x in range(100) if cells[x].state == -1])
                        prime = 0
                
        if animate and (abs(delay - elapsed_time) > 0.15):
            if len(change):
                cells[change[0] - 1].change_state(not bool(prime))
                if prime:
                    cells[change[0] - 1].chosencol = (160, 0, 255)
                change.popleft()
                delay = elapsed_time
            else:
                animate = False

        elapsed_time = time.time()
        pygame.display.update()
        pygame.time.Clock().tick(60)
      

if __name__ == '__main__':  
    main()
