import nltk as nltk


para = "The Taj Mahal is a beautiful place. This monument is present in Agra ."


tag_elem = nltk.pos_tag(para.split())

print(nltk.ne_chunk(tag_elem))



#the tagged element means they can be person, location, time ,organization....... specified in this way



