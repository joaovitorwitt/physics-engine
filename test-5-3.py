from core.base import Base
from core.renderer import Renderer
from core.camera import Camera
from core.scene import Scene
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial

from geometry.sphereGeometry import SphereGeometry
from geometry.rectangleGeometry import RectangleGeometry

from material.material import Material
from material.surfaceMaterial import SurfaceMaterial

from OpenGL.GL import *
from math import cos, sin, pi



class Test(Base):

    def initialize(self):
        print("Initializing program....")

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=800/600)
        self.camera.setPosition([0, 0, 1.5])

        vertexShaderCode = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec2 vertexUV;
        out vec2 UV;

        void main() {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
            UV = vertexUV;
        }
        """

        fragmentShaderCode = """
        uniform sampler2D texture;
        in vec2 UV;
        uniform float time;
        out vec4 fragColor;

        void main() {
            vec2 shiftUV = UV + vec2(0, 0.2 * sin(6.0*UV.x + time));
            fragColor = texture2D(texture, shiftUV);
        }
        """

        gridTex = Texture("images/grid.png")
        self.waveMaterial = Material(vertexShaderCode, fragmentShaderCode)
        self.waveMaterial.addUniform("sampler2D", "texture", [gridTex.textureRef, 1])
        self.waveMaterial.addUniform("float", "time", 0.0)
        self.waveMaterial.locateUniforms()

        geometry = RectangleGeometry()
        self.mesh = Mesh(geometry, self.waveMaterial)
        self.scene.add(self.mesh)



    def update(self):
        self.renderer.render(self.scene, self.camera)
        self.waveMaterial.uniforms["time"].data += self.deltaTime


# instantiate class and run the program
Test(screenSize=[800, 600]).run()