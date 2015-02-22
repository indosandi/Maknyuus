import numpy as np
from covMatrix import covMatrix as cM 

x = np.array([[0, 2], [1, 3], [2, 0]]).T
test1=cM.cor(x)
#print(x[:,0].mean())
#print(x[:,0])
#test1=cM.covXY(x,0,0)
print(test1.shape)
for i in range(0,test1.shape[0]):
    print("{0} , {1}, {2}  \n".format(test1[i,0],test1[i,1],test1[i,2]))
