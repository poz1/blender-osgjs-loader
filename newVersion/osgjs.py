from .yson import *
from .Skeleton.skeleton import *
from .Skeleton.bone import *
from .Mesh.model import *
from .Util.var import *
from .Mesh.mesh import *

################################################
# BINDPOSE=0
BINDPOSE = 1
################################################

class Osgjs:

    def getGeometry(ys, parent, n):
        print('#'*50, 'Geometry')
        n += 4
        mode = None
        indiceArray = []
        vertexArray = []
        texArray = []
        atributes = {}

        #write(log, ['Geometry'], n)
        PrimitiveSetList = ys.get(parent, '"PrimitiveSetList"')
        if PrimitiveSetList:
            indiceArray = getPrimitiveSetList(ys, PrimitiveSetList, n)

        UserDataContainer = ys.get(parent, '"UserDataContainer"')
        if UserDataContainer:
            for UserData in UserDataContainer:
                Values = ys.get(UserData, '"Values"')
                if Values:
                    for a in Values[0].children:
                        values = ys.values(a.data, ':')
                        Name = ys.getValue(values, '"Name"', '""')
                        Value = ys.getValue(values, '"Value"', '""')
                        #if Name:write(log,[Name,Value],n+4)
                        if Name:
                            atributes[Name] = Value

        VertexAttributeList = ys.get(parent, '"VertexAttributeList"')
        if VertexAttributeList:
            vertexArray, texArray = getVertexAttributeList(ys, VertexAttributeList, n)

        # print atributes
        mesh = Mesh()
        if len(indiceArray) > 0:
            for [indices, mode] in indiceArray:
                print(mode, len(indices))
                mat = Mat()
                mesh.matList.append(mat)
                mat.IDStart = len(mesh.indiceList)
                mat.IDCount = len(indices)
                mesh.indiceList.extend(indices)
                if mode == '"TRIANGLE_STRIP"':
                    mat.TRISTRIP = True
                if mode == '"TRIANGLES"':
                    mat.TRIANGLE = True

            indices = indiceArray[0][0]
            mode = indiceArray[0][1]
            if len(vertexArray) == 1:
                if vertexArray[0][1] == '"varint"':
                    bytes = vertexArray[0][0]
                    ItemSize = vertexArray[0][2]
                    if mode == '"TRIANGLE_STRIP"':
                        bytes = decodePredict(indices, bytes, ItemSize)
                    s1 = float(atributes['vtx_bbl_x'])
                    s2 = float(atributes['vtx_bbl_y'])
                    s3 = float(atributes['vtx_bbl_z'])
                    s = [s1, s2, s3]
                    a1 = float(atributes['vtx_h_x'])
                    a2 = float(atributes['vtx_h_y'])
                    a3 = float(atributes['vtx_h_z'])
                    a = [a1, a2, a3]
                    floats = decodeQuantize(bytes, s, a, ItemSize)
                    mesh.vertPosList = [floats[m:m+ItemSize]
                                        for m in range(0, len(floats), 3)]
                else:
                    list = vertexArray[0][0]
                    mesh.vertPosList = list

            if len(texArray) == 1:
                if texArray[0][1] == '"varint"':
                    bytes = texArray[0][0]
                    ItemSize = texArray[0][2]
                    if mode == '"TRIANGLE_STRIP"':
                        bytes = decodePredict(indices, bytes, ItemSize)
                    s1 = float(atributes['uv_0_bbl_x'])
                    s2 = float(atributes['uv_0_bbl_y'])
                    s = [s1, s2]
                    a1 = float(atributes['uv_0_h_x'])
                    a2 = float(atributes['uv_0_h_y'])
                    a = [a1, a2]
                    floats = decodeQuantize(bytes, s, a, ItemSize)
                    for m in range(0, len(floats), ItemSize):
                        u, v = floats[m:m+ItemSize]
                        mesh.vertUVList.append([u, 1-v])

                else:
                    list = texArray[0][0]
                    mesh.vertUVList = list

        return mesh


    def getMatrixTransform(self, ys, parent, n, boneParent):
        #write(log, ['MatrixTransform'], n)
        n += 4
        bone = Bone()
        bone.name = str(len(skeleton.boneList))
        skeleton.boneList.append(bone)
        bone.parentName = boneParent.name

        Name = None
        for child in parent.children:
            values = ys.values(child.header, ':')
            Name = ys.getValue(values, '"Name"', '""')
            if Name:
                Name = self.getSplitName(Name, '_', -1)
                #write(log, [Name], n)
                #if len(Name)<25:bone.name=Name
                boneIndeksList[Name] = bone.name

        for child in parent.children:
            if '"Matrix"' in child.header:
                floats = ys.values(child.data, 'f')
                #write(log, floats, n)
                bone.matrix = Matrix4x4(floats)
                bone.matrix *= boneParent.matrix
        for child in parent.children:
            if '"Children"' in child.header:
                self.getChildren(ys, child, n, bone)


    def getSkeletonNode(self, ys, parent, n, boneParent):
        global firstmatrix
        #write(log, ['Skeleton'], n)
        n += 4
        bone = Bone()
        bone.name = str(len(skeleton.boneList))
        skeleton.boneList.append(bone)
        bone.parentName = boneParent.name

        firstmatrix = boneParent.matrix

        Name = None
        for child in parent.children:
            values = ys.values(child.header, ':')
            Name = ys.getValue(values, '"Name"', '""')
            if Name:
                Name = self.getSplitName(Name, '_', -1)
                # print Name
                #write(log, [Name], n)
                #if len(Name)<25:bone.name=Name
                boneIndeksList[Name] = bone.name

        for child in parent.children:
            if '"Matrix"' in child.header:
                floats = ys.values(child.data, 'f')
                #write(log, floats, n)
                bone.matrix = Matrix4x4(floats)
                bone.matrix *= boneParent.matrix
        for child in parent.children:
            if '"Children"' in child.header:
                self.getChildren(ys, child, n, bone)


    def getRigGeometryNode(self ,ys, parent, n, boneParent):
        #write(log, ['RigGeometry'], n)
        mesh = self.getRigGeometry(ys, parent, n)
        if len(mesh.vertPosList) > 0:
            model.meshList.append(mesh)
            mesh.matrix = boneParent.matrix

        n += 4
        for child in parent.children:
            if '"Children"' in child.header:
                self.getChildren(ys, child, n, boneParent)


    def getGeometryNode(self, ys, parent, n, boneParent):
        #write(log, ['Geometry'], n)
        mesh = self.getGeometry(ys, parent, n)
        if len(mesh.vertPosList) > 0:
            model.meshList.append(mesh)
            mesh.matrix = boneParent.matrix

        n += 4
        for child in parent.children:
            if '"Children"' in child.header:
                self.getChildren(ys, child, n, boneParent)


    def getBoneNode(self, ys, parent, n, boneParent):
        #write(log, ['Bone'], n)
        bone = Bone()
        bone.parentName = boneParent.name
        bone.name = str(len(skeleton.boneList))
        skeleton.boneList.append(bone)

        n += 4
        Name = None
        for child in parent.children:
            values = ys.values(child.header, ':')
            # print child.header
            Name = ys.getValue(values, '"Name"', '""')
            if Name:
                Name = getSplitName(Name, '_', -1)
                #write(log, [Name], n)
                # print Name
                #if len(Name)<25:bone.name=Name
                boneIndeksList[Name] = bone.name

        for child in parent.children:
            if '"Matrix"' in child.header:
                values = ys.values(child.header, ':')
                floats = ys.values(child.data, 'f')
                bone.matrix = Matrix4x4(floats)
                bone.matrix *= boneParent.matrix

            if '"InvBindMatrixInSkeletonSpace"' in child.header:
                bindbone = Bone()
                #if Name:bindbone.name=Name
                bindbone.name = bone.name
                bindskeleton.boneList.append(bindbone)
                floats = ys.values(child.data, 'f')
                #write(log, [floats], n+4)
                matrix = Matrix4x4(floats).invert()
                bindbone.matrix = matrix*firstmatrix

        for child in parent.children:
            if '"Children"' in child.header:
                self.getChildren(ys, child, n, bone)


    def getChildren(self, ys, parent, n, boneParent):
        #write(log, ['Children'], n)
        n += 4
        for child in parent.children:
            for a in child.children:
                if '"osg.MatrixTransform"' in a.header:
                    self.getMatrixTransform(ys, a, n, boneParent)
                if '"osg.Node"' in a.header:
                    self.getNode(ys, a, n, boneParent)
                if '"osgAnimation.Skeleton"' in a.header:
                    self.getSkeletonNode(ys, a, n, boneParent)
                if '"osgAnimation.RigGeometry"' in a.header:
                    self.getRigGeometryNode(ys, a, n, boneParent)
                if '"osg.Geometry"' in a.header:
                    self.getGeometryNode(ys, a, n, boneParent)
                if '"osgAnimation.Bone"' in a.header:
                    self.getBoneNode(ys, a, n, boneParent)


    def getNode(self, ys, parent, n, boneParent):
        #write(log, ['Node'], n)
        n += 4

        bone = Bone()
        bone.name = str(len(skeleton.boneList))
        skeleton.boneList.append(bone)
        bone.parentName = boneParent.name
        bone.matrix = boneParent.matrix

        Name = None
        for child in parent.children:
            values = ys.values(child.header, ':')
            Name = ys.getValue(values, '"Name"', '""')
            if Name:
                # Name=getSplitName(Name,'_',-1)
                #¶write(log, [Name], n)
                #if len(Name)<25:bone.name=Name
                boneIndeksList[Name] = bone.name

        for child in parent.children:
            if '"Children"' in child.header:
                self.getChildren(ys, child, n, bone)


    def bindPose(self, bindSkeleton, poseSkeleton, meshObject):
        # print 'BINDPOSE'
        mesh = meshObject.getData(mesh=1)
        poseBones = poseSkeleton.getData().bones
        bindBones = bindSkeleton.getData().bones
        # mesh.transform(meshObject.matrixWorld)
        mesh.update()
        for vert in mesh.verts:
            index = vert.index
            skinList = mesh.getVertexInfluences(index)
            vco = vert.co.copy()*meshObject.matrixWorld
            vector = Vector()
            sum = 0
            for skin in skinList:
                bone = skin[0]
                weight = skin[1]
                if bone in list(bindBones.keys()) and bone in list(poseBones.keys()):
                    matA = bindBones[bone].matrix['ARMATURESPACE'] * \
                        bindSkeleton.matrixWorld
                    matB = poseBones[bone].matrix['ARMATURESPACE'] * \
                        poseSkeleton.matrixWorld
                    vector += vco*matA.invert()*matB*weight
                    sum += weight
                else:
                    vector = vco
                    break
            vert.co = vector
        mesh.update()
        Blender.Window.RedrawAll()


	def __init__(self, filename):
        global skeleton, bindskeleton, model, boneIndeksList, firstmatrix
        boneIndeksList = {}
        model = Model(filename)
        skeleton = Skeleton()
        skeleton.ARMATURESPACE = True
        bindskeleton = Skeleton()
        bindskeleton.NICE = True
        bindskeleton.ARMATURESPACE = True
        ys = Yson()
        ys.log = True
        ys.filename = filename
        ys.parse()

        firstmatrix = Matrix4x4([1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1])

        n = 0
        bone = Bone()
        bone.matrix = Matrix().resize4x4()
        bone.name = str(len(skeleton.boneList))
        bone.name = 'scene'
        skeleton.boneList.append(bone)
        Node = ys.get(ys.root, '"osg.Node"')
        if Node:
            self.getNode(ys, Node[0], n, bone)
        if len(bindskeleton.boneList) > 0:
            bindskeleton.draw()

        for mesh in model.meshList:
            if len(mesh.skinList) > 0:
                for map in mesh.BoneMap:
                    if map == 0:
                        break
                    mesh.boneNameList.append(boneIndeksList[map])

        for mesh in model.meshList:
            if len(mesh.skinList) > 0:
                skeleton.NICE = True
                skeleton.draw()
                break

        for mesh in model.meshList:
            mesh.draw()
            if mesh.object:
                if len(mesh.skinList) > 0:
                    if BINDPOSE == 1:
                        if bindskeleton.object and skeleton.object:
                            mesh.object.getData(mesh=1).transform(mesh.matrix)
                            mesh.object.getData(mesh=1).update()
                            # mesh.object.setMatrix(mesh.matrix)
                            self.bindPose(bindskeleton.object, skeleton.object, mesh.object)
                            # mesh.object.setMatrix(mesh.matrix.invert()*mesh.object.matrixWorld)
                            scene = bpy.data.scenes.active
                            scene.objects.unlink(bindskeleton.object)
                    else:
                        if bindskeleton.object and skeleton.object:
                            mesh.object.getData(mesh=1).transform(mesh.matrix)
                            mesh.object.getData(mesh=1).update()

                else:
                    mesh.object.setMatrix(mesh.matrix)

        n = 0
        Animations = ys.get(ys.root, '"osgAnimation.Animationnnnn"')
        if Animations:
            for animation in Animations:
                getAnimation(ys, animation, n)
