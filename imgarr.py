from scipy import misc
#import matplotlib.pyplot as plt
#import matpotlib.cm as cm # 
import numpy as np
class imgarr:

    #init
    def __init__(self):
        self.listInput=[]
        self.nparrayimage=np.array([],dtype=np.float64)

    #add string to listInput
    def appInput(self,myin):
        self.listInput.append(myin)

    #fill up listInput with begin end string
    def fillInput(self,begin,end,total):
        for i in range(1,total+1):
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

# if run as a script
#if __name__=="__main__":
    #myarr=arrimg()
    ##myarr.appinput("img/Lenna.png")
    #a=["img/Lenna.png","Lenna.png"]
    ##a=["Lenna.png"]
    #myarr.repinput(a)
    ##print(myarr.listInput)
    #myarr.imgToArr()
    #print(myarr.nparrayimage.shape)
    ##ar2=myarr.rgbToG(ar)
    #ar2=myarr.nparrayimage[:,:,1]
    #plt.draw()
    #plt.imshow(ar2,cmap=cm.Greys_r)
    #plt.show()

