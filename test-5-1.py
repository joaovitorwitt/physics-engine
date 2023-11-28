from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial
from material.surfaceMaterial import SurfaceMaterial

from geometry.rectangleGeometry import RectangleGeometry
from geometry.sphereGeometry import SphereGeometry

from OpenGL.GL import *


class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 2])


        geometry = SphereGeometry(radius=0.5)
        grid = Texture("images/earth.png")
        material = TextureMaterial(grid)
        self.mesh = Mesh( geometry, material )
        self.scene.add(self.mesh)
        self.mesh.setPosition([0, 0, 0])


    def update(self):
        self.renderer.render(self.scene, self.camera)

        self.mesh.rotateY(0.009)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()