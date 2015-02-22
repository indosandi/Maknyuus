import numpy as np

class covMatrix:

    #return 2d mean matrix by row
    #@staticmethod
    #def meanr(arr):
        ##1d array of mean of row
        #mean1d=arr.mean(axis=0)
        ##2d  1xn of mean of row jk 
        #mean1ds=np.reshape(mean1d,(1,mean1d.shape[0]))
        #nrow=arr.shape[0]
        #one=np.ones((nrow,1))
        #return np.dot(one,mean1ds)

    #return mean of row matrix
    def meanRow(arr):
        return np.mean(arr,axis=0)

    #return covariance matrix
    def cov(arr):
        nTrainsize=arr.shape[0]
        meanX=covMatrix.meanRow(arr)
        xTilde=arr-meanX
        return np.dot(xTilde.T,xTilde)/nTrainsize
    
    #return elemenet covXY
    def corXY(arr,i,j):
        arri=np.reshape(arr[:,i],(arr[:,i].shape[0],1))
        arrj=np.reshape(arr[:,j],(arr[:,j].shape[0],1))
        #arri=arr[:,i].flatten()
        #arrj=arr[:,j].flatten()
        #print(arr[:,i].shape)
        #meani=covMatrix.meanRow(arr[:,i])
        #meanj=covMatrix.meanRow(arr[:,j])
        #stdi=np.std(arr[:,i])
        #stdj=np.std(arr[:,j])
        #x=arr[:,i]-meani
        #y=arr[:,i]-meanj
        meani=covMatrix.meanRow(arri)
        meanj=covMatrix.meanRow(arrj)
        stdi=np.std(arri,axis=0)
        stdj=np.std(arrj,axis=0)
        x=arri-meani
        y=arrj-meanj
        return x*y/(stdi*stdj)

    #return np array covMatrix
    def cor(arr):
        nsize=arr.shape[1]
        res=np.zeros((nsize,nsize))
        for i in range(0,nsize):
            for j in range(0,nsize):
                #print(covMatrix.corXY(arr,i,j).shape)
                res[i,j]=covMatrix.corXY(arr,i,j)[0]
        return res

    meanRow=staticmethod(meanRow)
    #meanr=staticmethod(meanr)
    cov=staticmethod(cov)
    corXY=staticmethod(corXY)
    cor=staticmethod(cor)


