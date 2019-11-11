from Cube import Cube
import copy
import rubiktools

class Estado:
    def __init__(self, cube):
        self.cube = copy.deepcopy(cube)
        self.md5 = cube.hash()
