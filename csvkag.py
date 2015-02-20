import csv
import numpy as np
class csvkag:
    #init
    def __init__(self):
        self.csvname="";
        self.csvlist=[]
        self.npcsvid=np.array([],dtype=np.intc)

    #add input csv
    def addInput(self,myin):
        self.csvname=myin
        with open(myin,'rb') as csvfile:
            csvtemp=csv.reader(csvfile, delimiter=',')
            for row in csvtemp:
                self.csvlist.append(row)
        print(len(self.csvlist))
        self.cutHead()

    # cut head and since kaggle 
    def cutHead(self):
        del self.csvlist[0]

    #generate unique id
    def genUniqueId(self):
        nindex=0
        dicttemp={}
        for i in self.csvlist:
            if i[1] in dicttemp:
                print(i[1]+" already there")
                self.npcsvid=np.append(self.npcsvid,dicttemp[i[1]])
            else:
                dicttemp[i[1]]=nindex
                self.npcsvid=np.append(self.npcsvid,nindex)
                nindex+=1
            print(i[1],dicttemp[i[1]])

        
