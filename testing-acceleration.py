from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh

from geometry.sphereGeometry import SphereGeometry

from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi, pow

from extras.axisHelper import AxesHelper
from extras.gridHelper import GridHelper
from extras.movementRig import MovementRig

import time

class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        # self.rig.setPosition([0.5, 1, 5])
        self.rig.setPosition([3, 5, 10])
        self.scene.add(self.rig)

        axes = AxesHelper(axisLength=2)
        self.scene.add(axes)

        grid = GridHelper(divisions=20, size=20, gridColor=[1,1,1], centerColor=[1,1,0])
        grid.rotateX(-pi/2)
        self.scene.add(grid)

        # constant acceleration sphere
        constantAcceleration = SphereGeometry(radius=1)
        constantMaterial = SurfaceMaterial({"wireframe": True, "lineWidth": 1, "doubleSize": True, "useVertexColors": True})
        self.constantMesh = Mesh(constantAcceleration, constantMaterial)
        self.constantMesh.setPosition([-20, 2, -4])
        self.scene.add(self.constantMesh)

        # increasing acceleration sphere
        increasingAcceleration = SphereGeometry(radius=1)
        increasingMaterial = SurfaceMaterial({"wireframe": True, "lineWidth": 1, "doubleSize": True, "useVertexColors": True})
        self.increasingMesh = Mesh(increasingAcceleration, increasingMaterial)
        self.increasingMesh.setPosition([-20, 2, 4])
        self.scene.add(self.increasingMesh)


        # velocity formula = distance / time (its actually delta)
        # acceleration formula = velocity / time (also delta)
        self.distance = 1
        self.time = 100
        self.constantAcceleration = self.distance / self.time
        self.increasingAcceleration = 0


    def update(self):
        self.rig.update(self.input, self.deltaTime)

        # make spheres orbit their own axis
        # self.constantMesh.rotateY(0.009)
        # self.increasingMesh.rotateY(0.009)

        self.increasingAcceleration += self.constantAcceleration / self.time
        # print(f"{self.increasingAcceleration:.2f} units/second")

        # we could consider these values the actual velocity
        self.increasingMesh.translate(self.increasingAcceleration, 0, 0)
        self.constantMesh.translate(self.constantAcceleration, 0, 0)

        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()