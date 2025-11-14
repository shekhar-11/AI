#This basically takes a singular regular expression and removes any suffix or prefix defined on the expression

from nltk.stem import RegexpStemmer

stem = RegexpStemmer("ing$|es$|s$|ed$|ly$")

print(stem.stem("running"))
print(stem.stem("played"))