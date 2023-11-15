from geometry.geometry import Geometry

class BoxGeometry(Geometry):


    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        P0 = [-width / 2, -height / 2, -depth / 2]
        P1 = [width / 2, -height / 2, -depth / 2]
        P2 = [-width / 2, height / 2, -depth / 2]
        P3 = [width / 2, height / 2, -depth / 2]
        P4 = [-width / 2, -height / 2, depth / 2]
        P5 = [width / 2, -height / 2, depth / 2]
        P6 = [-width / 2, height / 2, depth / 2]
        P7 = [width / 2, height/ 2, depth / 2]

        # colors for faces in order: x+ , x- , y+ , y- , z+, z-
        C1, C2 = [1, 0.5, 0.5], [0.5, 0, 0]
        C3, C4 = [0.5, 1, 0.5], [0, 0.5, 0]
        C5, C7 = [0.5, 0.5, 1], [0, 0, 0.5]

        positionData = [P5,P1,P3,P5,P3,P7, ] 