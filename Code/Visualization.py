# import spacy
# from spacy import displacy
#
# text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."
#
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# displacy.serve(doc, style="ent")


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = """In ancient Rome, some neighbors live in three adjacent houses. In the center is the house of Senex, who lives there with wife Domina, son Hero, and 
several slaves, including head slave Hysterium and the musical's main character Pseudolus. A slave belonging to Hero, Pseudolus wishes to buy, win, or 
steal his freedom. One of the neighboring houses is owned by Marcus Lycus, who is a buyer and seller of beautiful women; the other belongs to the ancient 
Erronius, who is abroad searching for his long-lost children (stolen in infancy by pirates). One day, Senex and Domina go on a trip and leave Pseudolus in 
charge of Hero. Hero confides in Pseudolus that he is in love with the lovely Philia, one of the courtesans in the House of Lycus (albeit still a virgin)."""


doc = nlp(text)


sentence_spans = list(doc.sents)
displacy.serve(sentence_spans, style="ent")


