import os

class Model:
    def __init__(self, input):
        self.meshList = []
        self.filename = input
        self.dirname = None
        self.basename = None
        # if self.filename is not None

    def getMat(self):
        if self.filename is not None and self.meshList > 0:
            self.basename = os.path.basename(self.filename)
            self.dirname = os.path.dirname(self.filename)
            # matPath=self.dirname+os.sep+'mat.txt'
            matPath = self.filename+'.mat'
            if os.path.exists(matPath) == True:
                matfile = open(matPath, 'r')
                lines = matfile.readlines()
                for i, mesh in enumerate(self.meshList):
                    for j, mat in enumerate(mesh.matList):
                        for line in lines:
                            values = line.strip().split(':')
                            if values[0] == "-1":
                                i = -1  # pierwszy raz
                            if len(values) == 3:
                                if values[0] == str(i).zfill(3) and values[1] == 'd':
                                    mat.diffuse = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'n':
                                    mat.normal = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 's':
                                    mat.specular = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'a':
                                    mat.alpha = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'o':
                                    mat.ao = self.dirname+os.sep + \
                                        values[2].split('"')[1]

                                if values[0] == str(i).zfill(3) and values[1] == 'd1':
                                    mat.diffuse1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'd2':
                                    mat.diffuse2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'n1':
                                    mat.normal1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'n2':
                                    mat.normal2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'e':
                                    mat.emit = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'b':
                                    mat.bump = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 't':
                                    mat.trans = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                            if len(values) == 4:
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'd':
                                    mat.diffuse = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'n':
                                    mat.normal = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 's':
                                    mat.specular = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'a':
                                    mat.alpha = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'o':
                                    mat.ao = self.dirname+os.sep + \
                                        values[2].split('"')[1]

                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'd1':
                                    mat.diffuse1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'd2':
                                    mat.diffuse2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'n1':
                                    mat.normal1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'n2':
                                    mat.normal2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'e':
                                    mat.emit = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'b':
                                    mat.bump = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 't':
                                    mat.trans = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                for i, mesh in enumerate(self.meshList):
                    for j, mat in enumerate(mesh.matList):
                        for line in lines:
                            values = line.strip().split(':')
                            #if values[0]=="-1":i=-1
                            if len(values) == 3:
                                if values[0] == str(i).zfill(3) and values[1] == 'd':
                                    mat.diffuse = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'n':
                                    mat.normal = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 's':
                                    mat.specular = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'a':
                                    mat.alpha = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'o':
                                    mat.ao = self.dirname+os.sep + \
                                        values[2].split('"')[1]

                                if values[0] == str(i).zfill(3) and values[1] == 'd1':
                                    mat.diffuse1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'd2':
                                    mat.diffuse2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'n1':
                                    mat.normal1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'n2':
                                    mat.normal2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'e':
                                    mat.emit = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 'b':
                                    mat.bump = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[1] == 't':
                                    mat.trans = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                            if len(values) == 4:
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'd':
                                    mat.diffuse = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'n':
                                    mat.normal = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 's':
                                    mat.specular = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'a':
                                    mat.alpha = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'o':
                                    mat.ao = self.dirname+os.sep + \
                                        values[2].split('"')[1]

                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'd1':
                                    mat.diffuse1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'd2':
                                    mat.diffuse2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'n1':
                                    mat.normal1 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'n2':
                                    mat.normal2 = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'e':
                                    mat.emit = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 'b':
                                    mat.bump = self.dirname+os.sep + \
                                        values[2].split('"')[1]
                                if values[0] == str(i).zfill(3) and values[3] == str(j) and values[1] == 't':
                                    mat.trans = self.dirname + \
                                        os.sep+values[2].split('"')[1]
                        # print i,j,mat.diffuse	"""
                matfile.close()

    def setMat(self):
        # print 'setMat'
        if self.filename is not None and self.meshList > 0:
            self.basename = os.path.basename(self.filename)
            self.dirname = os.path.dirname(self.filename)
            # matPath=self.dirname+os.sep+'mat.txt'
            matPath = self.filename+'.mat'
            # for file in os.listdir(self.dirname):
            #	if file.lower()=='mat.txt':
            matLines = []
            if os.path.exists(matPath) == True:
                file = open(matPath, 'r')
                lines = file.readlines()
                for line in lines:
                    if ':' in line:
                        matLines.append(line)
                file.close()

            # if 'mat.txt' not in os.listdir(os.path.dirname(filename)):
            matFile = open(matPath, 'w')
            for file in os.listdir(self.dirname):
                if file.split('.')[-1].lower() in ['dds', 'png', 'jpg', 'jpeg', 'tga', 'bmp']:
                    matFile.write('"'+file+'"'+'\n')

            for i, mesh in enumerate(self.meshList):
                for j, mat in enumerate(mesh.matList):
                    # print mat.name
                    split = mat.name.split('-')
                    if mat.diffuse is not None:
                        matFile.write(
                            str(split[0])+':d:"'+os.path.basename(mat.diffuse)+'":'+str(split[1])+'\n')
                    if mat.normal is not None:
                        matFile.write(
                            str(split[0])+':n:"'+os.path.basename(mat.normal)+'":'+str(split[1])+'\n')
                    if mat.specular is not None:
                        matFile.write(
                            str(split[0])+':s:"'+os.path.basename(mat.specular)+'":'+str(split[1])+'\n')
                    if mat.ao is not None:
                        matFile.write(
                            str(split[0])+':o:"'+os.path.basename(mat.ao)+'":'+str(split[1])+'\n')
                    if mat.alpha is not None:
                        matFile.write(
                            str(split[0])+':a:"'+os.path.basename(mat.alpha)+'":'+str(split[1])+'\n')

                    if mat.diffuse1 is not None:
                        matFile.write(
                            str(split[0])+':d1:"'+os.path.basename(mat.diffuse1)+'":'+str(split[1])+'\n')
                    if mat.diffuse2 is not None:
                        matFile.write(
                            str(split[0])+':d2:"'+os.path.basename(mat.diffuse2)+'":'+str(split[1])+'\n')
                    if mat.normal1 is not None:
                        matFile.write(
                            str(split[0])+':n1:"'+os.path.basename(mat.normal1)+'":'+str(split[1])+'\n')
                    if mat.normal2 is not None:
                        matFile.write(
                            str(split[0])+':n2:"'+os.path.basename(mat.normal2)+'":'+str(split[1])+'\n')
                    if mat.emit is not None:
                        matFile.write(
                            str(split[0])+':e:"'+os.path.basename(mat.emit)+'":'+str(split[1])+'\n')
                    if mat.bump is not None:
                        matFile.write(
                            str(split[0])+':b:"'+os.path.basename(mat.bump)+'":'+str(split[1])+'\n')
                    if mat.trans is not None:
                        matFile.write(
                            str(split[0])+':t:"'+os.path.basename(mat.trans)+'":'+str(split[1])+'\n')

            matFile.close()

    def draw(self):
        for i, mesh in enumerate(self.meshList):
            # print 'mesh:',i,'vert:',len(mesh.vertPosList),'indice:',len(mesh.indiceList),
            # if len(mesh.indiceList)>0:
            #	print 'min:',min(mesh.indiceList),'max:',max(mesh.indiceList),
            # print 'face:',len(mesh.faceList)
            mesh.draw()
