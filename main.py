#from sklearn import ensemble
#from csvkag import csvkag
import numpy as np
from sklearn import cross_validation
from sklearn import ensemble
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm  # 
#from imgarr import imgarr
from streamobj import streamobj
#myarr=imgarr()
#noimage=range(1,6284)
#myarr.fillInput("trainResized/",".bmp",noimage)
#print(len(myarr.listInput))
#myarr.imgToArr1D()
#with open('mydata.obj','wb') as output:
    #pickle.dump(myarr,output,pickle.HIGHEST_PROTOCOL)
#with open('mydata.obj','rb') as input:
    #myarr=pickle.load(input)
    #print(myarr.nparrayimage.shape)
#myarr.setPCA()
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

#myarr.saveMe('img1_6283.obj')
#test=imgarr()
#load array object

#arrimg=streamobj.loadMe('img1_6283.obj')
#arrimg.setPCA()

#I set no_eigen is 250
#no_eigen=250
#traindata=arrimg.getXp(no_eigen)
#streamobj.saveMe(traindata,'traindata.np')
#load trainLabel obj
#trainLabelobj=streamobj.loadMe('trainLabel.obj')
#trainLabel=trainLabelobj.npcsvid
#streamobj.saveMe(trainLabel,'trainLabel.np')
traindata=streamobj.loadMe('traindata.np')
trainLabel=streamobj.loadMe('trainLabel.np')
print(traindata.shape)
print(trainLabel.shape)
clf = ensemble.RandomForestClassifier(n_estimators=100,criterion='entropy')
clf = clf.fit(traindata,trainLabel)
print("ok")
streamobj.saveMe('clf','randomforestall.ml')
#len=traindata.shape[0]
#kf=cross_validation.KFold(len,5)
#clf = ensemble.RandomForestClassifier(n_estimators=2,criterion='gini')
#for train_index,test_index in kf:
        #x_train,x_test=traindata[train_index],trainLabel[test_index]
        #y_train,y_test=traindata[train_index],trainLabel[test_index]
        #clf = clf.fit(x_train,y_train)
        #print(clf.score(x_test,y_test))
        #print("ok")

