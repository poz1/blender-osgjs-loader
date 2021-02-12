
def isQuat(quat):
        sum = quat[0]**2+quat[1]**2+quat[2]**2+quat[3]**2
        return sum


def quatDecompress3(s0, s1, s2):
        tmp0 = s0 >> 15
        tmp1 = (s1*2+tmp0) & 0x7FFF
        s0 = s0 & 0x7FFF;
        tmp2 = s2*4;
        tmp2 = (s2*4 + (s1 >> 14)) & 0x7FFF;
        s1 = tmp1;
        AxisFlag = s2 >> 13;
        # AxisFlag = ((s1 & 1) << 1) | (s2 & 1)
        s2 = tmp2;
        f0 = 1.41421*(s0-0x3FFF)/0x7FFF
        f1 = 1.41421*(s1-0x3FFF)/0x7FFF
        f2 = 1.41421*(s2-0x3FFF)/0x7FFF;
        f3 = sqrt(1.0-(f0*f0+f1*f1+f2*f2))
        # print AxisFlag
        if AxisFlag == 3:
            x = f2
            y = f1
            z = f0
            w = f3
        if AxisFlag == 2:
            x = f2; y = f1; z = f3; w = f0
        if AxisFlag == 1: x = f2; y = f3; z = f1; w = f0
        if AxisFlag == 0:
            x = f3; y = f2; z = f1; w = f0
        # print x,y,z,w
        return x, y, z, w


def quatDecompress(s0, s1, s2):
        tmp0 = s0 >> 15
        tmp1 = (s1*2+tmp0) & 0x7FFF
        s0 = s0 & 0x7FFF;
        tmp2 = s2*4;
        tmp2 = (s2*4 + (s1 >> 14)) & 0x7FFF;
        s1 = tmp1;
        AxisFlag = s2 >> 13;
        # AxisFlag = ((s1 & 1) << 1) | (s2 & 1)
        s2 = tmp2;
        f0 = 1.41421*(s0-0x3FFF)/0x7FFF
        f1 = 1.41421*(s1-0x3FFF)/0x7FFF
        f2 = 1.41421*(s2-0x3FFF)/0x7FFF;
        f3 = sqrt(1.0-(f0*f0+f1*f1+f2*f2))
        # print AxisFlag
        if AxisFlag == 3:
            x = f2
            y = f1
            z = f0
            w = f3
        if AxisFlag == 2:
            x = f2; y = f1; z = f3; w = f0
        if AxisFlag == 1: x = f2; y = f3; z = f1; w = f0
        if AxisFlag == 0:
            x = f3; y = f2; z = f1; w = f0
        # print x,y,z,w
        return x, y, z, w

def QuatMatrix(quat):
        return Quaternion(quat[3], quat[0],quat[1],quat[2]).toMatrix()	

def VectorMatrix(vector):
        return TranslationMatrix(Vector(vector))


def roundVector(vec, dec=17):
        fvec = []
        for v in vec:
            fvec.append(round(v, dec))
        return Vector(fvec)


def roundMatrix(mat, dec=17):
        fmat = []
        for row in mat:
            fmat.append(roundVector(row, dec))
        return Matrix(*fmat)

def Matrix4x4(data):
        return Matrix(data[:4],\
                        data[4:8],
                        data[8:12],
                        data[12:16])

def Matrix3x3(data):
        return Matrix(data[:3],\
                        data[3:6],
                        data[6:9])

def Matrix4x3(data):
        # print data
        data = list(data)
        return Matrix(data[:3]+[0.0],\
                        data[3:6]+[0.0],
                        data[6:9]+[0.0],
                        data[9:12]+[1.0])

def VectorScaleMatrix(scale):
        mat = Blender.Mathutils.Matrix(
            [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            )
        mat *= Blender.Mathutils.ScaleMatrix(scale[0], 4, Blender.Mathutils.Vector([1, 0, 0]))
        mat *= Blender.Mathutils.ScaleMatrix(scale[1], 4, Blender.Mathutils.Vector([0, 1, 0]))
        mat *= Blender.Mathutils.ScaleMatrix(scale[2], 4, Blender.Mathutils.Vector([0, 0, 1]))
        return mat

def ParseID():
		#0-0-0 - oznacza kolejno meshID - matID - objectID
		ids = []
		objectID=0
		modelID=0
		matID=0
		scene = bpy.data.scenes.active
		
		#for meshID
		for object in scene.objects:
			if object.getType()=='Mesh':
				try:
					meshID = int(object.getData(mesh=1).name.split('-')[0])
					ids.append(meshID)
				except:pass 
		try:
			meshID = max(ids)+1
		except:
			meshID = 0
		return meshID
