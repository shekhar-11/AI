
import pandas as pd



#Step 1 ---  data entry
messages = pd.read_csv(
    '/home/rajs11/I_CODE/26/AI/Text-2-Vector/BOW/spam.csv',
    encoding='latin1'                       #utf-8 is giving error as there are different characters
)

messages = messages[['v1', 'v2']]                   #it has 2 labels as v1 v2 for each column
messages.columns = ['label', 'message']             #forcefully setting the labels

print(messages)




#step 2 --  data cleaning and preprocessing
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

ps = PorterStemmer()


corpus = []             #post cleaning the final will be stored here
