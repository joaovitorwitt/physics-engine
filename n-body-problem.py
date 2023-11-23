from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh

from geometry.sphereGeometry import SphereGeometry

from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi, sqrt, radians

from extras.axisHelper import AxesHelper
from extras.gridHelper import GridHelper
from extras.movementRig import MovementRig


class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)

        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.setPosition([0.5, 1, 5])
        self.scene.add(self.rig)

        axes = AxesHelper(axisLength=2)
        self.scene.add(axes)

        grid = GridHelper(divisions=20, size=20, gridColor=[1,1,1], centerColor=[1,1,0])
        grid.rotateX(-pi/2)
        self.scene.add(grid)

        # first body
        firstBody = SphereGeometry(radius=1)
        firstBodyMaterial = SurfaceMaterial({"wireframe": True, "lineWidth": 1, "doubleSize": True, "useVertexColors": True})
        self.firstBodyMesh = Mesh(firstBody, firstBodyMaterial)
        self.firstBodyMesh.setPosition([-3, 1, 0])

        # second body
        secondBody = SphereGeometry(radius=0.7)
        secondBodyMaterial = SurfaceMaterial({"wireframe": True, "lineWidth": 1, "doubleSize": True, "useVertexColors": True})
        self.secondBodyMesh = Mesh(secondBody, secondBodyMaterial)
        self.secondBodyMesh.setPosition([7,1,0])

        # add objects to the scene
        self.scene.add(self.firstBodyMesh)
        self.scene.add(self.secondBodyMesh)

        # units
        self.GRAVITATIONAL_CONSTANT = 1
        self.FIRST_BODY_MASS = 1
        self.SECOND_BODY_MASS = 1
        self.RADIUS = 1
        self.VELOCITY = 0.7
        self.dt = 0.001
        self.TIME = 0


    def update(self):
        self.rig.update(self.input, self.deltaTime)
        self.r = self.RADIUS
        self.GRAVITATIONAL_FORCE = -self.GRAVITATIONAL_CONSTANT*self.FIRST_BODY_MASS*self.SECOND_BODY_MASS*self.r/self.r**2
        self.firstBodyMesh.translate(self.GRAVITATIONAL_FORCE*self.dt, 0, 0)
        self.secondBodyMesh.translate(self.dt/self.FIRST_BODY_MASS, 0, 0)

        self.TIME += self.dt

        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()