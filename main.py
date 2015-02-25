import numpy as np
from sklearn import ensemble
from imgarr import imgarr
from streamobj import streamobj
from csvkag import csvkag
from sklearn.decomposition import PCA
#all configuration
trainstart=1
trainend=6283
filetrain1='trainResized/'
filetrain2='.Bmp'
noeig=400

filelable='trainLabels.csv'

teststart=6284
testend=12503
filetest1='testResized/'
filetest2='.Bmp'

noTree=150
critF='entropy'
fileRF='randomforestall.ml'

fileres='myresult.np'

#get matrix data set
myarr=imgarr()
noimage=range(trainstart,trainend+1)
myarr.fillInput(filetrain1,filetrain2,noimage)
myarr.imgToArr1D()
traindata=myarr.nparrayimage

#uncomment if want to do PCA
myarr.setPCA()
#pca=PCA(n_components=noeig)
#pca.fit(myarr.nparrayimage)
#traindata=pca.fit_transform(myarr.nparrayimage)
#traindata=myarr.getXp(noeig)




##get label in integer
csvT=csvkag()
csvT.addInput(filelable)
csvT.genUniqueId()
trainLabel=csvT.npcsvid
#print(traindata.shape)
#print(trainLabel.shape)

#get test data vector
imgarrtest=imgarr()
noimage=range(teststart,testend+1)
imgarrtest.fillInput(filetest1,filetest2,noimage)
imgarrtest.imgToArr1D()
testdata=imgarrtest.nparrayimage

#Uncomment if want to do PCA on test data
#testdata=pca.fit_transform(imgarrtest.nparrayimage)
#testdata=np.dot(imgarrtest.nparrayimage,ucut)

##setup random forest
clf = ensemble.RandomForestClassifier(n_estimators=noTree,criterion=critF)
print("Classifier:\n\t %s"%str(clf))
clf = clf.fit(traindata,trainLabel)
streamobj.saveMe(clf,fileRF)  #save machine learning algorithma as object 

#do prediction
myresult=clf.predict(testdata)

#save in kaggle format
res=csvT.getKey(myresult)
noId=range(teststart,testend+1)
csvT.wrtCsv(noId,res)

