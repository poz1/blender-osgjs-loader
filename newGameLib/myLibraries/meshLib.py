import bpy
import mathutils
from math import *
from .myFunction import *
from .commandLib import *
import random
import os
#from bump_to_normal import *

#print 'meshLib'
   

	
def GetBlackFromImage(path):

	sys=Sys(path)
	image = Blender.Image.Load(path)
	imagedepth=image.getDepth() 
	imagesize = image.getSize()
	imagenewname=sys.dir+os.sep+sys.base+'-alfa.tga'
	
	
	img=Sys(imagenewname)
	ImgPath=img.dir+os.sep+img.base+'.jpg'
	
	if os.path.exists(ImgPath)==False:
		#print imagenewname
		imagenew = Blender.Image.New(imagenewname,imagesize[0],imagesize[1],imagedepth) 
		for x in range(0,imagesize[0]):
				for y in range(0,imagesize[1]):
					pix=image.getPixelI(x, y)
					if 125<pix[0]<135 and 121<pix[1]<131 and 57<pix[2]<67:
					#if pix[0]==130 and pix[1]==126 and pix[2]==62:
						#print pix
						imagenew.setPixelI(x,y,[0,0,0,0])
					else:
						#imagenew.setPixelI(x,y,[255-pix[0],255-pix[1],255-pix[2],0])
						imagenew.setPixelI(x,y,[255,255,255,0])
		imagenew.save()
		
		
				
		cmd=Cmd()
		cmd.input=imagenewname
		cmd.JPG=True
		cmd.run()
	return ImgPath 
	
def setBox(box,meshList):
	E=[[],[],[]]
	for mesh in meshList:
		for n in range(len(mesh.vertPosList)):
			x,y,z=mesh.vertPosList[n]
			E[0].append(x)
			E[1].append(y)
			E[2].append(z)	
	skX=(box[3]-box[0])/(max(E[0])-min(E[0]))
	skY=(box[4]-box[1])/(max(E[1])-min(E[1]))
	skZ=(box[5]-box[2])/(max(E[2])-min(E[2]))
	sk=min(skX,skY,skZ)
	trX1=(box[3]+box[0])/2#-(max(E[0])+min(E[0]))/2
	trY1=(box[4]+box[1])/2#-(max(E[1])+min(E[1]))/2
	trZ1=(box[5]+box[2])/2#-(max(E[2])+min(E[2]))/2
	
	trX=-(max(E[0])+min(E[0]))/2
	trY=-(max(E[1])+min(E[1]))/2
	trZ=-(max(E[2])+min(E[2]))/2
	#print trX,trY,trZ
	#print skX,skY,skZ
	
	for mesh in meshList:
		for n in range(len(mesh.vertPosList)):
			x,y,z=mesh.vertPosList[n]
			mesh.vertPosList[n]=[x+trX,y+trY,z+trZ]
		for n in range(len(mesh.vertPosList)):
			x,y,z=mesh.vertPosList[n]
			mesh.vertPosList[n]=[x*skX,y*skY,z*skZ]
		for n in range(len(mesh.vertPosList)):
			x,y,z=mesh.vertPosList[n]
			mesh.vertPosList[n]=[x+trX1,y+trY1,z+trZ1]
		#mesh.draw()	 
		
def setBox1(box,meshList):
	E=[[],[],[]]
	for mesh in meshList:
		for n in range(len(mesh.vertPosList)):
			x,y,z=mesh.vertPosList[n]
			E[0].append(x)
			E[1].append(y)
			E[2].append(z)	
	skX=(box[3]-box[0])/(max(E[0])-min(E[0]))
	skY=(box[4]-box[1])/(max(E[1])-min(E[1]))
	skZ=(box[5]-box[2])/(max(E[2])-min(E[2]))
	sk=min(skX,skY,skZ)
	trX=(box[3]+box[0])/2
	trY=(box[4]+box[1])/2
	trZ=(box[5]+box[2])/2
	
	
	for mesh in meshList:
		for n in range(len(mesh.vertPosList)):
			x,y,z=mesh.vertPosList[n]
			mesh.vertPosList[n]=[trX+x*skX,trY+y*skY,trZ+z*skZ]
		#mesh.draw()	

def bindPose(bindSkeleton,poseSkeleton,meshObject):
		#print 'BINDPOSE'
		mesh=meshObject.getData(mesh=1)
		poseBones=poseSkeleton.getData().bones
		bindBones=bindSkeleton.getData().bones			
		for vert in mesh.verts:
			index=vert.index
			skinList=mesh.getVertexInfluences(index)
			vco=vert.co.copy()*meshObject.matrixWorld
			vector=Vector()
			sum=0
			for skin in skinList:
				#try:
					bone=skin[0]							
					weight=skin[1]					
					matA=bindBones[bone].matrix['ARMATURESPACE']*bindSkeleton.matrixWorld
					matB=poseBones[bone].matrix['ARMATURESPACE']*poseSkeleton.matrixWorld
					vector+=vco*matA.invert()*matB*weight
					sum+=weight
				#except:pass	
			#print sum,	
			vert.co=vector
		mesh.update()
		Blender.Window.RedrawAll()
			
			
#ID=3
#bindSkeleton=Blender.Object.Get('armature-'+str(ID))
#poseSkeleton=Blender.Object.Get('bindPose-mesh-'+str(ID))
#meshObject=Blender.Object.Get('mesh-'+str(ID))

#bindPose(bindSkeleton,poseSkeleton,meshObject)	



		
		
			
			
def image2png(imagePath):
	if os.path.exists(imagePath)==True:
		cmd=Cmd()
		cmd.PNG=True	
		cmd.input=imagePath
		cmd.run()
	
		
class Skin:
	def __init__(self):
		self.boneMap=[]
		self.IDStart=None
		self.IDCount=None
		self.skeleton=None
		self.skeletonFile=None
			

		
