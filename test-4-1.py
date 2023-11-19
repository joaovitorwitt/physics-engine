from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh

from geometry.boxGeometry import BoxGeometry
from geometry.hexagon import HexagonGeometry
from geometry.sphereGeometry import SphereGeometry
from geometry.cylinderGeometry import CylinderGeometry
from geometry.cylindricalGeometry import CylindricalGeometry
from geometry.coneGeometry import ConeGeometry
from geometry.ellipsoidGeometry import EllipsoidGeometry
from geometry.parametricGeometry import ParametricGeometry

from material.surfaceMaterial import SurfaceMaterial
from material.pointMaterial import PointMaterial

from core.openGLUtils import OpenGLUtils

from core.uniform import Uniform

from OpenGL.GL import *
from math import cos, sin


# scene that consists of a spinning cube
class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 5])

        # first box
        geometry = BoxGeometry()
        material = SurfaceMaterial({"wireframe": True, "lineWidth": 3, "doubleSize": True})
        self.mesh = Mesh( geometry, material )
        self.mesh.setPosition([1,1,0])
        self.scene.add(self.mesh)

        # second box
        geometryTwo = BoxGeometry()
        materialTwo = SurfaceMaterial({"wireframe": True, "lineWidth": 2, "doubleSize": True})
        self.meshTwo = Mesh(geometryTwo, materialTwo)
        self.meshTwo.setPosition([0,0,0])
        self.scene.add(self.meshTwo)


    def update(self):
        self.mesh.rotateY(0.02)
        self.mesh.rotateX(0.03)

        self.meshTwo.rotateX(0.032)
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()


# PAGE 188