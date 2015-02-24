from streamobj import streamobj
from csvkag import csvkag
csvT=csvkag()
csvT.addInput('trainLabels.csv')
csvT.genUniqueId()
print(csvT.npcsvid.shape)
#print(csvT.npcsvid[6282])
#print(len(csvT.csvlist))
streamobj.saveMe(csvT,"trainLabel.obj")
