import pandas as pd


#first is to load data
file = pd.read_csv('/home/rajs11/I_CODE/26/AI/Practice/spam.csv',encoding='latin1')

# print(file)

file = file[['v1','v2']]  #this is making the column headings as v1 and v2
file.columns = ['label','messages'] #replaces v1== label , v2 = messages
# print(file)


import re
import nltk as nt
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords


porterObj = PorterStemmer()

para = []

for i in range(0,len(file)):
    alphabets = re.sub(r'[^a-zA-Z]', ' ', file['messages'][i])
    alphabets = alphabets.lower()
    alphabets = alphabets.split()
    alphabets = [porterObj.stem(word) for word in alphabets if not word in stopwords.words('english')]
    alphabets = ' '.join(alphabets)
    para.append(alphabets)



from sklearn.feature_extraction.text import CountVectorizer

countvec = CountVectorizer(max_features=2000,binary=False)

countvec.fit(para)
trs = countvec.transform(para)

trs = trs.toarray()
print(trs)