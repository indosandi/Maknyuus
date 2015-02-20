from csvkag import csvkag
csvT=csvkag()
csvT.addInput('trainLabels.csv')
print(csvT.npcsv.shape)
csvT.genUniqueId()
print(csvT.npcsvid.shape)
print(csvT.npcsvid[6282])
