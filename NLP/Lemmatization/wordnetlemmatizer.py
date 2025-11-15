from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

# lemmatizer.lemmatize(word,pos)
# #pos ===>
# Noun- n
# verb - v
# adverb = r
# adjective = a
print("NOUN--- ",lemmatizer.lemmatize("going",'n'))
print("VERB--- ",lemmatizer.lemmatize("going",'v'))
print("Adjective--- ",lemmatizer.lemmatize("going",'a'))
print("Adverb ----",lemmatizer.lemmatize("going",'r'))

print("/n/n/n")


words = "Researchers were observing how different animals behaved while moving through varied environments , collecting samples and recording changes carefully . They attempted to analyze patterns , compare results , and develop meaningful insights that could help improve future studies . Despite facing challenges , the team kept working consistently to achieve accurate , reliable scientific outcomes ."
listOfWords = words.split(" ")
# print(listOfWords)
for word in listOfWords:
    if len(word)>1:
        print(lemmatizer.lemmatize("carefully",'r'))


