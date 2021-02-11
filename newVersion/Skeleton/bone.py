class Bone:
    def __init__(self):
        self.id = None
        self.name = None
        self.parentId = None
        self.parentName = None
        self.quat = None
        self.pos = None
        self.matrix = None
        self.posMatrix = None
        self.rotMatrix = None
        self.scaleMatrix = None
        self.children = []
        self.edit = None
