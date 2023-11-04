from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *


class Test(Base):
    def initialize(self):
        print("Initializing Program....")

        # intializate program
        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main() {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0)
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        out vec4 color;
        void main() {
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0)
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # set up vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up vertex array attribute
        positionData = [[0.0, 0.2, 0.0], [0.2, -0.2, 0.0], [-0.2, -0.2, 0.0]]
        

