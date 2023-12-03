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
from core.renderTarget import RenderTarget
from geometry.boxGeometry import BoxGeometry
from material.surfaceMaterial import SurfaceMaterial

# mipmap effect
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


        # sphere
        sphereGeometry = SphereGeometry()
        sphereMaterial = TextureMaterial(Texture("images/grid.png"))
        
        self.sphere = Mesh(sphereGeometry, sphereMaterial)
        self.sphere.setPosition([-1.2, 1, 0])
        self.scene.add(self.sphere)

        # box
        boxGeometry = BoxGeometry(width=2, height=2, depth=0.2)
        boxMaterial = SurfaceMaterial({"baseColor": [0,0,0]})
        box = Mesh(boxGeometry, boxMaterial)
        box.setPosition([1.2, 1, 0])
        self.scene.add(box)

        # create "television screen" effect
        self.renderTarget = RenderTarget(resolution=[512, 512])
        screenGeometry = RectangleGeometry(width=1.8, height=1.8)
        screenMaterial = TextureMaterial(self.renderTarget.texture)
        screen = Mesh(screenGeometry, screenMaterial)
        screen.setPosition([1.2, 1, 0.11])
        self.scene.add(screen)


        # create second camera that will be used when rendering to the texture
        self.skyCamera = Camera(aspectRatio=512/512)
        self.skyCamera.setPosition([0, 10, 0.1])
        self.skyCamera.lookAt([0,0,0])
        self.scene.add(self.skyCamera)
         
    # this might be used to render a mipmap on a game
    def update(self):

        self.sphere.rotateY(0.01337)
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.skyCamera, renderTarget=self.renderTarget)
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()