import csv
import numpy as np
class csvkag:

    #init
    def __init__(self):
        self.csvname=""
        self.csvlist=[]
        self.dit={}
        self.npcsvid=np.array([],dtype=np.intc)

    #get key
    def getKey(self,myinarr):
        res=[]
        for myin in myinarr:
            for key in self.dit.keys():
                if self.dit[key] == myin:
                    res.append(key)
                    break
        return res

    #for kaggle
    def wrtCsv(self,noId,arr):
        str1="ID"
        str2="Class"
        f = open('result.csv', 'w')
        f.write(str1+","+str2+"\n")
        index=0
        for i in noId:
            #print(i)
            f.write(str(i)+","+arr[index]+"\n")
            index+=1
        f.close()

    #add input csv
    def addInput(self,myin):
        self.csvname=myin
        with open(myin,'rb') as csvfile:
            csvtemp=csv.reader(csvfile, delimiter=',')
            for row in csvtemp:
                self.csvlist.append(row)
        #print(len(self.csvlist))
        self.cutHead()

    # cut head and since kaggle 
    def cutHead(self):
        del self.csvlist[0]
        #print(len(self.csvlist))
        self.npcsvid=np.zeros(len(self.csvlist),dtype=np.intc)
        self.npcsvid=np.zeros(len(self.csvlist),dtype=np.intc)
        self.genUniqueId()

    #generate unique id
    def genUniqueId(self):
        nindex=0
        dicttemp={}
        inc=0
        for i in self.csvlist:
            if i[1] in dicttemp:
                #print(i[1]+" already there")
                #self.npcsvid[inc]=np.append(self.npcsvid,dicttemp[i[1]])
                self.npcsvid[inc]=dicttemp[i[1]]
            else:
                dicttemp[i[1]]=nindex
                #self.npcsvid[inc]=np.append(self.npcsvid,nindex)
                self.npcsvid[inc]=nindex
                nindex+=1
            #print(inc)
            inc+=1
            #print(i[1],dicttemp[i[1]])
        self.dit=dicttemp

        
