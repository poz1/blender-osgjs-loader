from newGameLib import *
import bpy


def etap1(input, ItemSize):
    n = len(input)/ItemSize
    r = 0
    output = [0]*len(input)
    while(r < n):
        a = r*ItemSize
        s = 0
        while(s < ItemSize):
            output[a+s] = input[r+n*s]
            s += 1
        r += 1
    return output


def etap2(input, ItemSize, atributes):
    i = [atributes['"bx"'], atributes['"by"'], atributes['"bz"']]
    n = [atributes['"hx"'], atributes['"hy"'], atributes['"hz"']]
    # start=[atributes['"ox"'],atributes['"oy"'],atributes['"oz"']]

    a = len(input)/ItemSize
    s = 0
    output = [0]*len(input)
    while(s < a):
        o = s*ItemSize
        u = 0
        while(u < ItemSize):
            output[o+u] = i[u]+input[o+u]*n[u]
            u += 1
        s += 1

    # start.extend(output)
    # start[0]=atributes['"ot"']
    return output


def etap3(input, ItemSize):
    i = ItemSize | 1
    n = 1
    r = len(input)/i
    while(n < r):
        a = (n-1)*i
        s = n*i
        o = 0
        while(o < i):
            input[s+o] += input[a+o]
            o += 1
        n += 1
    return input


def etap4(input):
    e = 1
    i = len(input)/4
    while(e < i):
        n = 4*(e-1)
        r = 4*e
        a = input[n]
        s = input[n+1]
        o = input[n+2]
        u = input[n+3]
        l = input[r]
        h = input[r+1]
        c = input[r+2]
        d = input[r+3]
        input[r] = a*d+s*c-o*h+u*l
        input[r+1] = -a*c+s*d+o*l+u*h
        input[r+2] = a*h-s*l+o*d+u*c
        input[r+3] = -a*l-s*h-o*c+u*d
        e += 1
    return input


def int3float4(input, atributes, ItemSize):
    c = 4
    d = atributes['"epsilon"']
    p = int(atributes['"nphi"'])
    e = [0]*len(input)*4
    i = 1.57079632679
    n = 6.28318530718
    r = 3.14159265359
    a = .01745329251
    s = .25
    o = 720
    u = 832
    l = 47938362584151635e-21
    h = {}
    f = True

    d = d or s
    p = p or o
    g = math.cos(d*a)
    m = 0
    v = 0
    _ = []

    v = (p+1)*(u+1)*3
    _ = [None]*v

    b = r/float(p-1)
    x = i/float(p-1)

    if f:
        y = 3
    else:
        y = 2

    m = 0
    v = len(input)/y
    while(m < v):
        A = m*c
        S = m*y
        C = input[S]
        w = input[S+1]
        if c == 0:
            if f == 0:
                if (C & -1025) != 4:
                    e[A+3] = -1
                else:
                    e[A+3] = 1
        M = None
        T = None
        E = None
        I = 3*(C+p*w)
        M = _[I]
        if M == None:
            N = C*b
            k = cos(N)
            F = sin(N)
            N += x
            D = (g-k*cos(N))/float(max(1e-5, F*sin(N)))
            if D > 1:
                D = 1
            else:
                if D < -1:
                    D = -1
            P = w*n/float(math.ceil(r/float(max(1e-5, math.acos(D)))))
            M = _[I] = F*math.cos(P)
            T = _[I+1] = F*math.sin(P)
            E = _[I+2] = k
        else:
            T = _[I+1]
            E = _[I+2]
        if f:
            R = input[S+2]*l
            O = math.sin(R)
            e[A] = O*M
            e[A+1] = O*T
            e[A+2] = O*E
            e[A+3] = math.cos(R)
            # write(log,[A,e[A],e[A+1],e[A+2],e[A+3]],0)
        else:
            e[A] = M
            e[A+1] = T
            e[A+2] = E
        m += 1

    # write(log,_,0)
    return e




def getAnimation(ys, A, n):
    action = Action()
    action.ARMATURESPACE = True
    action.BONESORT = True
    action.skeleton = skeleton.name
    n += 4
    Channels = ys.get(A, '"Channels"')
    boneList = {}
    if Channels:
        values = ys.values(Channels[0].header, ':')
        Name = ys.getValue(values, '"Name"')
        action.name = Name
        write(log, [Name], n)

        for a in Channels[0].children:
            write(log, ['Bone'], n)
            Vec3LerpChannel = ys.get(a, '"osgAnimation.Vec3LerpChannel"')
            bone = None
            if Vec3LerpChannel:
                KeyFrames = ys.get(a, '"KeyFrames"')
                if KeyFrames:
                    values = ys.values(KeyFrames[0].header, ':')
                    Name = ys.getValue(values, '"Name"')
                    TargetName = ys.getValue(values, '"TargetName"', '""')
                    write(log, ['Vec3LerpChannel:', Name,
                                'TargetName:', TargetName], n+4)
                    name = getSplitName(TargetName, '_', -1)
                    if Name == '"translate"':
                        if name in boneIndeksList:
                            name = boneIndeksList[name]
                            if name not in list(boneList.keys()):
                                bone = ActionBone()
                                action.boneList.append(bone)
                                bone.name = name
                                boneList[name] = bone
                            bone = boneList[name]

                        Key = ys.get(a, '"Key"')
                        if Key:
                            values = ys.values(Key[0].data, ':')
                            ItemSize = ys.getValue(values, '"ItemSize"', 'i')
                            Float32Array = ys.get(Key[0], '"Float32Array"')
                            if Float32Array:
                                values = ys.values(Float32Array[0].data, ':')
                                File = ys.getValue(values, '"File"')
                                Size = ys.getValue(values, '"Size"')
                                Offset = ys.getValue(values, '"Offset"')
                                write(
                                    log, [File, 'Size:', Size, 'Offset:', Offset, 'ItemSize:', ItemSize], n+4)
                                path = os.path.dirname(
                                    input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                                if os.path.exists(path):
                                    file = open(path, 'rb')
                                    g = BinaryReader(file)
                                    g.seek(int(Offset))
                                    for m in range(int(Size)):
                                        value = g.f(ItemSize)
                                        write(log, value, n+8)
                                        if bone:
                                            boneMatrix = skeleton.object.getData(
                                            ).bones[bone.name].matrix['ARMATURESPACE']
                                            bone.posKeyList.append(
                                                boneMatrix*VectorMatrix(value))
                                    file.close()

                        Time = ys.get(a, '"Time"')
                        if Time:
                            values = ys.values(Time[0].data, ':')
                            ItemSize = ys.getValue(values, '"ItemSize"', 'i')
                            Float32Array = ys.get(Time[0], '"Float32Array"')
                            if Float32Array:
                                values = ys.values(Float32Array[0].data, ':')
                                File = ys.getValue(values, '"File"')
                                Size = ys.getValue(values, '"Size"')
                                Offset = ys.getValue(values, '"Offset"')
                                write(
                                    log, [File, 'Size:', Size, 'Offset:', Offset, 'ItemSize:', ItemSize], n+4)
                                path = os.path.dirname(
                                    input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                                if os.path.exists(path):
                                    file = open(path, 'rb')
                                    g = BinaryReader(file)
                                    g.seek(int(Offset))
                                    for m in range(int(Size)):
                                        value = g.f(ItemSize)
                                        if ItemSize == 1:
                                            value = value[0]
                                        # write(log,[value],n+8)
                                        if bone:
                                            bone.posFrameList.append(
                                                int(value*33))
                                    file.close()

            Vec3LerpChannelCompressedPacked = ys.get(
                a, '"osgAnimation.Vec3LerpChannelCompressedPacked"')
            if Vec3LerpChannelCompressedPacked:

                atributes = {}
                UserDataContainer = ys.get(
                    Vec3LerpChannelCompressedPacked[0], '"UserDataContainer"')
                if UserDataContainer:
                    Values = ys.get(UserDataContainer[0], '"Values"')
                    if Values:
                        for child in Values[0].children:
                            values = ys.values(child.data, ':')
                            Name = ys.getValue(values, '"Name"')
                            Value = ys.getValue(values, '"Value"', '"f"')
                            # write(log,[Name,Value],n+4)
                            atributes[Name] = Value

                KeyFrames = ys.get(a, '"KeyFrames"')
                if KeyFrames:
                    values = ys.values(KeyFrames[0].header, ':')
                    Name = ys.getValue(values, '"Name"')
                    TargetName = ys.getValue(values, '"TargetName"', '""')
                    write(log, ['Vec3LerpChannelCompressedPacked:',
                                Name, 'TargetName:', TargetName], n+4)
                    name = getSplitName(TargetName, '_', -1)
                    if Name == '"translate"':
                        if name in boneIndeksList:
                            name = boneIndeksList[name]
                            if name not in list(boneList.keys()):
                                bone = ActionBone()
                                action.boneList.append(bone)
                                bone.name = name
                                boneList[name] = bone
                            bone = boneList[name]

                        Key = ys.get(a, '"Key"')
                        if Key:
                            values = ys.values(Key[0].data, ':')
                            ItemSize = int(ys.getValue(values, '"ItemSize"'))
                            Uint16Array = ys.get(Key[0], '"Uint16Array"')
                            type = "Uint16Array"
                            if Uint16Array:
                                values = ys.values(Uint16Array[0].data, ':')
                                File = ys.getValue(values, '"File"')
                                Size = int(ys.getValue(values, '"Size"'))
                                Offset = int(ys.getValue(values, '"Offset"'))
                                Encoding = ys.getValue(values, '"Encoding"')
                                write(log, [File, 'Size:', Size, 'Offset:', Offset,
                                            'Encoding:', Encoding, 'ItemSize:', ItemSize], n+4)
                                path = os.path.dirname(
                                    input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                                if os.path.exists(path):
                                    file = open(path, 'rb')
                                    g = BinaryReader(file)

                                    list = decodeVarint(
                                        g, Offset, Size*ItemSize, type)
                                    list1 = etap1(list, ItemSize)
                                    out = etap2(list1, ItemSize, atributes)
                                    list2 = [atributes['"ox"'],
                                             atributes['"oy"'], atributes['"oz"']]
                                    list2.extend(out)
                                    list3 = etap3(list2, ItemSize)
                                    for m in range(Size+1):
                                        value = list3[m*3:m*3+3]
                                        write(log, value, n+8)
                                        if bone:
                                            boneMatrix = skeleton.object.getData(
                                            ).bones[bone.name].matrix['ARMATURESPACE']
                                            bone.posKeyList.append(
                                                boneMatrix*VectorMatrix(value))
                                    file.close()

                        Time = ys.get(a, '"Time"')
                        if Time:
                            values = ys.values(Time[0].data, ':')
                            ItemSize = ys.getValue(values, '"ItemSize"', 'i')
                            Float32Array = ys.get(Time[0], '"Float32Array"')
                            if Float32Array:
                                values = ys.values(Float32Array[0].data, ':')
                                File = ys.getValue(values, '"File"')
                                Size = ys.getValue(values, '"Size"', 'i')
                                Offset = ys.getValue(values, '"Offset"', 'i')
                                write(
                                    log, [File, 'Size:', Size, 'Offset:', Offset, 'ItemSize:', ItemSize], n+4)
                                path = os.path.dirname(
                                    input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                                if os.path.exists(path):
                                    file = open(path, 'rb')
                                    g = BinaryReader(file)
                                    g.seek(int(Offset))
                                    list = g.f(Size*ItemSize)
                                    list1 = etap1(list, ItemSize)
                                    # out=etap2(list1,ItemSize,atributes)
                                    list2 = [atributes['"ot"']]
                                    list2.extend(list1)
                                    list3 = etap3(list2, ItemSize)
                                    # write(log,list3,0)
                                    for m in range(Size+1):
                                        value = list3[m]
                                        if bone:
                                            bone.posFrameList.append(
                                                int(value*33))
                                    file.close()

            QuatSlerpChannel = ys.get(a, '"osgAnimation.QuatSlerpChannel"')
            if QuatSlerpChannel:
                KeyFrames = ys.get(a, '"KeyFrames"')
                if KeyFrames:
                    values = ys.values(KeyFrames[0].header, ':')
                    Name = ys.getValue(values, '"Name"')
                    TargetName = ys.getValue(values, '"TargetName"', '""')
                    write(log, ['QuatSlerpChannel:', Name,
                                'TargetName:', TargetName], n+4)
                    name = getSplitName(TargetName, '_', -1)
                    if name in boneIndeksList:
                        name = boneIndeksList[name]
                        if name not in list(boneList.keys()):
                            bone = ActionBone()
                            action.boneList.append(bone)
                            bone.name = name
                            boneList[name] = bone
                        bone = boneList[name]

                    Key = ys.get(a, '"Key"')
                    if Key:
                        values = ys.values(Key[0].data, ':')
                        ItemSize = ys.getValue(values, '"ItemSize"')
                        Float32Array = ys.get(Key[0], '"Float32Array"')
                        if Float32Array:
                            values = ys.values(Float32Array[0].data, ':')
                            File = ys.getValue(values, '"File"')
                            Size = ys.getValue(values, '"Size"')
                            Offset = ys.getValue(values, '"Offset"')
                            write(log, [File, 'Size:', Size, 'Offset:',
                                        Offset, 'ItemSize:', ItemSize], n+4)
                            path = os.path.dirname(
                                input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                            if os.path.exists(path):
                                file = open(path, 'rb')
                                g = BinaryReader(file)
                                g.seek(int(Offset))
                                for m in range(int(Size)):
                                    value = g.f(4)
                                    value = Quaternion(value)
                                    if bone:
                                        boneMatrix = skeleton.object.getData(
                                        ).bones[bone.name].matrix['ARMATURESPACE']
                                        bone.rotKeyList.append(
                                            boneMatrix*QuatMatrix(value).resize4x4())
                                file.close()

                    Time = ys.get(a, '"Time"')
                    if Time:
                        values = ys.values(Time[0].data, ':')
                        ItemSize = ys.getValue(values, '"ItemSize"', 'i')
                        Float32Array = ys.get(Time[0], '"Float32Array"')
                        if Float32Array:
                            values = ys.values(Float32Array[0].data, ':')
                            File = ys.getValue(values, '"File"')
                            Size = ys.getValue(values, '"Size"')
                            Offset = ys.getValue(values, '"Offset"')
                            write(log, [File, 'Size:', Size, 'Offset:',
                                        Offset, 'ItemSize:', ItemSize], n+4)
                            path = os.path.dirname(
                                input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                            if os.path.exists(path):
                                file = open(path, 'rb')
                                g = BinaryReader(file)
                                g.seek(int(Offset))
                                for m in range(int(Size)):
                                    value = g.f(ItemSize)
                                    if ItemSize == 1:
                                        value = value[0]
                                    if bone:
                                        bone.rotFrameList.append(int(value*33))
                                file.close()

            QuatSlerpChannelCompressedPacked = ys.get(
                a, '"osgAnimation.QuatSlerpChannelCompressedPacked"')
            if QuatSlerpChannelCompressedPacked:

                atributes = {}
                UserDataContainer = ys.get(
                    QuatSlerpChannelCompressedPacked[0], '"UserDataContainer"')
                if UserDataContainer:
                    Values = ys.get(UserDataContainer[0], '"Values"')
                    if Values:
                        for child in Values[0].children:
                            values = ys.values(child.data, ':')
                            Name = ys.getValue(values, '"Name"')
                            Value = ys.getValue(values, '"Value"', '"f"')
                            # write(log,[Name,Value],n+4)
                            atributes[Name] = Value

                KeyFrames = ys.get(a, '"KeyFrames"')
                if KeyFrames:
                    values = ys.values(KeyFrames[0].header, ':')
                    Name = ys.getValue(values, '"Name"')
                    TargetName = ys.getValue(values, '"TargetName"', '""')
                    write(log, ['QuatSlerpChannelCompressedPacked:',
                                Name, 'TargetName:', TargetName], n+4)
                    name = getSplitName(TargetName, '_', -1)
                    if name in boneIndeksList:
                        name = boneIndeksList[name]
                        if name not in list(boneList.keys()):
                            bone = ActionBone()
                            action.boneList.append(bone)
                            bone.name = name
                            boneList[name] = bone
                        bone = boneList[name]

                    Key = ys.get(a, '"Key"')
                    if Key:
                        values = ys.values(Key[0].data, ':')
                        ItemSize = int(ys.getValue(values, '"ItemSize"'))
                        Uint16Array = ys.get(Key[0], '"Uint16Array"')
                        type = "Uint16Array"
                        if Uint16Array:
                            values = ys.values(Uint16Array[0].data, ':')
                            File = ys.getValue(values, '"File"')
                            Size = int(ys.getValue(values, '"Size"'))
                            Offset = int(ys.getValue(values, '"Offset"'))
                            Encoding = ys.getValue(values, '"Encoding"')
                            write(log, [File, 'Size:', Size, 'Offset:', Offset,
                                        'Encoding:', Encoding, 'ItemSize:', ItemSize], n+4)
                            path = os.path.dirname(
                                input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                            if os.path.exists(path):
                                file = open(path, 'rb')
                                g = BinaryReader(file)

                                list = decodeVarint(
                                    g, Offset, Size*ItemSize, type)
                                # write(log,list,0)
                                list1 = etap1(list, ItemSize)
                                # write(log,list1,0)

                                list2 = int3float4(list1, atributes, ItemSize)
                                # write(log,list2,0)
                                list3 = [atributes['"ox"'], atributes['"oy"'],
                                         atributes['"oz"'], atributes['"ow"']]
                                list3.extend(list2)
                                list4 = etap4(list3)
                                # write(log,list4,0)

                                for m in range(Size+1):
                                    value = list4[m*4:m*4+4]
                                    value = Quaternion(value)
                                    # write(log,value,n+8)
                                    if bone:
                                        boneMatrix = skeleton.object.getData(
                                        ).bones[bone.name].matrix['ARMATURESPACE']
                                        # bone.rotKeyList.append((boneMatrix.rotationPart()*QuatMatrix(value)).resize4x4())
                                        bone.rotKeyList.append(
                                            boneMatrix*QuatMatrix(value).resize4x4())
                                file.close()

                    Time = ys.get(a, '"Time"')
                    if Time:
                        values = ys.values(Time[0].data, ':')
                        ItemSize = ys.getValue(values, '"ItemSize"', 'i')
                        Float32Array = ys.get(Time[0], '"Float32Array"')
                        if Float32Array:
                            values = ys.values(Float32Array[0].data, ':')
                            File = ys.getValue(values, '"File"')
                            Size = ys.getValue(values, '"Size"', 'i')
                            Offset = ys.getValue(values, '"Offset"', 'i')
                            write(log, [File, 'Size:', Size, 'Offset:',
                                        Offset, 'ItemSize:', ItemSize], n+4)
                            path = os.path.dirname(
                                input.filename)+os.sep+File.split('"')[1].split('.gz')[0]
                            if os.path.exists(path):
                                file = open(path, 'rb')
                                g = BinaryReader(file)
                                g.seek(int(Offset))
                                list = g.f(Size*ItemSize)
                                list1 = etap1(list, ItemSize)
                                # out=etap2(list1,ItemSize,atributes)
                                list2 = [atributes['"ot"']]
                                list2.extend(list1)
                                list3 = etap3(list2, ItemSize)
                                # write(log,list3,0)
                                for m in range(Size+1):
                                    value = list2[m]
                                    if bone:
                                        bone.rotFrameList.append(int(value*33))
                                file.close()

            if bone:
                print(name, bone.name)

    action.draw()
    action.setContext()





def getPath(File):
    path = os.path.dirname(input.filename)+os.sep+File.split('.gz')[0]
    if os.path.exists(path) == False:
        path = os.path.dirname(input.filename)+os.sep+File+'.txt'
    if os.path.exists(path) == False:
        path = os.path.dirname(input.filename)+os.sep+File
    if os.path.exists(path) == True:
        return path
    else:
        return None


def getVertexAttributeList(ys, VertexAttributeList, n):
    vertexArray = []
    texArray = []

    Vertex = ys.get(VertexAttributeList[0], '"Vertex"')
    mode = "Vertex"
    for b in Vertex:
        Size = None
        Offset = None
        Encoding = None
        ItemSize = None
        type = None
        values = ys.values(b.data, ':')
        if '"ItemSize"' in values:
            ItemSize = int(values['"ItemSize"'])
            Int32Array = ys.get(b, '"Int32Array"')
            if Int32Array:
                type = 'Int32Array'
                print(mode, type)
                values = ys.values(Int32Array[0].data, ':')
                Size = ys.getValue(values, '"Size"', 'i')
                Offset = ys.getValue(values, '"Offset"', 'i')
                File = ys.getValue(values, '"File"', '""')
                Encoding = ys.getValue(values, '"Encoding"')
                write(log, ['Vertex:', 'mode:', mode, type, 'Size:',
                            Size, 'Offset:', Offset, 'Encoding:', Encoding], n)
                if Encoding == '"varint"':
                    path = getPath(File)
                    if path:
                        file = open(path, 'rb')
                        g = BinaryReader(file)
                        bytes = decodeVarint(g, Offset, Size*ItemSize, type)
                        vertexArray.append([bytes, Encoding, ItemSize])
                        file.close()

            Float32Array = ys.get(b, '"Float32Array"')
            if Float32Array:
                type = 'Float32Array'
                print(mode, type)
                values = ys.values(Float32Array[0].data, ':')
                Size = ys.getValue(values, '"Size"', 'i')
                Offset = ys.getValue(values, '"Offset"', 'i')
                File = ys.getValue(values, '"File"', '""')
                Encoding = ys.getValue(values, '"Encoding"')
                write(log, ['Vertex:', 'mode:', mode, type, 'Size:',
                            Size, 'Offset:', Offset, 'Encoding:', Encoding], n)
                if Encoding != '"varint"':
                    path = getPath(File)
                    if path:
                        file = open(path, 'rb')
                        g = BinaryReader(file)
                        g.seek(Offset)
                        bytes = g.f(Size*ItemSize)
                        list = []
                        for m in range(Size):
                            list.append(bytes[m*ItemSize:m*ItemSize+ItemSize])
                        vertexArray.append([list, Encoding])
                        file.close()

    TexCoord0 = ys.get(VertexAttributeList[0], '"TexCoord0"')
    if TexCoord0:
        mode = "TexCoord0"
        for b in TexCoord0:
            Size = None
            Offset = None
            Encoding = None
            ItemSize = None
            type = None
            values = ys.values(b.data, ':')
            if '"ItemSize"' in values:
                ItemSize = int(values['"ItemSize"'])
                Int32Array = ys.get(b, '"Int32Array"')
                if Int32Array:
                    type = 'Int32Array'
                    print(mode, type)
                    values = ys.values(Int32Array[0].data, ':')
                    Size = ys.getValue(values, '"Size"', 'i')
                    Offset = ys.getValue(values, '"Offset"', 'i')
                    File = ys.getValue(values, '"File"', '""')
                    Encoding = ys.getValue(values, '"Encoding"')
                    write(log, ['TexCoord0:', 'mode:', mode, type, 'Size:',
                                Size, 'Offset:', Offset, 'Encoding:', Encoding], n)
                    if Encoding == '"varint"':
                        path = getPath(File)
                        if path:
                            file = open(path, 'rb')
                            g = BinaryReader(file)
                            bytes = decodeVarint(
                                g, Offset, Size*ItemSize, type)
                            texArray.append([bytes, Encoding, ItemSize])
                            file.close()

                Float32Array = ys.get(b, '"Float32Array"')
                if Float32Array:
                    type = 'Float32Array'
                    print(mode, type)
                    values = ys.values(Float32Array[0].data, ':')
                    Size = ys.getValue(values, '"Size"', 'i')
                    Offset = ys.getValue(values, '"Offset"', 'i')
                    File = ys.getValue(values, '"File"', '""')
                    Encoding = ys.getValue(values, '"Encoding"')
                    write(log, ['TexCoord0:', 'mode:', mode, type, 'Size:',
                                Size, 'Offset:', Offset, 'Encoding:', Encoding], n)
                    if Encoding != '"varint"':
                        path = getPath(File)
                        if path:
                            file = open(path, 'rb')
                            g = BinaryReader(file)
                            g.seek(Offset)
                            bytes = g.f(Size*ItemSize)
                            list = []
                            for m in range(Size):
                                u, v = bytes[m*ItemSize:m*ItemSize+ItemSize]
                                list.append([u, 1-v])
                            texArray.append([list, Encoding])
                            file.close()

    return vertexArray, texArray


def getRigGeometry(ys, parent, n):
    print('#'*50, 'RigGeometry')
    n += 4
    BoneMap = [0]*1000
    bones = []
    weights = []
    mode = None
    indiceArray = []
    vertexArray = []
    texArray = []
    atributes = {}
    for child in parent.children:
        if "BoneMap" in child.header:
            write(log, ['BoneMap'], n)
            values = ys.values(child.data, ':')
            # print values
            for value in values:
                id = ys.getValue(values, value, 'i')
                name = value.split('"')[1]
                BoneMap[id] = getSplitName(name, '_', -1)
        if "SourceGeometry" in child.header:
            values = ys.values(child.data, ':')
            PrimitiveSetList = ys.get(child, '"PrimitiveSetList"')
            if PrimitiveSetList:
                indiceArray = getPrimitiveSetList(ys, PrimitiveSetList, n)

            UserDataContainer = ys.get(child, '"UserDataContainer"')
            if UserDataContainer:
                for UserData in UserDataContainer:
                    Values = ys.get(UserData, '"Values"')
                    if Values:
                        for a in Values[0].children:
                            values = ys.values(a.data, ':')
                            Name = ys.getValue(values, '"Name"', '""')
                            Value = ys.getValue(values, '"Value"', '""')
                            if Name:
                                atributes[Name] = Value

            VertexAttributeList = ys.get(child, '"VertexAttributeList"')
            if VertexAttributeList:
                vertexArray, texArray = getVertexAttributeList(
                    ys, VertexAttributeList, n)

        if "UserDataContainer" in child.header:
            write(log, ['UserDataContainer'], n)
            Values = ys.get(child, '"Values"')
            if Values:
                for a in Values[0].children:
                    values = ys.values(a.data, ':')
                    for value in values:
                        id = ys.getValue(values, value)
                        write(log, [value, ':', id], n+4)
        if "VertexAttributeList" in child.header:
            write(log, ['VertexAttributeList'], n)
            Bones = ys.get(child, '"Bones"')
            if Bones:
                write(log, ['Bones'], n+4)
                values = ys.values(Bones[0].data, ':')
                ItemSize = ys.getValue(values, '"ItemSize"', 'i')
                write(log, ['"ItemSize"', ':', ItemSize], n+8)
                Uint16Array = ys.get(Bones[0], '"Uint16Array"')
                if Uint16Array:
                    type = "Uint16Array"
                    values = ys.values(Uint16Array[0].data, ':')
                    File = ys.getValue(values, '"File"', '""')
                    Size = ys.getValue(values, '"Size"', 'i')
                    Offset = ys.getValue(values, '"Offset"', 'i')
                    Encoding = ys.getValue(values, '"Encoding"', '""')
                    write(log, ['"File"', ':', File], n+8)
                    write(log, ['"Size"', ':', Size], n+8)
                    write(log, ['"Offset"', ':', Offset], n+8)
                    write(log, ['"Encoding"', ':', Encoding], n+8)

                    if Encoding == 'varint':
                        path = os.path.dirname(
                            ys.filename)+os.sep+"model_file.bin.gz.txt"
                        if os.path.exists(path) == False:
                            path = os.path.dirname(
                                ys.filename)+os.sep+"model_file.bin"
                        if os.path.exists(path) == False:
                            path = os.path.dirname(
                                ys.filename)+os.sep+values['"File"'].split('"')[1]  # +'.txt'
                        if os.path.exists(path) == True:
                            file = open(path, 'rb')
                            g = BinaryReader(file)
                            list = decodeVarint(g, Offset, Size*ItemSize, type)
                            # write(log,list,0)
                            for m in range(Size):
                                bones.append(
                                    list[m*ItemSize:m*ItemSize+ItemSize])
                            file.close()

            Weights = ys.get(child, '"Weights"')
            if Weights:
                write(log, ['Weights'], n+4)
                values = ys.values(Weights[0].data, ':')
                ItemSize = ys.getValue(values, '"ItemSize"', 'i')
                write(log, ['"ItemSize"', ':', ItemSize], n+8)
                Float32Array = ys.get(Weights[0], '"Float32Array"')
                if Float32Array:
                    values = ys.values(Float32Array[0].data, ':')
                    File = ys.getValue(values, '"File"', '""')
                    Size = ys.getValue(values, '"Size"', 'i')
                    Offset = ys.getValue(values, '"Offset"', 'i')
                    Encoding = ys.getValue(values, '"Encoding"', '""')
                    write(log, ['"File"', ':', File], n+8)
                    write(log, ['"Size"', ':', Size], n+8)
                    write(log, ['"Offset"', ':', Offset], n+8)
                    write(log, ['"Encoding"', ':', Encoding], n+8)

                    if Encoding == 'varint':
                        path = os.path.dirname(
                            ys.filename)+os.sep+"model_file.bin.gz.txt"
                        if os.path.exists(path) == False:
                            path = os.path.dirname(
                                ys.filename)+os.sep+"model_file.bin"
                        if os.path.exists(path) == False:
                            path = os.path.dirname(
                                ys.filename)+os.sep+values['"File"'].split('"')[1]  # +'.txt'
                        if os.path.exists(path) == True:
                            file = open(path, 'rb')
                            g = BinaryReader(file)
                            list = decodeVarint(g, Offset, Size*ItemSize, type)
                            # write(log,list,0)
                            file.close()
                    else:
                        path = os.path.dirname(
                            ys.filename)+os.sep+"model_file.bin.gz.txt"
                        if os.path.exists(path) == False:
                            path = os.path.dirname(
                                ys.filename)+os.sep+"model_file.bin"
                        if os.path.exists(path) == False:
                            path = os.path.dirname(
                                ys.filename)+os.sep+values['"File"'].split('"')[1]  # +'.txt'
                        if os.path.exists(path) == True:
                            file = open(path, 'rb')
                            g = BinaryReader(file)
                            g.seek(Offset)
                            list = g.f(Size*ItemSize)
                            # write(log,list,0)
                            for m in range(Size):
                                weights.append(
                                    list[m*ItemSize:m*ItemSize+ItemSize])
                            file.close()

    # print atributes
    mesh = Mesh()
    if len(bones) > 0 and len(Weights) > 0:
        mesh.BoneMap = BoneMap
        skin = Skin()
        mesh.skinList.append(skin)
        mesh.skinIndiceList = bones
        mesh.skinWeightList = weights
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
                #mesh.vertUVList=[floats[m:m+ItemSize]for m in range(0,len(floats),ItemSize)]
                for m in range(0, len(floats), ItemSize):
                    u, v = floats[m:m+ItemSize]
                    mesh.vertUVList.append([u, 1-v])
            else:
                list = texArray[0][0]
                mesh.vertUVList = list
    return mesh









def Parser():
    global log
    log = open('log.txt', 'w')
    filename = input.filename
    print()
    print(filename)
    print()
    os.system("cls")
    ext = filename.split('.')[-1].lower()
    osgParser(filename)
    log.close()


def openFile(flagList):
    global input, output
    input = Input(flagList)
    output = Output(flagList)
    parser = Parser()


Blender.Window.FileSelector(openFile, 'import', 'file.osgjs')
