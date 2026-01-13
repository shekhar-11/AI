
from nltk.tokenize import *


paragraph = """In recent years, technology has become an essential part of everyday life, influencing how people communicate, work, and learn. Many individuals rely on digital devices to complete their daily tasks more efficiently, whether they are sending emails, attending online meetings, or searching for information on the internet. As technology continues to evolve, organizations are constantly adapting their processes to stay competitive in a rapidly changing environment. Employees are encouraged to develop new skills and improve their knowledge so that they can contribute effectively to their teams.

At the same time, excessive use of technology can lead to challenges such as reduced physical activity and increased stress. People often spend long hours staring at screens, which may affect their health and productivity. To maintain a healthy balance, it is important to manage time wisely and take regular breaks. Educational institutions are also integrating technology into classrooms to enhance learning experiences, making education more accessible to students across different regions. Overall, technology offers numerous benefits, but responsible usage is necessary to ensure long-term well-being and sustainable development."""

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
portstem = PorterStemmer()
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
sentences = sent_tokenize(paragraph)

for i in range(len(sentences)):
    words = word_tokenize(sentences[i])
    newWords = []
    for j in range(len(words)):
        if words[j] not in set(stopwords.words('english')):
            words[j] = portstem.stem(words[j])
            newWords.append(words[j])
            
    sentences[i] = ' '.join(newWords)


print(sentences)
           


#use from nltk.stem import WordNetLemmatizer

#lemmatizer = WordNetLemmatizer() for lemmatization