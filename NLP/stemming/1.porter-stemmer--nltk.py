import nltk as nt

from nltk.stem import PorterStemmer

portstem = PorterStemmer()


words = ["running","run","runner","easily","fairly","fairness","cats","catlike","connected","connection","connections","congratulations"]

for word in words:
    print(word,"-->",portstem.stem(word))




