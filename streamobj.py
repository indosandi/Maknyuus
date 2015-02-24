import pickle
class streamobj:
    #save object to file
    def saveMe(obj,str):
        with open(str,'wb') as output:
            pickle.dump(obj,output,pickle.HIGHEST_PROTOCOL)

    #load obj
    def loadMe(str):
        with open(str,'rb') as input:
            tmpObj=pickle.load(input)
        return tmpObj
    saveMe=staticmethod(saveMe)
    loadMe=staticmethod(loadMe)
