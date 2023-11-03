import pygame


class Input(object):
    def __init__(self):
        # has the user quit the application?
        self.quit = False

    def update(self):
        # iterate over all user input the occured since the last time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True