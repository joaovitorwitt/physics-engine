from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from geometry.geometry import Geometry
from numpy import arange
from material.lineMaterial import LineMaterial
from material.pointMaterial import PointMaterial
from OpenGL.GL import *
from math import sin

# generates an image with vertices along the graph of a sine function
class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 5])


        geometry = Geometry()
        posData = []

        for x in arange(-3.2, 3.2, 0.3):
            posData.append([x, sin(x), 0])

        geometry.addAttribute("vec3", "vertexPosition", posData)
        geometry.countVertices()

        pointMaterial = PointMaterial({"baseColor": [1, 1, 0], "pointSize": 10, "roundedPoints": True})
        pointMesh = Mesh(geometry, pointMaterial)

        lineMaterial = LineMaterial({"baseColor": [1,0,1], "lineWidth": 4})
        lineMesh = Mesh(geometry, lineMaterial)

        self.scene.add(pointMesh)
        self.scene.add(lineMesh)


    def update(self):
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()