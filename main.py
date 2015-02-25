#from sklearn import ensemble
#from csvkag import csvkag
import numpy as np
from sklearn import cross_validation
from sklearn import ensemble
from imgarr import imgarr
from streamobj import streamobj
from csvkag import csvkag

#all configuration
trainstart=1
trainend=6283
filetrain1='trainResized/'
filetrain2='.bmp'

filelable='trainLabels.csv'

teststart=6284
testend=12503
filetest1='testResized/'
filetest2='.bmp'

noTree=100
critF='entropy'
fileRF='randomforestall.ml'

fileres='myresult.np'

#get matrix data set
myarr=imgarr()
noimage=range(trainstart,trainend+1)
myarr.fillInput(filetrain1,filetrain2,noimage)
myarr.imgToArr1D()
traindata=myarr.nparrayimage

##get label in integer
csvT=csvkag()
csvT.addInput(filelable)
csvT.genUniqueId()
trainLabel=csvT.npcsvid
#print(traindata.shape)
#print(trainLabel.shape)

##get test data vector
imgarrtest=imgarr()
noimage=range(teststart,testend+1)
imgarrtest.fillInput(filetest1,filetest2,noimage)
imgarrtest.imgToArr1D()
testdata=imgarrtest.nparrayimage

##setup random forest
clf = ensemble.RandomForestClassifier(n_estimators=noTree,criterion=critF)
clf = clf.fit(traindata,trainLabel)
streamobj.saveMe(clf,fileRF)

##do prediction
myresult=clf.predict(testdata)
streamobj.saveMe(myresult,fileres)

#save in kaggle format
#myresult=streamobj.loadMe('myresult.np')
res=csvT.getKey(myresult)
noId=range(teststart,testend+1)
csvT.wrtCsv(noId,res)

