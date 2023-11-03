from OpenGL.GL import *

# static methods to load and compile OpenGl shaders and link to create programs

class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):
        # Specify required OpenGL/GLSL version
        shaderCode = '#version 330\n' + shaderCode

        # Create empty shader object and return reference value
        shaderRef = glCreateShader(shaderType)