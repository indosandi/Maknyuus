import numpy as np

class covMatrix:

    #return 2d mean matrix by row
    #@staticmethod
    def meanr(arr):
        #1d array of mean of row
        mean1d=arr.mean(axis=0)
        #2d  1xn of mean of row jk 
        mean1ds=np.reshape(mean1d,(1,mean1d.shape[0]))
        nrow=arr.shape[0]
        one=np.ones((nrow,1))
        return np.dot(one,mean1ds)

    #return covariance matrix
    def cov(arr):
        nTrainsize=arr.shape[0]
        meanX=covMatrix.meanr(arr)
        xTilde=arr-meanX
        return np.dot(xTilde.T,xTilde)/nTrainsize
    
    meanr=staticmethod(meanr)
    cov=staticmethod(cov)


