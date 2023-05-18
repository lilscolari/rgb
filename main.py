from sys import exit
import pygame
import time

pygame.init()

screen = pygame.display.set_mode((1800, 1000))
pygame.display.set_caption("cool RGB")
clock = pygame.time.Clock()

def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

# Changes background color through RGB scale.
def rgb():
    x, y, z = 255, 0, 0
    colors = [x, y, z]
    color = colors
    while True:
        while colors[1] < 255:
            screen.fill(color)
            pygame.display.update()
            colors[1] += 1
            time.sleep(0.01)
            quit()
        while colors[0] > 0:
            screen.fill(color)
            pygame.display.update()
            colors[0] -= 1
            time.sleep(0.007)
            quit()
        while colors[2] < 255:
            screen.fill(color)
            pygame.display.update()
            colors[2] += 1
            time.sleep(0.007)
            quit()
        while colors[1] > 0:
            screen.fill(color)
            pygame.display.update()
            colors[1] -= 1
            time.sleep(0.007)
            quit()
        while colors[0] < 255:
            screen.fill(color)
            pygame.display.update()
            colors[0] += 1
            time.sleep(0.007)
            quit()
        while colors[2] > 0:
            screen.fill(color)
            pygame.display.update()
            colors[2] -= 1
            time.sleep(0.007)
            quit()

# main game loop
run = True
def main():
    while run:
        rgb()
        clock.tick(60)
    main()

if __name__ == "__main__":
    main()