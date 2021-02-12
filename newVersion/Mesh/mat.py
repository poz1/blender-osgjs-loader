import random
from ..Util.var import *

class Mat:
	def __init__(self):#0,1,2,3,4,5,6,7,
		self.name=None
		self.matrix=None
		self.BINDSKELETON=None
		self.ZTRANS=False
		self.RGBTRANSPARENT=False
		
		self.diffuse=None
		self.DIFFUSESLOT=0
		self.NORMALSLOT=1
		self.SPECULARSLOT=2
		self.AOSLOT=3
		self.NORMAL1SLOT=4
		self.NORMAL2SLOT=5
		self.DIFFUSE1SLOT=6
		self.DIFFUSE2SLOT=7
		self.REFLECTIONSLOT=8
		self.ALPHASLOT=8
		#self.RGBTRANSPARENTSLOT=8
		self.EMITSLOT=9
		
		self.diffuse1=None
		self.diffuse2=None
		self.alpha=None
		
		self.normal=None
		self.NORMALSTRONG=0.5
		self.NORMALDIRECTION=1
		self.NORMALSIZE=(1,1,1) 
		
		self.bump=None
		
		self.specular=None
		
		self.ao=None
		
		self.normal1=None
		self.NORMAL1STRONG=0.8
		self.NORMAL1DIRECTION=1
		self.NORMAL1SIZE=(15,15,15) 
		
		self.normal2=None
		self.NORMAL2STRONG=0.8
		self.NORMAL2DIRECTION=1
		self.NORMAL2SIZE=(15,15,15) 
		
		self.reflection=None
		self.REFLECTIONSTRONG=1.0
		
		self.emit=None
		
		#self.USEDTRIANGLES=[None,None]
		self.TRIANGLE=False
		self.TRISTRIP=False
		self.QUAD=False
		self.IDStart=None
		self.IDCount=None
		self.faceIDList=[]
		self.rgbCol=None
		self.rgbSpec=None
		
		r=random.randint(0,255)
		g=random.randint(0,255)
		b=random.randint(0,255)
		self.rgba=[r/255.0,g/255.0,b/255.0,1.0]
		
		self.trans=None
		
	def draw(self): 
		if self.name is None:
			self.name=str(ParseID())+'-mat-'+str(0)
		blendMat=Blender.Material.New(self.name)
		blendMat.diffuseShader=Blender.Material.Shaders.DIFFUSE_ORENNAYAR
		blendMat.specShader=Blender.Material.Shaders.SPEC_WARDISO
		blendMat.setRms(0.04)
		blendMat.shadeMode=Blender.Material.ShadeModes.CUBIC
		if self.ZTRANS==True:
			blendMat.mode |= Blender.Material.Modes.ZTRANSP
			blendMat.mode |= Blender.Material.Modes.TRANSPSHADOW
			blendMat.alpha = 0.0 
		if self.diffuse is not None:diffuse(blendMat,self)
		if self.reflection is not None:reflection(blendMat,self)
		if self.diffuse1 is not None:diffuse1(blendMat,self)
		if self.diffuse2 is not None:diffuse2(blendMat,self)
		if self.specular is not None:specular(blendMat,self)
		if self.normal is not None:normal(blendMat,self)
		if self.normal1 is not None:normal1(blendMat,self)
		if self.normal2 is not None:normal2(blendMat,self)
		if self.ao is not None:ao(blendMat,self)
		if self.alpha is not None:alpha(blendMat,self)	
		