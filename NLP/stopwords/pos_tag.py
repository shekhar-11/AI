# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('averaged_perceptron_tagger_eng')


#below are the pos tags ---
# """
# "CC coordinating conjunction \n",
#     "CD cardinal digit \n",
#     "DT determiner \n",
#     "EX existential there (like: “there is” … think of it like “there exists”) \n",
#     "FW foreign word \n",
#     "IN preposition/subordinating conjunction \n",
#     "JJ adjective – ‘big’ \n",
#     "JJR adjective, comparative – ‘bigger’ \n",
#     "JJS adjective, superlative – ‘biggest’ \n",
#     "LS list marker 1) \n",
#     "MD modal – could, will \n",
#     "NN noun, singular ‘- desk’ \n",
#     "NNS noun plural – ‘desks’ \n",
#     "NNP proper noun, singular – ‘Harrison’ \n",
#     "NNPS proper noun, plural – ‘Americans’ \n",
#     "PDT predeterminer – ‘all the kids’ \n",
#     "POS possessive ending parent’s \n",
#     "PRP personal pronoun –  I, he, she \n",
#     "PRP$ possessive pronoun – my, his, hers \n",
#     "RB adverb – very, silently, \n",
#     "RBR adverb, comparative – better \n",
#     "RBS adverb, superlative – best \n",
#     "RP particle – give up \n",
#     "TO – to go ‘to’ the store. \n",
#     "UH interjection – errrrrrrrm \n",
#     "VB verb, base form – take \n",
#     "VBD verb, past tense – took \n",
#     "VBG verb, gerund/present participle – taking \n",
#     "VBN verb, past participle – taken \n",
#     "VBP verb, sing. present, non-3d – take \n",
#     "VBZ verb, 3rd person sing. present – takes \n",
#     "WDT wh-determiner – which \n",
#     "WP wh-pronoun – who, what \n",
#     "WP$ possessive wh-pronoun, eg- whose \n",
#     "WRB wh-adverb, eg- where, when"
# """




#Pos tag is to determine which parts of speech the word is 
from nltk import word_tokenize
from nltk import pos_tag


para = """In recent years, technology has become an essential part of everyday life, influencing how people communicate, work, and learn. Many individuals rely on digital devices to complete their daily tasks more efficiently, whether they are sending emails, attending online meetings, or searching for information on the internet. As technology continues to evolve, organizations are constantly adapting their processes to stay competitive in a rapidly changing environment. Employees are encouraged to develop new skills and improve their knowledge so that they can contribute effectively to their teams.

At the same time, excessive use of technology can lead to challenges such as reduced physical activity and increased stress. People often spend long hours staring at screens, which may affect their health and productivity. To maintain a healthy balance, it is important to manage time wisely and take regular breaks. Educational institutions are also integrating technology into classrooms to enhance learning experiences, making education more accessible to students across different regions. Overall, technology offers numerous benefits, but responsible usage is necessary to ensure long-term well-being and sustainable development."""


list_para = word_tokenize(para)

print(pos_tag(list_para,lang="eng"))








