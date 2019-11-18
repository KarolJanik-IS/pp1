#38
import re
def WielkieLitery(ciag):
    test = re.findall('[A-Z-ŻŹĆĄŚĘŁÓŃ]',ciag)
    return test
    #print(test)
print(WielkieLitery("TestowyCiągZNAKÓW"))