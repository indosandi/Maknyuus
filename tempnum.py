import numpy as np
from covMatrix import covMatrix as cM 
#a=np.array([[40,10],[50,20]]) 
#b=a.mean(axis=0)
#print(a[:,0])
#print(b.shape[0])
#print(b.T.shape)
#c=np.ones((5,1))
#d=np.reshape(b,(1,b.shape[0]))
#print(c.shape)
#print(d.shape)
#e=np.dot(c,d)
#print(e.shape)
#for i in range(0,c.shape[0]):
    #print("{0} , {1}  \n".format(e[i,0],e[i,1]))

x = np.array([[0, 2], [1, 1], [2, 0]]).T
print(x)
test1=cM.cov(x)
print(test1.shape)
for i in range(0,test1.shape[0]):
    print("{0} , {1}  \n".format(test1[i,0],test1[i,1]))
