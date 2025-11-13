from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize     #nltk is a toolkit having library as tokenize which has module/function as sent_tokenize, word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize import TreebankWordTokenizer
corpus = """
Hello Raj ! How are you? Hope you are fine, how's the life going , are you happy? You're still creative enough. I guess you are enjoying your work at office.
"""

sentence = sent_tokenize(corpus)   #prints the sentences in the corpus as a list of sentences, (list is seperated by punctuation marks like . ? ! )
print("sentence tokenize \n",sentence)

word  = word_tokenize(corpus) #each word and punctuation is considered as a separate token apostrophe is considered as a part of the word
print("\n\n\n WORD TOKENIZE")
print(word)

print("\n\n\nWordPunct Tokenize") #appostrophe is also considered as a separate token
punkt_ = wordpunct_tokenize(corpus)  
print(punkt_)

treebank = TreebankWordTokenizer() #each fullstop is considered as the same token along with word except the last fullstop

full_st = treebank.tokenize(corpus)

print("\n\n\n TreebankWordTokenizer")
print(full_st)