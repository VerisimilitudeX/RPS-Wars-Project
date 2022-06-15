import random
import pygame
pygame.init()

def get_color(color_name):
    if color_name == "red":
        return (255, 0, 0)
    if color_name == "green":
        return (0, 250, 0)
    if color_name == "blue":
        return (0, 0, 255)

    return (255, 255, 255)

w = pygame.display.set_mode([200, 200])
w.fill((255, 255, 255))
pygame.display.flip()

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    color_string = input("What color should we change to? (x to quit) ")
    if color_string == "x":
        drawing = False
    else:
        color_tuple = get_color(color_string)
        w.fill(color_tuple)

    pygame.display.flip()
