from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from core.uniform import Uniform
from OpenGL.GL import *
from math import sin, cos

class Test(Base):
    def initialize(self):
        print("Initializing Program....")

        # intializate program
        vsCode = """
        in vec3 position;
        uniform vec3 translation;
        void main() {
            vec3 pos = position + translation;
            gl_Position = vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main() {
            fragColor = vec4(baseColor.r, baseColor.g, baseColor.b, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        # specify color used when clearly
        glClearColor(0.0, 0.0, 0.0, 1.0)

        # set up vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        # set up vertex array attribute
        positionData = [[0.0, 0.2, 0.0], [0.2, -0.2, 0.0], [-0.2, -0.2, 0.0]]
        self.vertexCount = len(positionData)
        positionAttribute = Attribute("vec3", positionData)
        positionAttribute.associateVariable(self.programRef, "position")

        # set up uniforms
        self.translation1 = Uniform("vec3", [-0.4, 0.0, 0.0])
        self.translation1.locateVariable(self.programRef, "translation")

        self.baseColor1 = Uniform("vec3", [1.0, 0.0, 0.0])
        self.baseColor1.locateVariable(self.programRef, "baseColor")

        ################################################################

        self.translation2 = Uniform("vec3", [0.4, 0.0, 0.0])
        self.translation2.locateVariable(self.programRef, "translation")

        self.baseColor2 = Uniform("vec3", [0.0, 1.0, 0.0])
        self.baseColor2.locateVariable(self.programRef, "baseColor")

        ################################################################

        self.translation3 = Uniform("vec3", [0.0, 0.0, 0.0])
        self.translation3.locateVariable(self.programRef, "translation")

        self.baseColor3 = Uniform("vec3", [0.0, 0.0, 1.0])
        self.baseColor3.locateVariable(self.programRef, "baseColor")

        ################################################################
        
        self.translation4 = Uniform("vec3", [-0.8, 0.0, 0.0])
        self.translation4.locateVariable(self.programRef, "translation")

        self.baseColor4 = Uniform("vec3", [0.5, 0.5, 0.5])
        self.baseColor4.locateVariable(self.programRef, "baseColor")

        ################################################################

        self.translation5 = Uniform("vec3", [0.8, 0.0, 0.0])
        self.translation5.locateVariable(self.programRef, "translation")

        self.baseColor5 = Uniform("vec3", [0.471, 0.318, 0.663])
        self.baseColor5.locateVariable(self.programRef, "baseColor")



    def update(self):
        # X and Y coordinates for the first triangle
        self.translation1.data[0] = 0.5 * -sin(self.time)
        self.translation1.data[1] = 0.5 * -cos(self.time)

        # constantly update the colors for the first triangle
        self.baseColor1.data[0] = (sin(self.time) + 1) / 2
        self.baseColor1.data[1] = (sin(self.time + 3.4) + 1) / 2
        self.baseColor1.data[2] = (sin(self.time + 6.8) + 1) / 2

        # X and Y coordinates for the second triangle
        self.translation2.data[0] = 0.8 * sin(self.time)
        self.translation2.data[1] = 0.5 * cos(self.time)

        # constantly update the colors for the second triangle
        self.baseColor2.data[0] = (sin(self.time) + 1) / 2
        self.baseColor2.data[1] = (sin(self.time + 2.1) + 1) / 2
        self.baseColor2.data[2] = (sin(self.time + 4.2) + 1) / 2

        # X and Y coordinates for the third triangle
        self.translation3.data[0] = 0.5 * sin(self.time)
        self.translation3.data[1] = 0.5 * -cos(self.time)

        # constantly update the colors for the third triangle
        self.baseColor3.data[0] = (sin(self.time) + 1) / 2
        self.baseColor3.data[1] = (sin(self.time + 1.5) + 1) / 2
        self.baseColor3.data[2] = (sin(self.time + 3) + 1) / 2

        # X and Y coordinates for the fourth triangle
        self.translation4.data[0] = 0.5 * sin(self.time)
        self.translation4.data[1] = 0.5 * cos(self.time)

        # constantly update the colors for the fourth triangle
        self.baseColor4.data[0] = (sin(self.time) + 1) / 2
        self.baseColor4.data[1] = (sin(self.time + 1.2) + 1) / 2
        self.baseColor4.data[2] = (sin(self.time + 2.4) + 1) / 2

        # X and Y coordinates for the fifth triangle
        self.translation5.data[0] = 0.5 * -sin(self.time)
        self.translation5.data[1] = 0.5 * cos(self.time)

        # constantly update the colors for the fifth triangle
        self.baseColor5.data[0] = (sin(self.time) + 1) / 2
        self.baseColor5.data[1] = (sin(self.time + 1.7) + 1) / 2
        self.baseColor5.data[2] = (sin(self.time + 3.4) + 1) / 2


        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(self.programRef)

        # draw first triangle
        self.translation1.uploadData()
        self.baseColor1.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

        # draw second triangle
        self.translation2.uploadData()
        self.baseColor2.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

        # draw third triangle
        self.translation3.uploadData()
        self.baseColor3.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

        # draw fourth triangle
        self.translation4.uploadData()
        self.baseColor4.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)

        # draw fifth triangle
        self.translation5.uploadData()
        self.baseColor5.uploadData()
        glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)


# instantiate class and run program
Test().run()
        

