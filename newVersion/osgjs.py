import yson 
# from .Skeleton.skeleton import *
# from .Skeleton.bone import *
# from .Mesh.model import *
# from .Mesh.mat import *
# from .Util.var import *
# from .Mesh.mesh import *

################################################
# BINDPOSE=0
BINDPOSE = 1
################################################

class Osgjs:

    # def getSplitName(name, what, which):
    #     a = None
    #     if what in name:
    #         a = ''
    #         splits = name.split(what)
    #         if which < 0:
    #             num = len(splits)+which-1
    #         else:
    #             num = which
    #         if num < 0:
    #             a = name
    #         else:
    #             if which < len(splits):
    #                 for m in range(num):
    #                     a += splits[m]+what
    #                 a += splits[num]
    #             else:
    #                 a = name
    #     return a


    # def decodeQuantize(input, s, a, itemsize):
    #     x = [0]*len(input)
    #     id = 0
    #     for r in range(len(input)/itemsize):
    #         for l in range(itemsize):
    #             x[id] = s[l]+input[id]*a[l]
    #             id += 1
    #     return x

    # def decodeVarint(self, g, offset, size, type):
    #     g.seek(offset)
    #     n = [0]*size
    #     a = 0
    #     s = 0
    #     while(a != size):
    #         shift = 0
    #         result = 0
    #         while True:
    #             byte = g.B(1)[0]
    #             result |= (byte & 127) << shift
    #             shift += 7
    #             if not (byte & 0x80):
    #                 break
    #         n[a] = result
    #         a += 1
    #     if type[0] != 'U':
    #         l = 0
    #         while(l < size):
    #             h = n[l]
    #             n[l] = h >> 1 ^ -(1 & h)
    #             l += 1
    #     return n


    # def decodeDelta(self, t, e):
    #     i = e | 0
    #     n = len(t)
    #     if i >= len(t):
    #         r = None
    #     else:
    #         r = t[i]
    #     a = i+1
    #     while(a < n):
    #         s = t[a]
    #         r = t[a] = r+(s >> 1 ^ -(1 & s))
    #         a += 1
    #     return t


    # def decodeImplicit(self, input, n):
    #     IMPLICIT_HEADER_LENGTH = 3
    #     IMPLICIT_HEADER_MASK_LENGTH = 1
    #     IMPLICIT_HEADER_PRIMITIVE_LENGTH = 0
    #     IMPLICIT_HEADER_EXPECTED_INDEX = 2
    #     highWatermark = 2

    #     t = input
    #     e = [0]*t[IMPLICIT_HEADER_PRIMITIVE_LENGTH]
    #     a = t[IMPLICIT_HEADER_EXPECTED_INDEX]
    #     s = t[IMPLICIT_HEADER_MASK_LENGTH]
    #     o = t[IMPLICIT_HEADER_LENGTH:s+IMPLICIT_HEADER_LENGTH]
    #     r = highWatermark
    #     u = 32*s-len(e)
    #     l = 1 << 31
    #     h = 0
    #     while(h < s):
    #         c = o[h]
    #         d = 32
    #         p = h*d
    #         if h == s-1:
    #             f = u
    #         else:
    #             f = 0
    #         g1 = f
    #         while(g1 < d):
    #             if c & l >> g1:
    #                 e[p] = t[n]
    #                 n += 1
    #             else:
    #                 if r:
    #                     e[p] = a
    #                 else:
    #                     e[p] = a
    #                     a += 1
    #             g1 += 1
    #             p += 1
    #         h += 1
    #     return e


    # def decodeWatermark(self, t, e, i):
    #     n = i[0]
    #     r = len(t)
    #     a = 0
    #     while(a < r):
    #         s = n-t[a]
    #         e[a] = s
    #         if n <= s:
    #             n = s+1
    #         a += 1
    #     return e, n





    # def decodePredict(self, indices, input, itemsize):
    #     t = input
    #     if len(indices) > 0:
    #         t = input
    #         e = itemsize
    #         i = indices
    #         n = len(t)/e
    #         r = [0]*n
    #         a = len(i)-1
    #         r[i[0]] = 1
    #         r[i[1]] = 1
    #         r[i[2]] = 1
    #         s = 2
    #         while(s < a):
    #             o = s-2
    #             u = i[o]
    #             l = i[o+1]
    #             h = i[o+2]
    #             c = i[o+3]
    #             if 1 != r[c]:
    #                 r[c] = 1
    #                 u *= e
    #                 l *= e
    #                 h *= e
    #                 c *= e
    #                 d = 0
    #                 while(d < e):
    #                     t[c+d] = t[c+d]+t[l+d]+t[h+d]-t[u+d]
    #                     d += 1
    #             s += 1
    #     return t



    # def getIndices(self, itemsize, size, offset, type, g, mode, magic):
    #     if type != "Uint8Array":
    #         bytes = self.decodeVarint(g, offset, size*itemsize, type)
    #     else:
    #         g.seek(offset)
    #         bytes = list(g.B(size*itemsize))
    #     # write(log,[magic],0)
    #     # write(log,bytes,0)

    #     IMPLICIT_HEADER_LENGTH = 3
    #     IMPLICIT_HEADER_MASK_LENGTH = 1
    #     IMPLICIT_HEADER_PRIMITIVE_LENGTH = 0
    #     IMPLICIT_HEADER_EXPECTED_INDEX = 2
    #     highWatermark = 2

    #     if mode == '"TRIANGLE_STRIP"':
    #         k = IMPLICIT_HEADER_LENGTH+bytes[IMPLICIT_HEADER_MASK_LENGTH]
    #         bytes = self.decodeDelta(bytes, k)
    #         # write(log,[magic,k],0)
    #         # write(log,bytes,0)
    #         bytes = self.decodeImplicit(bytes, k)
    #         # write(log,[magic,k],0)
    #         # write(log,bytes,0)
    #         i = [magic]
    #         bytes, magic = self.decodeWatermark(bytes, bytes, i)
    #         # write(log,[magic],0)
    #         # write(log,bytes,0)

    #     elif mode == '"TRIANGLES"':
    #         k = 0
    #         bytes = self.decodeDelta(bytes, k)
    #         # write(log,[magic],0)
    #         # write(log,bytes,0)
    #         i = [magic]
    #         bytes, magic = self.decodeWatermark(bytes, bytes, i)
    #         # write(log,[magic],0)
    #         # write(log,bytes,0)

    #     return magic, bytes

    # def getPrimitiveSetList(self, ys, PrimitiveSetList, n):
    #     global magic
    #     mode = None
    #     magic = 0
    #     indiceArray = []
    #     for child in PrimitiveSetList[0].children:
    #         for b in child.children:
    #             if '"DrawElementsUInt"' in b.header:
    #                 values = ys.values(b.data, ':')
    #                 mode = values['"Mode"']
    #                 Size = None
    #                 Offset = None
    #                 Encoding = None
    #                 ItemSize = None
    #                 type = None
    #                 if mode != '"LINES"':
    #                     Indices = ys.get(b, '"Indices"')
    #                     if Indices:
    #                         values = ys.values(Indices[0].data, ':')
    #                         ItemSize = ys.getValue(values, '"ItemSize"', 'i')
    #                         Uint32Array = ys.get(Indices[0], '"Uint32Array"')
    #                         type = "Uint32Array"
    #                         print("DrawElementsUInt", type)
    #                         if Uint32Array:
    #                             values = ys.values(Uint32Array[0].data, ':')
    #                             Size = ys.getValue(values, '"Size"', 'i')
    #                             Offset = ys.getValue(values, '"Offset"', 'i')
    #                             Encoding = ys.getValue(values, '"Encoding"', '""')
    #                             #write(log, ['Indice:', 'mode:', mode, type, 'Size:', Size,'Offset:', Offset, 'Encoding:', Encoding, 'magic:', magic], n)
    #                             if Encoding == 'varint':
    #                                 path = os.path.dirname(
    #                                     ys.filename)+os.sep+"model_file.bin.gz.txt"
    #                                 if os.path.exists(path) == False:
    #                                     path = os.path.dirname(
    #                                         ys.filename)+os.sep+"model_file.bin"
    #                                 if os.path.exists(path) == False:
    #                                     path = os.path.dirname(
    #                                         ys.filename)+os.sep+values['"File"'].split('"')[1]  # +'.txt'
    #                                 if os.path.exists(path) == True:
    #                                     file = open(path, 'rb')
    #                                     g = BinaryReader(file)
    #                                     magic, indiceList = self.getIndices(ItemSize, Size, Offset, type, g, mode, magic)
    #                                     indiceArray.append([indiceList, mode])
    #                                     file.close()
    #                 else:
    #                     print('LINES')

    #             if '"DrawElementsUShort"' in b.header:
    #                 values = ys.values(b.data, ':')
    #                 mode = values['"Mode"']
    #                 Size = None
    #                 Offset = None
    #                 Encoding = None
    #                 ItemSize = None
    #                 type = None
    #                 if mode != '"LINES"':
    #                     Indices = ys.get(b, '"Indices"')
    #                     if Indices:
    #                         values = ys.values(Indices[0].data, ':')
    #                         ItemSize = ys.getValue(values, '"ItemSize"', 'i')
    #                         Uint16Array = ys.get(Indices[0], '"Uint16Array"')
    #                         type = "Uint16Array"
    #                         print("DrawElementsUShort", type)
    #                         if Uint16Array:
    #                             values = ys.values(Uint16Array[0].data, ':')
    #                             Size = ys.getValue(values, '"Size"', 'i')
    #                             Offset = ys.getValue(values, '"Offset"', 'i')
    #                             Encoding = ys.getValue(values, '"Encoding"', '""')
    #                             #write(log, ['Indice:', 'mode:', mode, type, 'Size:', Size, 'Offset:', Offset, 'Encoding:', Encoding, 'magic:', magic], n)
    #                             print(Encoding)
    #                             if Encoding == 'varint':
    #                                 path = os.path.dirname(
    #                                     ys.filename)+os.sep+"model_file.bin.gz.txt"
    #                                 if os.path.exists(path) == False:
    #                                     path = os.path.dirname(
    #                                         ys.filename)+os.sep+"model_file.bin"
    #                                 if os.path.exists(path) == False:
    #                                     path = os.path.dirname(
    #                                         ys.filename)+os.sep+values['"File"'].split('"')[1]  # +'.txt'
    #                                 if os.path.exists(path) == True:
    #                                     file = open(path, 'rb')
    #                                     g = BinaryReader(file)
    #                                     magic, indiceList = self.getIndices(
    #                                         ItemSize, Size, Offset, type, g, mode, magic)
    #                                     indiceArray.append([indiceList, mode])
    #                                     file.close()
    #                             else:
    #                                 path = os.path.dirname(
    #                                     ys.filename)+os.sep+"model_file.bin.gz.txt"
    #                                 if os.path.exists(path) == False:
    #                                     path = os.path.dirname(
    #                                         ys.filename)+os.sep+"model_file.bin"
    #                                 if os.path.exists(path) == False:
    #                                     path = os.path.dirname(
    #                                         ys.filename)+os.sep+values['"File"'].split('"')[1]  # +'.txt'
    #                                 if os.path.exists(path) == True:
    #                                     file = open(path, 'rb')
    #                                     g = BinaryReader(file)
    #                                     g.seek(Offset)
    #                                     indiceList = g.H(ItemSize*Size)
    #                                     indiceArray.append([indiceList, mode])
    #                                     file.close()
    #                 else:
    #                     print('LINES')

    #             if '"DrawElementsUByte"' in b.header:
    #                 values = ys.values(b.data, ':')
    #                 mode = values['"Mode"']
    #                 Size = None
    #                 Offset = None
    #                 Encoding = None
    #                 ItemSize = None
    #                 type = None
    #                 if mode != '"LINES"':
    #                     Indices = ys.get(b, '"Indices"')
    #                     if Indices:
    #                         values = ys.values(Indices[0].data, ':')
    #                         ItemSize = ys.getValue(values, '"ItemSize"', 'i')
    #                         Uint8Array = ys.get(Indices[0], '"Uint8Array"')
    #                         type = "Uint8Array"
    #                         print("DrawElementsUByte", type)
    #                         if Uint8Array:
    #                             values = ys.values(Uint8Array[0].data, ':')
    #                             Size = ys.getValue(values, '"Size"', 'i')
    #                             Offset = ys.getValue(values, '"Offset"', 'i')
    #                             Encoding = ys.getValue(values, '"Encoding"', '""')
    #                             #write(log, ['Indice:', 'mode:', mode, type, 'Size:', Size, 'Offset:', Offset, 'Encoding:', Encoding, 'magic:', magic], n)
    #                             path = os.path.dirname(
    #                                 ys.filename)+os.sep+"model_file.bin.gz.txt"
    #                             if os.path.exists(path) == False:
    #                                 path = os.path.dirname(
    #                                     ys.filename)+os.sep+"model_file.bin"
    #                             if os.path.exists(path) == False:
    #                                 path = os.path.dirname(
    #                                     ys.filename)+os.sep+values['"File"'].split('"')[1]  # +'.txt'
    #                             if os.path.exists(path) == True:
    #                                 file = open(path, 'rb')
    #                                 g = BinaryReader(file)
    #                                 magic, indiceList = self.getIndices(
    #                                     ItemSize, Size, Offset, type, g, mode, magic)
    #                                 indiceArray.append([indiceList, mode])
    #                                 file.close()
    #                 else:
    #                     print('LINES')

    #     return indiceArray

    # def getGeometry(self, ys, parent, n):
    #     print('#'*50, 'Geometry')
    #     n += 4
    #     mode = None
    #     indiceArray = []
    #     vertexArray = []
    #     texArray = []
    #     atributes = {}

    #     #write(log, ['Geometry'], n)
    #     PrimitiveSetList = ys.get(parent, '"PrimitiveSetList"')
    #     if PrimitiveSetList:
    #         indiceArray = self.getPrimitiveSetList(ys, PrimitiveSetList, n)

    #     UserDataContainer = ys.get(parent, '"UserDataContainer"')
    #     if UserDataContainer:
    #         for UserData in UserDataContainer:
    #             Values = ys.get(UserData, '"Values"')
    #             if Values:
    #                 for a in Values[0].children:
    #                     values = ys.values(a.data, ':')
    #                     Name = ys.getValue(values, '"Name"', '""')
    #                     Value = ys.getValue(values, '"Value"', '""')
    #                     #if Name:write(log,[Name,Value],n+4)
    #                     if Name:
    #                         atributes[Name] = Value

    #     VertexAttributeList = ys.get(parent, '"VertexAttributeList"')
    #     if VertexAttributeList:
    #         vertexArray, texArray = self.getVertexAttributeList(ys, VertexAttributeList, n)

    #     # print atributes
    #     mesh = Mesh()
    #     if len(indiceArray) > 0:
    #         for [indices, mode] in indiceArray:
    #             print(mode, len(indices))
    #             mat = Mat()
    #             mesh.matList.append(mat)
    #             mat.IDStart = len(mesh.indiceList)
    #             mat.IDCount = len(indices)
    #             mesh.indiceList.extend(indices)
    #             if mode == '"TRIANGLE_STRIP"':
    #                 mat.TRISTRIP = True
    #             if mode == '"TRIANGLES"':
    #                 mat.TRIANGLE = True

    #         indices = indiceArray[0][0]
    #         mode = indiceArray[0][1]
    #         if len(vertexArray) == 1:
    #             if vertexArray[0][1] == '"varint"':
    #                 bytes = vertexArray[0][0]
    #                 ItemSize = vertexArray[0][2]
    #                 if mode == '"TRIANGLE_STRIP"':
    #                     bytes = self.decodePredict(indices, bytes, ItemSize)
    #                 s1 = float(atributes['vtx_bbl_x'])
    #                 s2 = float(atributes['vtx_bbl_y'])
    #                 s3 = float(atributes['vtx_bbl_z'])
    #                 s = [s1, s2, s3]
    #                 a1 = float(atributes['vtx_h_x'])
    #                 a2 = float(atributes['vtx_h_y'])
    #                 a3 = float(atributes['vtx_h_z'])
    #                 a = [a1, a2, a3]
    #                 floats = self.decodeQuantize(bytes, s, a, ItemSize)
    #                 mesh.vertPosList = [floats[m:m+ItemSize]
    #                                     for m in range(0, len(floats), 3)]
    #             else:
    #                 list = vertexArray[0][0]
    #                 mesh.vertPosList = list

    #         if len(texArray) == 1:
    #             if texArray[0][1] == '"varint"':
    #                 bytes = texArray[0][0]
    #                 ItemSize = texArray[0][2]
    #                 if mode == '"TRIANGLE_STRIP"':
    #                     bytes = self.decodePredict(indices, bytes, ItemSize)
    #                 s1 = float(atributes['uv_0_bbl_x'])
    #                 s2 = float(atributes['uv_0_bbl_y'])
    #                 s = [s1, s2]
    #                 a1 = float(atributes['uv_0_h_x'])
    #                 a2 = float(atributes['uv_0_h_y'])
    #                 a = [a1, a2]
    #                 floats = self.decodeQuantize(bytes, s, a, ItemSize)
    #                 for m in range(0, len(floats), ItemSize):
    #                     u, v = floats[m:m+ItemSize]
    #                     mesh.vertUVList.append([u, 1-v])

    #             else:
    #                 list = texArray[0][0]
    #                 mesh.vertUVList = list

    #     return mesh


    # def getMatrixTransform(self, ys, parent, n, boneParent):
    #     #write(log, ['MatrixTransform'], n)
    #     n += 4
    #     bone = Bone()
    #     bone.name = str(len(skeleton.boneList))
    #     skeleton.boneList.append(bone)
    #     bone.parentName = boneParent.name

    #     Name = None
    #     for child in parent.children:
    #         values = ys.values(child.header, ':')
    #         Name = ys.getValue(values, '"Name"', '""')
    #         if Name:
    #             Name = self.getSplitName(Name, '_', -1)
    #             #write(log, [Name], n)
    #             #if len(Name)<25:bone.name=Name
    #             boneIndeksList[Name] = bone.name

    #     for child in parent.children:
    #         if '"Matrix"' in child.header:
    #             floats = ys.values(child.data, 'f')
    #             #write(log, floats, n)
    #             bone.matrix = Matrix4x4(floats)
    #             bone.matrix *= boneParent.matrix
    #     for child in parent.children:
    #         if '"Children"' in child.header:
    #             self.getChildren(ys, child, n, bone)


    # def getSkeletonNode(self, ys, parent, n, boneParent):
    #     global firstmatrix
    #     #write(log, ['Skeleton'], n)
    #     n += 4
    #     bone = Bone()
    #     bone.name = str(len(skeleton.boneList))
    #     skeleton.boneList.append(bone)
    #     bone.parentName = boneParent.name

    #     firstmatrix = boneParent.matrix

    #     Name = None
    #     for child in parent.children:
    #         values = ys.values(child.header, ':')
    #         Name = ys.getValue(values, '"Name"', '""')
    #         if Name:
    #             Name = self.getSplitName(Name, '_', -1)
    #             # print Name
    #             #write(log, [Name], n)
    #             #if len(Name)<25:bone.name=Name
    #             boneIndeksList[Name] = bone.name

    #     for child in parent.children:
    #         if '"Matrix"' in child.header:
    #             floats = ys.values(child.data, 'f')
    #             #write(log, floats, n)
    #             bone.matrix = Matrix4x4(floats)
    #             bone.matrix *= boneParent.matrix
    #     for child in parent.children:
    #         if '"Children"' in child.header:
    #             self.getChildren(ys, child, n, bone)


    # def getRigGeometryNode(self ,ys, parent, n, boneParent):
    #     #write(log, ['RigGeometry'], n)
    #     mesh = self.getRigGeometry(ys, parent, n)
    #     if len(mesh.vertPosList) > 0:
    #         model.meshList.append(mesh)
    #         mesh.matrix = boneParent.matrix

    #     n += 4
    #     for child in parent.children:
    #         if '"Children"' in child.header:
    #             self.getChildren(ys, child, n, boneParent)


    # def getGeometryNode(self, ys, parent, n, boneParent):
    #     #write(log, ['Geometry'], n)
    #     mesh = self.getGeometry(ys, parent, n)
    #     if len(mesh.vertPosList) > 0:
    #         model.meshList.append(mesh)
    #         mesh.matrix = boneParent.matrix

    #     n += 4
    #     for child in parent.children:
    #         if '"Children"' in child.header:
    #             self.getChildren(ys, child, n, boneParent)


    # def getBoneNode(self, ys, parent, n, boneParent):
    #     #write(log, ['Bone'], n)
    #     bone = Bone()
    #     bone.parentName = boneParent.name
    #     bone.name = str(len(skeleton.boneList))
    #     skeleton.boneList.append(bone)

    #     n += 4
    #     Name = None
    #     for child in parent.children:
    #         values = ys.values(child.header, ':')
    #         # print child.header
    #         Name = ys.getValue(values, '"Name"', '""')
    #         if Name:
    #             Name = self.getSplitName(Name, '_', -1)
    #             #write(log, [Name], n)
    #             # print Name
    #             #if len(Name)<25:bone.name=Name
    #             boneIndeksList[Name] = bone.name

    #     for child in parent.children:
    #         if '"Matrix"' in child.header:
    #             values = ys.values(child.header, ':')
    #             floats = ys.values(child.data, 'f')
    #             bone.matrix = Matrix4x4(floats)
    #             bone.matrix *= boneParent.matrix

    #         if '"InvBindMatrixInSkeletonSpace"' in child.header:
    #             bindbone = Bone()
    #             #if Name:bindbone.name=Name
    #             bindbone.name = bone.name
    #             bindskeleton.boneList.append(bindbone)
    #             floats = ys.values(child.data, 'f')
    #             #write(log, [floats], n+4)
    #             matrix = Matrix4x4(floats).invert()
    #             bindbone.matrix = matrix*firstmatrix

    #     for child in parent.children:
    #         if '"Children"' in child.header:
    #             self.getChildren(ys, child, n, bone)


    # def getChildren(self, ys, parent, n, boneParent):
    #     #write(log, ['Children'], n)
    #     n += 4
    #     for child in parent.children:
    #         for a in child.children:
    #             if '"osg.MatrixTransform"' in a.header:
    #                 self.getMatrixTransform(ys, a, n, boneParent)
    #             if '"osg.Node"' in a.header:
    #                 self.getNode(ys, a, n, boneParent)
    #             if '"osgAnimation.Skeleton"' in a.header:
    #                 self.getSkeletonNode(ys, a, n, boneParent)
    #             if '"osgAnimation.RigGeometry"' in a.header:
    #                 self.getRigGeometryNode(ys, a, n, boneParent)
    #             if '"osg.Geometry"' in a.header:
    #                 self.getGeometryNode(ys, a, n, boneParent)
    #             if '"osgAnimation.Bone"' in a.header:
    #                 self.getBoneNode(ys, a, n, boneParent)


    # def getNode(self, ys, parent, n, boneParent):
    #     #write(log, ['Node'], n)
    #     n += 4

    #     bone = Bone()
    #     bone.name = str(len(skeleton.boneList))
    #     skeleton.boneList.append(bone)
    #     bone.parentName = boneParent.name
    #     bone.matrix = boneParent.matrix

    #     Name = None
    #     for child in parent.children:
    #         values = ys.values(child.header, ':')
    #         Name = ys.getValue(values, '"Name"', '""')
    #         if Name:
    #             # Name=getSplitName(Name,'_',-1)
    #             #¶write(log, [Name], n)
    #             #if len(Name)<25:bone.name=Name
    #             boneIndeksList[Name] = bone.name

    #     for child in parent.children:
    #         if '"Children"' in child.header:
    #             self.getChildren(ys, child, n, bone)


    # def bindPose(self, bindSkeleton, poseSkeleton, meshObject):
    #     # print 'BINDPOSE'
    #     mesh = meshObject.getData(mesh=1)
    #     poseBones = poseSkeleton.getData().bones
    #     bindBones = bindSkeleton.getData().bones
    #     # mesh.transform(meshObject.matrixWorld)
    #     mesh.update()
    #     for vert in mesh.verts:
    #         index = vert.index
    #         skinList = mesh.getVertexInfluences(index)
    #         vco = vert.co.copy()*meshObject.matrixWorld
    #         vector = Vector()
    #         sum = 0
    #         for skin in skinList:
    #             bone = skin[0]
    #             weight = skin[1]
    #             if bone in list(bindBones.keys()) and bone in list(poseBones.keys()):
    #                 matA = bindBones[bone].matrix['ARMATURESPACE'] * \
    #                     bindSkeleton.matrixWorld
    #                 matB = poseBones[bone].matrix['ARMATURESPACE'] * \
    #                     poseSkeleton.matrixWorld
    #                 vector += vco*matA.invert()*matB*weight
    #                 sum += weight
    #             else:
    #                 vector = vco
    #                 break
    #         vert.co = vector
    #     mesh.update()
    #     Blender.Window.RedrawAll()


    def __init__(self, filename):
        global skeleton, bindskeleton, model, boneIndeksList, firstmatrix
        boneIndeksList = {}
        # model = Model(filename)
        # skeleton = Skeleton()
        # skeleton.ARMATURESPACE = True
        # bindskeleton = Skeleton()
        # bindskeleton.NICE = True
        # bindskeleton.ARMATURESPACE = True
        ys = Yson()
        ys.log = True
        ys.filename = filename
        ys.parse()

        # firstmatrix = Matrix4x4([1, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 1])

        # n = 0
        # bone = Bone()
        # bone.matrix = Matrix().resize4x4()
        # bone.name = str(len(skeleton.boneList))
        # bone.name = 'scene'
        # skeleton.boneList.append(bone)
        # Node = ys.get(ys.root, '"osg.Node"')
        # if Node:
        #     self.getNode(ys, Node[0], n, bone)
        # if len(bindskeleton.boneList) > 0:
        #     bindskeleton.draw()

        # for mesh in model.meshList:
        #     if len(mesh.skinList) > 0:
        #         for map in mesh.BoneMap:
        #             if map == 0:
        #                 break
        #             mesh.boneNameList.append(boneIndeksList[map])

        # for mesh in model.meshList:
        #     if len(mesh.skinList) > 0:
        #         skeleton.NICE = True
        #         skeleton.draw()
        #         break

        # for mesh in model.meshList:
        #     mesh.draw()
        #     if mesh.object:
        #         if len(mesh.skinList) > 0:
        #             if BINDPOSE == 1:
        #                 if bindskeleton.object and skeleton.object:
        #                     mesh.object.getData(mesh=1).transform(mesh.matrix)
        #                     mesh.object.getData(mesh=1).update()
        #                     # mesh.object.setMatrix(mesh.matrix)
        #                     self.bindPose(bindskeleton.object, skeleton.object, mesh.object)
        #                     # mesh.object.setMatrix(mesh.matrix.invert()*mesh.object.matrixWorld)
        #                     scene = bpy.data.scenes.active
        #                     scene.objects.unlink(bindskeleton.object)
        #             else:
        #                 if bindskeleton.object and skeleton.object:
        #                     mesh.object.getData(mesh=1).transform(mesh.matrix)
        #                     mesh.object.getData(mesh=1).update()

        #         else:
        #             mesh.object.setMatrix(mesh.matrix)

        # n = 0
        # Animations = ys.get(ys.root, '"osgAnimation.Animationnnnn"')
        # TODO: reenable animations!
        # if Animations:
        #     for animation in Animations:
        #         getAnimation(ys, animation, n)
