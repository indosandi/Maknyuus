from scipy import misc
import pickle
from covMatrix import covMatrix as covMatrix
import numpy as np
class imgarr:

    #init
    def __init__(self):
        self.listInput=[]
        self.nparrayimage=np.array([],dtype=np.float64)
        self.ueig=None
        self.seig=None

    #save object to file
    def saveMe(self,str):
        with open(str,'wb') as output:
            pickle.dump(self,output,pickle.HIGHEST_PROTOCOL)

    #load obj
    def loadMe(self,str):
        with open(str,'rb') as input:
            tmpObj=pickle.load(input)
            self.__dict__.update(tmpObj.__dict__)

    #add string to listInput
    def appInput(self,myin):
        self.listInput.append(myin)

    #fill up listInput with begin end string
    def fillInput(self,begin,end,listNumber):
        for i in listNumber:
            strtemp=begin+str(i)+end
            self.appInput(strtemp)

    #average from RGB to grayscale
    def rgbToG(self,arr):
        return (arr[:,:,0]+arr[:,:,1]+arr[:,:,2])/3

    #replace array list input
    def repinput(self,myin):
        self.listInput=myin
    
    #image to 1 D array
    def imgToArr1D(self):
        nindex=0;
        img=misc.imread(self.listInput[0])
        xdim=img.shape[0]
        ydim=img.shape[1]
        self.nparrayimage=np.zeros((len(self.listInput),xdim*ydim))
        for value in self.listInput:
            img=misc.imread(value)
            if len(img.shape)>2:
                imgGrey=self.rgbToG(img)
            else:
                imgGrey=img
            totalDim=xdim*ydim
            imgGrey1D=np.reshape(imgGrey,totalDim)
            self.nparrayimage[nindex,0:xdim*ydim]=imgGrey1D[:]
            nindex+=1

    #image to 2D array
    def imgToArr(self):
        nindex=0;
        img=misc.imread(self.listInput[0])
        xdim=img.shape[0]
        ydim=img.shape[1]
        self.nparrayimage=np.zeros((xdim,ydim,len(self.listInput)))
        for value in self.listInput:
            img=misc.imread(value)
            imgGrey=self.rgbToG(img)
            totalDim=xdim*ydim
            self.nparrayimage[0:xdim,0:ydim,nindex]=imgGrey[:,:]
            nindex+=1
    
    #do PCA on array
    def setPCA(self):
        #covariance matrix
        covM=covMatrix.cov(self.nparrayimage)
        u,s,v=np.linalg.svd(covM,full_matrices=True)
        self.ueig=u
        self.seig=s

    #get error given cut
    def getErr(self,eigint):
        return 1-np.sum(self.seig[0:eigint])/np.sum(self.seig)

    #get x in different representation
    def getXp(self,eigint):
        ucut=np.delete(self.ueig,range(eigint,self.ueig.shape[1]),1)
        return np.dot(self.nparrayimage,ucut)

    #get x value back after cut
    def getXred(self,eigint,idX):
        ucut=np.delete(self.ueig,range(eigint,self.ueig.shape[1]),1)
        newdata=np.dot(self.nparrayimage[idX,:],ucut)
        return np.dot(newdata,ucut.T)



