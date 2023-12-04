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

from extras.postprocessor import Postprocessor
from effects.tintEffect import TintEffect
from effects.invertEffect import InvertEffect
from effects.pixelateEffect import PixelateEffect
from effects.vignetteEffect import VignetteEffect
from effects.colorReduceEffect import ColorReduceEffect

"""
render a scene with different filters applied
"""
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

        # include sphere
        sphereGeometry = SphereGeometry()
        sphereMaterial = TextureMaterial(Texture("images/grid.png"))
        self.sphere = Mesh(sphereGeometry, sphereMaterial)
        self.sphere.setPosition([0,1,0])
        self.scene.add(self.sphere)

        # postprocessing stuff
        self.postprocessor = Postprocessor(self.renderer, self.scene, self.camera)
        self.postprocessor.addEffect(ColorReduceEffect())

    def update(self):
        self.postprocessor.render()
        self.rig.update(self.input, self.deltaTime)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()