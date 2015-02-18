from scipy import misc
import matplotlib.pyplot as plt
import matplotlib.cm as cm # 
import numpy as np
class arrimg:

    def __init__(self):
        self.listInput=[]
        self.nparrayimage=np.array([],dtype=np.float64)
    def appinput(self,myin):
        self.listInput.append(myin)

    def rgbToG(self,arr):
        return (arr[:,:,0]+arr[:,:,1]+arr[:,:,0])/3
    def repinput(self,myin):
        self.listInput=myin
    def imgToArr(self):
        #nparrayimage=np.array(nparrayimage)
        nindex=0;
        img=misc.imread(self.listInput[0])
        xdim=img.shape[0]
        ydim=img.shape[1]
        self.nparrayimage=np.zeros((xdim,ydim,len(self.listInput)))
        for value in self.listInput:
            img=misc.imread(value)
            imgGrey=self.rgbToG(img)
            totalDim=xdim*ydim
            #imgGrey1D=np.reshape(imgGrey,totalDim)
            #print(totalDim)
            #print(imgGrey.shape)
            #self.nparrayimage=np.vstack((self.nparrayimage,imgGrey1D))
            
            self.nparrayimage[0:xdim,0:ydim,nindex]=imgGrey[:,:]
            nindex+=1
            #self.nparrayimage=np.append(self.nparrayimage,imgGrey)
        #return img
        #self.nparrayimage=np.reshape(self.nparrayimage,(2,512*512))
        #self.nparrayimage=np.reshape(self.nparrayimage,(512,512,2))

# if run as a script
if __name__=="__main__":
    myarr=arrimg()
    #myarr.appinput("img/Lenna.png")
    a=["img/Lenna.png","Lenna.png"]
    #a=["Lenna.png"]
    myarr.repinput(a)
    #print(myarr.listInput)
    myarr.imgToArr()
    print(myarr.nparrayimage.shape)
    #ar2=myarr.rgbToG(ar)
    ar2=myarr.nparrayimage[:,:,1]
    plt.draw()
    plt.imshow(ar2,cmap=cm.Greys_r)
    plt.show()

