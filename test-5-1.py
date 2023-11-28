from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial

from geometry.rectangleGeometry import RectangleGeometry

from OpenGL.GL import *


class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 2])


        geometry = RectangleGeometry()
        grid = Texture("images/grid.jpg")
        material = TextureMaterial(grid)
        self.mesh = Mesh( geometry, material )
        self.scene.add(self.mesh)
        self.mesh.setPosition([0, 0, 0])


    def update(self):
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()