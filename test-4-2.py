from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh

from geometry.geometry import Geometry
from geometry.sphereGeometry import SphereGeometry

from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi


class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 5])


        geometry = Geometry()
        P0 = [-0.1, 0.1, 0.0]
        P1 = [0.0, 0.0, 0.0]
        P2 = [0.1, 0.1, 0.0]
        P3 = [-0.2, -0.2, 0.0]
        P4 = [0.2, -0.2, 0.0]
        posData = [P0, P3, P1, P1, P3, P4, P1, P4, P2]

        geometry.addAttribute("vec3", "vertexPosition", posData)
        R = [1, 0, 0]
        Y = [1, 1, 0]
        G = [0, 0.25, 0]

        colData = [R,G,Y, Y,G,G, Y,G,R]
        geometry.addAttribute("vec3", "vertexColor", colData)
        geometry.countVertices()

        material = SurfaceMaterial({"wireframe": True, "lineWidth": 1, "doubleSize": True, "useVertexColors": 1})
        self.mesh = Mesh( geometry, material )
        self.scene.add(self.mesh)
        self.mesh.setPosition([0, 0, 0])


    def update(self):
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()
