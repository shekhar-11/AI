import nltk as nt


para = """Natural Language Processing (NLP) is a branch of artificial 
intelligence that deals with the interaction between computers and human languages. 
It enables machines to read, interpret, and generate text in a way that is both meaningful and contextually relevant.
 Tokenization is often the very first step — breaking down text into sentences or words for further analysis."""



sentences = nt.tokenize.sent_tokenize(para)
print("-----------------Tokenizing the para to sentence-----------------------")
# print(sentences)

# for sentence in sentences:
    # print(sentence)
print("\n\n\n")
sentences = ",".join(sentences)

words = nt.tokenize.word_tokenize(para)
print(words)



punkt_words = nt.tokenize.wordpunct_tokenize(para)
print("/n/n/n------------__WORD PUNCT (CONSIDERS PUNCTUATION AS TOKENS )")
print(punkt_words)


fullst = nt.tokenize.TreebankWordTokenizer().tokenize(para)
print("\n\n\n--------------_FULLSTOP--------------------------")
print(fullst)