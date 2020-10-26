import pygame
import sys
from pygame.locals import *

name = "Frank Aboagye"  # you could place your name here

pygame.init()
dsp = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Printing name in pygame")

black = (0, 0, 0)
white = (255, 255, 255)

font_object = pygame.font.Font('freesansbold.ttf', 30)
text_surface_object = font_object.render(name, True, white)
text_rect_object = text_surface_object.get_rect()
text_rect_object.center = (250, 250)

while True:
    dsp.fill(black)
    dsp.blit(text_surface_object, text_rect_object)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
