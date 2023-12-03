from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.texture import Texture


from OpenGL.GL import *
from math import floor, pi
from geometry.rectangleGeometry import RectangleGeometry
from material.spriteMaterial import SpriteMaterial
from extras.movementRig import MovementRig
from extras.gridHelper import GridHelper


#  take an image and segment it into smaller chunks to constanly change the image
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

        geometry = RectangleGeometry()
        tileSet = Texture("images/rolling-ball.jpg")
        spriteMaterial = SpriteMaterial(tileSet, {
            "billboard": 1,
            "tileCount": [4,4],
            "tileNumber": 0
        })

        self.tilesPerSecond = 8
        
        self.sprite = Mesh(geometry, spriteMaterial)
        self.scene.add(self.sprite)

        grid = GridHelper(size=20, gridColor=[1,1,1], centerColor=[1,1,0])
        grid.rotateX(-pi / 2)
        self.scene.add(grid)

    def update(self):
        tileNumber = floor(self.time * self.tilesPerSecond)
        self.sprite.material.uniforms["tileNumber"].data = tileNumber
        self.rig.update(self.input, self.deltaTime)
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()