import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm  # 
#from imgarr import imgarr
#myarr=imgarr()
#noimage=6283
#myarr.fillInput("trainResized/",".bmp",noimage)
#for i in myarr.listInput:
    #print(i)
#a=["img/Lenna.png","Lenna.png"]
#myarr.repinput(a)
#myarr.imgToArr1D()
#print(myarr.nparrayimage.shape)
#with open('mydata.obj','wb') as output:
    #pickle.dump(myarr,output,pickle.HIGHEST_PROTOCOL)
with open('mydata.obj','rb') as input:
    myarr=pickle.load(input)
    print(myarr.nparrayimage.shape)
test=np.dot(myarr.nparrayimage.T,myarr.nparrayimage)
print(test.shape)
u,s,v=np.linalg.svd(test,full_matrices=True)
print(u.shape)
noeigvec=250;
print(np.sum(s[0:noeigvec])/np.sum(s))
ucut=np.delete(u,range(noeigvec,u.shape[1]),1)
print(ucut.shape)

justno=147
newdata=np.dot(myarr.nparrayimage[justno,:],ucut)
print(newdata.shape)
xreduce=np.dot(newdata,ucut.T)
print(xreduce.shape)
plt.figure(1)
plt.imshow(np.reshape(xreduce,(20,20)),cmap=cm.Greys_r)
plt.figure(2)
plt.imshow(np.reshape(myarr.nparrayimage[justno,:],(20,20)),cmap=cm.Greys_r)
plt.show()

#imgcov=np.cov(myarr.nparrayimage.T,myarr.nparrayimage)
#print(imgcov.shape)

