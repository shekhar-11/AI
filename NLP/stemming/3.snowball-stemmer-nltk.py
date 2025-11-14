#it is the improvement of porter stemmer and it overcomes the limitation of porter stemmer (not completely but somewhat)

from nltk.stem.snowball import SnowballStemmer

stem_____ = SnowballStemmer("english")  #provides for multiple languages


print(stem_____.stem("running"))



#differs from porter is for examply in sportingly word 

from nltk.stem import PorterStemmer
portstem = PorterStemmer()
print("PORTER-----------",portstem.stem("sportingly"))  #porterstemmer gives sportili
print("SNOWBALL---------",stem_____.stem("sportingly")) #snowball stemmer gives sporting