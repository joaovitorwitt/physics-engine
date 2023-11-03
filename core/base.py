import pygame
import sys

from core.input import Input

class Base(object):
    def __init__(self, screenSize=[512, 512]):

        # initialize pygame modules
        pygame.init()

        # indicate rendering details
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        # initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 4)

        # Use core OpenGl profile for cross-platform compatibility
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        # Create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # Set the text that appear on the title bar of the window
        pygame.display.set_caption("Physics Engine")

        # determine if main loop is active
        self.running = True
        
        # manage time-related data and operations
        self.clock = pygame.time.Clock()

        # manage user input
        self.input = Input()

    # implement by extending class
    def initialize(self):
        pass

    # implement by extending class
    def update(self):
        pass

    def run(self):
        # startup
        self.initialize()

        # main loop
        while self.running:
            # process input
            # this code will enable the user to stop the application
            self.input.update()
            if self.input.quit:
                self.running = False

            # update
            self.update()

            # render
            # display image on the screen
            pygame.display.flip()

            # pause if necessary to achieve 60 fps
            self.clock.tick(60)

        # shutdown
        pygame.quit()
        sys.exit()




