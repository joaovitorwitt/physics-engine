from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh

from geometry.sphereGeometry import SphereGeometry

from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi


# scene that consists of a spinning cube
class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 5])


        # first sphere (we can duplicate this to create more than one sphere)
        geometry = SphereGeometry(radius=0.4)
        material = SurfaceMaterial({"wireframe": True, "lineWidth": 1, "doubleSize": True, "useVertexColors": 1})
        self.mesh = Mesh( geometry, material )
        self.scene.add(self.mesh)
        self.mesh.setPosition([1, 0, 0])

        # central orbit 
        sunGeometry = SphereGeometry(radius=1)
        sunMaterial = SurfaceMaterial({"wireframe": True, "lineWidth":1, "doubleSize" :True})
        self.meshSun = Mesh(sunGeometry, sunMaterial)
        self.scene.add(self.meshSun)
        self.meshSun.setPosition([0, 0, 0])


    def update(self):

        self.mesh.rotateY(0.009)
        # self.mesh.rotateX(-0.009)

        self.meshSun.rotateY(0.009)

        self.mesh.translate(0.009 * cos(self.time), 0.009 * sin(self.time), 0)

        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()


# PAGE 188