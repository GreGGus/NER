import os

from nltk.tag.stanford import StanfordNERTagger


classifier_path='/home/gregoire.portier/NER/NER/python/classifier/english.muc.7class.distsim.crf.ser.gz'
jar_path='/home/gregoire.portier/NER/NER/python/classifier/stanford-ner.jar'
st = StanfordNERTagger(classifier_path,jar_path)

st.tag('Rami Eid is studying at Stony Brook University in NY'.split())


