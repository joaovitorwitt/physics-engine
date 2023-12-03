from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial
from extras.textTexture import TextTexture

from geometry.sphereGeometry import SphereGeometry

from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi

from geometry.rectangleGeometry import RectangleGeometry
from geometry.boxGeometry import BoxGeometry
from material.textureMaterial import TextureMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHelper


class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0, 0.5, 3])
        self.scene.add(self.rig)

        crateGeometry = BoxGeometry()
        crateMaterial = TextureMaterial(Texture("images/crate.jpg"))
        crate = Mesh(crateGeometry, crateMaterial)
        self.scene.add(crate)

        grid = GridHelper(gridColor=[1,1,1], centerColor=[1,1,0])
        grid.rotateX(-pi/2)
        self.scene.add(grid)

        # HUD stuff
        self.hudScene = Scene()
        self.hudCamera = Camera()
        self.hudCamera.setOrthographic(0,800, 0,600, 1,-1)
        
        # first label
        labelGeometry1 = RectangleGeometry(width=600, height=80, position=[0, 600], alignment=[0, 1])
        labelMaterial1 = TextureMaterial(Texture("images/crate-simulator.png"))
        label1 = Mesh(labelGeometry1, labelMaterial1)

        # add first label to the HUD scene
        self.hudCamera.add(label1)

        # second label
        labelGeometry2 = RectangleGeometry(width=400, height=80, position=[800, 0], alignment=[1, 0])

        labelMessage2 = TextTexture(
            text="Version 1.0",
            systemFontName="Ink Free",
            fontSize=32,
            fontColor=[127, 255, 127],
            imageWidth=200,
            imageHeight=200,
            transparent=True
        )

        labelMaterial2 = TextureMaterial(labelMessage2)
        label2 = Mesh(labelGeometry2, labelMaterial2)

        # add second label to the HUD scene
        self.hudCamera.add(label2)


    def update(self):
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.camera)
        self.renderer.render(self.hudCamera, self.hudCamera, clearColor=False)



# instantiate class and run the program
Test(screenSize=[800, 600]).run()