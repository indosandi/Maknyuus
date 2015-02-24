import numpy as np
from sklearn import cross_validation
from sklearn import ensemble
#from StringIO import StringIO
#data = "1, 2, 3\n4, 5, 6"
mydata=np.genfromtxt('train2.csv',delimiter=',')
mytarget=np.genfromtxt('train3.csv',delimiter=',')
mytest=np.genfromtxt('test.csv',delimiter=',')
#X_train, X_test, y_train, y_test = cross_validation.train_test_split(\
	#mydata, mytarget, test_size=0.1, random_state=0)

clf = ensemble.RandomForestClassifier(n_estimators=100,criterion='entropy')
clf = clf.fit(X_train,y_train)
#print(clf.score(X_test,y_test))
myresult=clf.predict(mytest)
print("ok")
#print(clf.oob_score_)
#np.savetxt("result.csv", myresult, delimiter=",",fmt='%1d')
#print(mydata[0,:])
