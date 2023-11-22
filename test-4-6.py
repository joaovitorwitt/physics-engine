from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh

from geometry.sphereGeometry import SphereGeometry

from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi

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

        grid = GridHelper(size=20, gridColor=[1,1,1], centerColor=[1,1,0])
        grid.rotateX(-pi/2)
        self.scene.add(grid)

        # center object spinning on its own axis
        geometry = SphereGeometry(radius=2)
        material = SurfaceMaterial({"wireframe": True, "lineWidth": 1, "doubleSize": True, "useVertexColors": True})
        self.mesh = Mesh(geometry, material)
        self.scene.add(self.mesh)

        # secondary sphere
        orbitingSphere = SphereGeometry(radius=1)
        orbitingMaterial = SurfaceMaterial({"wireframe": True, "lineWidth": 1})
        self.secondaryMesh = Mesh(orbitingSphere, orbitingMaterial)
        self.secondaryMesh.setPosition([0,0,0])
        self.scene.add(self.secondaryMesh)


    def update(self):
        self.rig.update(self.input, self.deltaTime)


        # make smaller sphere orbitate the larger sphere
        self.secondaryMesh.translate(0.075*cos(self.time), 0, 0.075*sin(self.time))

        self.mesh.rotateY(0.009)
        self.renderer.render(self.scene, self.camera)


# instantiate class and run the program
Test(screenSize=[800, 600]).run()