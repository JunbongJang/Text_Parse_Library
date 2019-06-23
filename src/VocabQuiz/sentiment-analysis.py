import spacy
nlp = spacy.load('en_core_web_lg')
print(nlp('lion').vector)