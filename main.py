import pickle
from imgarr import imgarr
#myarr=imgarr()
#a=["img/Lenna.png","Lenna.png"]
#myarr.repinput(a)
#myarr.imgToArr1D()
#print(myarr.nparrayimage.shape)
#with open('mydata.obj','wb') as output:
    #pickle.dump(myarr,output,pickle.HIGHEST_PROTOCOL)
with open('mydata.obj','rb') as input:
    myarr=pickle.load(input)
    print(myarr.nparrayimage.shape)
