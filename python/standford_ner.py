import os

from nltk.tag.stanford import NERTagger


classifier_path='/home/gregoire.portier/NER/NER/python/classifier/all.3class.distsim.crf.ser.gz'
jar_path='/home/gregoire.portier/NER/NER/python/classifier/stanford-ner.jar'
st = NERTagger(classifier_path,jar_path)

st.tag('Rami Eid is studying at Stony Brook University in NY'.split())


