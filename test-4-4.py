from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh

from geometry.sphereGeometry import SphereGeometry

from material.material import Material
from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi


# color the surface of an object based on the coordinates of each point
class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 7])

        geometry = SphereGeometry(radius=3)

        vsCode = """
        in vec3 vertexPosition;
        out vec3 position;
        uniform mat4 modelMatrix;

        uniform mat4 viewMatrix;
        uniform mat4 projectionMatrix;
        void main() {
            vec4 pos = vec4(vertexPosition, 1.0);
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * pos;
            position = vertexPosition;
        }
        """

        fsCode = """
        in vec3 position;
        out vec4 fragColor;
        void main() {
            vec3 color = mod(position, 1.0);
            fragColor = vec4(color, 1.0);
        }
        """

        material = Material(vsCode, fsCode)
        material.locateUniforms()

        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)
       

    def update(self):
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()