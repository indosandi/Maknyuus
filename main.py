from sklearn import ensemble
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm  # 
from imgarr import imgarr
myarr=imgarr()
noimage=range(1,6283)
myarr.fillInput("trainResized/",".bmp",noimage)
print(len(myarr.listInput))
myarr.imgToArr1D()
#with open('mydata.obj','wb') as output:
    #pickle.dump(myarr,output,pickle.HIGHEST_PROTOCOL)
#with open('mydata.obj','rb') as input:
    #myarr=pickle.load(input)
    #print(myarr.nparrayimage.shape)
myarr.setPCA()
#print(myarr.getErr(100))
#print(myarr.getXp(100).shape)
#xred=myarr.getXred(200,[0,1,2,3,4,5,6])
#plt.figure(1)
#justno=3
#xreduce=xred[justno,:]
#noxpixel=20
#noypixel=20
#plt.imshow(np.reshape(xreduce,(noxpixel,noypixel)),cmap=cm.Greys_r)
#plt.figure(2)
#plt.imshow(np.reshape(myarr.nparrayimage[justno,:],(noxpixel,noypixel)),cmap=cm.Greys_r)
#plt.show()

myarr.saveMe('mydata.obj')
test=imgarr()
test.loadMe('mydata.obj')
#test.fillInput('trainLabels/','.bmp',[1, 2, 3])
#print(test.nparrayimage.shape)
print(len(test.listInput))
#test.saveMe('nyimpen.obj')
