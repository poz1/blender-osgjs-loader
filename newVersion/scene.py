import bpy


class SceneIDList:
    def __init__(self):
        meshIDList = []
        objectIDList = []
        szkieletIDList = []
        scene = bpy.data.scenes.active
        for object in scene.objects:
            if object.getType() == 'Mesh':
                try:
                    meshID = int(object.getData(mesh=1).name.split('-')[0])
                    meshIDList.append(meshID)
                except:
                    pass
                try:
                    objectID = int(object.getData(mesh=1).name.split('-')[2])
                    objectIDList.append(objectID)
                except:
                    pass
        for mesh in bpy.data.meshes:
            try:
                objectID = int(mesh.name.split('-')[2])
                objectIDList.append(objectID)
            except:
                pass
        for mesh in bpy.data.armatures:
            try:
                ID = int(mesh.name.split('-')[1])
                szkieletIDList.append(ID)
            except:
                pass
        try:
            self.meshID = max(meshIDList)+1
        except:
            self.meshID = 0
        try:
            self.objectID = max(objectIDList)+1
        except:
            self.objectID = 0
        try:
            self.szkieletID = max(szkieletIDList)+1
        except:
            self.szkieletID = 0
        scene.update()
