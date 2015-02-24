from imgarr import imgarr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm  # 
myarr=imgarr()
noimage=range(1,6284)
myarr.fillInput("trainResized/",".bmp",noimage)
print(myarr.listInput[0])
myarr.imgToArr1D() #nama arraynya
print(myarr.nparrayimage.shape)
myarr.saveMe('objectane.obj')
myarr.setPCA()
print(myarr.getErr(50))
zmatrix=myarr.getXp(50)

xred=myarr.getXred(50,[0,1,2,3,4,5,6])
justno=3
xreduce=xred[justno,:]
noxpixel=20
noypixel=20
plt.figure(1)
plt.imshow(np.reshape(xreduce,(noxpixel,noypixel)),cmap=cm.Greys_r)
plt.figure(2)
plt.imshow(np.reshape(myarr.nparrayimage[justno,:],(noxpixel,noypixel)),cmap=cm.Greys_r)
plt.show()

#print(myarr.getXp(100).shape)
#newarr=imgarr.loadMe
#newarr.loadMe('objectane.obj')
#print(newarr.nparrayimage.shape)
