
import pandas as pd



#Step 1 ---  data entry
messages = pd.read_csv(
    '/home/rajs11/I_CODE/26/AI/Text-2-Vector/BOW/spam.csv',
    encoding='latin1'                       #utf-8 is giving error as there are different characters
)

messages = messages[['v1', 'v2']]                   #it has 2 labels as v1 v2 for each column
messages.columns = ['label', 'message']             #forcefully setting the labels

# print(messages)




#step 2 --  data cleaning and preprocessing
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

ps = PorterStemmer()


corpus = []             #post cleaning the final will be stored here



"""
#################################################################################################################
                                        GO THROUGH EACH AND EVERY SENTENCES
                                        REMOVE ALL THE SPECIAL CHARACTERS
                                        LOWER DOWN
                                        APPLY STOPWORDS
                                        APPLY STEMMING / LEMMATIZATION
#################################################################################################################
"""



for i in range(0,len(messages)):
    review = re.sub('[^a-zA-Z]',' ',messages['message'][i])  #replace all the char other than alphabets with ' ' and this has to be applied for all the messages under lable message
    review = review.lower()
    review = review.split()     #list of words
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
    # print(review)


# print(corpus)






#vectorization

####################################   COUNTVECTORIZER   ###################################
"""
class sklearn.feature_extraction.text.CountVectorizer(*, input='content', encoding='utf-8',
 decode_error='strict', strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None,
   stop_words=None, token_pattern='(?u)\\b\\w\\w+\\b', ngram_range=(1, 1), analyzer='word',
     max_df=1.0, min_df=1, max_features=None, vocabulary=None, binary=False, dtype=<class 'numpy.int64'>)[source]

     
     so this provides , binary /normal -bow, lowercase directly, stopwords .....
"""

from sklearn.feature_extraction.text import CountVectorizer


CV = CountVectorizer(max_features=2500,binary=True)         #top 2500 frequent words(as already explained we take top frequent words)







###################### FIT_TRANSFORM ----fit - learns from vocab, the unique words, transform -- to convert to numbers  ##################
X = CV.fit_transform(corpus) 

"""
corpus
  ↓
fit() → learn vocabulary
  ↓
transform() → text → numbers
  ↓
X (numerical matrix)
"""




X = X.toarray()
print(X)

