from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial

from geometry.sphereGeometry import SphereGeometry
from geometry.rectangleGeometry import RectangleGeometry

from extras.movementRig import MovementRig

from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi



class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.setPosition([0,1,4])

        # sky
        skyGeometry = SphereGeometry(radius=50)
        skyMaterial = TextureMaterial(Texture("images/sky.jpg"))
        sky = Mesh(skyGeometry, skyMaterial)
        self.scene.add(sky)

        # grass
        grassGeometry = RectangleGeometry(width=100, height=100)
        grassMaterial = TextureMaterial(Texture("images/grass.jpg"), {"repeatUV": [50,50]})
        grass = Mesh(grassGeometry, grassMaterial)
        grass.rotateX(-3.14/2)
        self.scene.add(grass)

        # self.mesh.setPosition([0, 0, 0])


    def update(self):
        self.renderer.render(self.scene, self.camera)
        self.rig.update(self.input, self.deltaTime)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()