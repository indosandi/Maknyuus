import numpy as np
from sklearn import cross_validation
from sklearn import ensemble
#from StringIO import StringIO
#data = "1, 2, 3\n4, 5, 6"
mydata=np.genfromtxt('traincut.csv',delimiter=',')
mytarget=np.genfromtxt('train3.csv',delimiter=',')
mytest=np.genfromtxt('test.csv',delimiter=',')
# mydata=mydata[:,0:9]
len=mydata.shape[0]
kf=cross_validation.KFold(len,5)
clf = ensemble.RandomForestClassifier(n_estimators=100,criterion='gini')
for train_index,test_index in kf:
	x_train,x_test=mydata[train_index],mydata[test_index]
	y_train,y_test=mytarget[train_index],mytarget[test_index]
	clf = clf.fit(x_train,y_train)
	print(clf.score(x_test,y_test))
	print("ok")
# X_train, X_test, y_train, y_test = cross_validation.train_test_split(\
#	mydata, mytarget, test_size=0.1, random_state=0)

#myresult=clf.predict(mytest)
#print(clf.oob_score_)
#np.savetxt("result.csv", myresult, delimiter=",",fmt='%1d')
#print(mydata[0,:])