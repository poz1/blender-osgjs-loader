from .yson import *
from .skeleton import *
from .bone import *
from .model import *

################################################
# BINDPOSE=0
BINDPOSE = 1
################################################

class Osgjs:
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
            getNode(ys, Node[0], n, bone)
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
                            bindPose(bindskeleton.object, skeleton.object, mesh.object)
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
