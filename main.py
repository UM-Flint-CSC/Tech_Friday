import pygame # import pygame module
from sys import exit # import the exit function from sys module

pygame.init()  # starts all sub parts of pygame needed to make a game
screen = pygame.display.set_mode((800, 400)) # create a display surface to display the game
pygame.display.set_caption("Tech Friday Game Design") # change the window caption
clock = pygame.time.Clock() # create clock object

while True:
    for event in pygame.event.get():  # loop through all events
        if event.type == pygame.QUIT:  # check if event is quit
            exit()  # exit program

    pygame.display.update() # draw elements and update
    clock.tick(60) # set loop to run no faster than 60 times per second
