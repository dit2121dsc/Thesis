#from transformers import AutoTokenizer, AutoModelForTokenClassification , AutoModel
#from transformers import pipeline

#tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
#model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
#nlp = pipeline("ner", model=model, tokenizer=tokenizer)
#example = "My name is Wolfgang and I live in Berlin"

#nlp = pipeline("token-classification", model=model, tokenizer=tokenizer)
#nlp = pipeline("token-classification", model = "RJuro/SciNERTopic" , aggregation_strategy="simple")
#example = "our goal is to learn task-independent representations of academic papers. Inspired by the recent success of pretrained Transformer language models across various NLP tasks, we use the Transformer model architecture as basis of encoding the input paper. Existing LMs such as BERT, however, are primarily based on masked language modeling objective, only considering intra-document context and do not use any inter-document information. This limits their ability to learn optimal document representations. To learn high-quality documentlevel representations we propose using citations as an inter-document relatedness signal and formulate it as a triplet loss learning objective. We then pretrain the model on a large corpus of citations using this objective, encouraging it to output representations that are more similar for papers that share a citation link than for those that do not. We call our model SPECTER, which learns Scientific Paper Embeddings using Citation-informed Trans-formERs. With respect to the terminology used by unlike most existing LMs that are , our approach results in embeddings that can be applied to downstream tasks in a fashion, meaning the learned paper embeddings can be easily used as features, with no need for further task-specific fine-tuning. In the following, as background information, we briefly describe how pretrained LMs can be applied for document representation and then discuss the details of SPECTER.</p><p>https://github.com/allenai/scidocs Transformer (initialized with SciBERT) Related paper (P + ) Query paper (P Q ) Unrelated paper (P − )"
#print(example)


#ner_results = nlp(example)
#print(len(ner_results))

#for x in range(len(ner_results)):
#    ner_results[x]['score']=str(ner_results[x]['score'])

# import required module
#import os

# assign directory
#directory = 'JSON_OUT'

# iterate over files in
# that directory
#for filename in os.scandir(directory):
#    if filename.is_file():
#        print(filename.name)

from cso_classifier import CSOClassifier as cc
cc.setup()
exit() # it is important to close the current console, to make those changes effective


#!/usr/bin/env python3


# In[Loading Libraries]:


# from cso_classifier import CSOClassifier
import spacy
import json

# In[Loading Paper]:

# nlp = spacy.load("en_core_web_sm")
#
# paper = {
#     "title": "De-anonymizing Social Networks",
#      "abstract": "Operators of online social networks are increasingly sharing potentially "
#                  "sensitive information about users and their relationships with advertisers, application "
#                  "developers, and data-mining researchers. Privacy is typically protected by anonymization, "
#                  "i.e., removing names, addresses, etc. We present a framework for analyzing privacy and "
#                  "anonymity in social networks and develop a new re-identification algorithm targeting "
#                  "anonymized social-network graphs. To demonstrate its effectiveness on real-world networks, "
#                  "we show that a third of the users who can be verified to have accounts on both Twitter, a "
#                  "popular microblogging service, and Flickr, an online photo-sharing site, can be re-identified "
#                  "in the anonymous Twitter graph with only a 12% error rate. Our de-anonymization algorithm is "
#                  "based purely on the network topology, does not require creation of a large number of dummy "
#                  "\"sybil\" nodes, is robust to noise and all existing defenses, and works even when the overlap "
#                  "between the target network and the adversary's auxiliary information is small.",
#      "keywords": "data mining, data privacy, graph theory, social networking (online)"
#  }
#
#  print(paper["title"])
#  print(paper["abstract"])
#  print(paper["keywords"])
#
#
#  # In[Run Classifier]
#
# cc = CSOClassifier(explanation=False)
#
# result = cc.run(paper)
#
# #nlp_text = nlp(paper["abstract"])
#
#
#
#  # In[Printing and Saving]:
#
# print(result)
#
#
#
# print ([token.text for token in nlp_text])
#
#
# with open('output.json', 'w') as outfile:
#     json.dump(result, outfile, indent=4)
# import spacy
from spacy.matcher import Matcher
import re

from spacy.lang.en import English
from spacy.pipeline import EntityRuler

# nlp = spacy.blank("en")
# new_ruler = nlp.add_pipe("entity_ruler")

# patterns=[{'label':'Syntactic','pattern': [{'': 'data mining techniques'}]}]

# patterns = [{"label":"Metrics","pattern":[{"text":"MAE"}]} , {"label":"Metrics","pattern":[{"text":"MSE"}]}]
# new_ruler.add_patterns(patterns)


# doc = nlp("The paper presents and compares the data mining techniques for selection of the diagnostic features in the problem of blood cell recognition in leukemia. Different techniques are compared, including the linear SVM ranking, correlation and statistical ISO 232232 analysis of centers and variances of clusters corresponding to different classes. We have applied radial kernel SVM as the classifier. The results of recognition of 10 classes of cells are presented and discussed. ")
# print([(ent.text, ent.label_) for ent in doc.ents])

# new_ruler.to_disk("./add22.jsonl")


# nlp = spacy.load("en_core_web_sm")
# matcher = Matcher(nlp.vocab)
# Add match ID "HelloWorld" with no callback and one pattern
# pattern = [{"TEXT": {"REGEX": "r'[ISO]\d+'"}}]
# pattern ={"LOWER": "hello"},  {"LOWER": "world"}

# pattern = [{"TEXT": {"REGEX":{"^awe(some)?$", "^wonder(ful)?"}}}]
# matcher.add("HelloWorld", [pattern])

# doc = nlp("Hello wOrld! ABC-123 Hello world!")
# expression = "r'[A-Z]+-\d+'"
# for match in re.finditer(expression, doc.text):
#     start, end = match.span()
#     span = doc.char_span(start, end)
#     # This is a Span object or None if match doesn't map to valid token sequence
#     if span is not None:
#         print("Found match:", span.text)
# print ("end")

# matches = matcher(doc)
# for match_id, start, end in matches:
#     string_id = nlp.vocab.strings[match_id]  # Get string representation
#     span = doc[start:end]  # The matched span
#     print(match_id, string_id, start, end, span.text)


#
from spacy.lang.en import English

#
nlp = English()
#ruler = nlp.add_pipe("entity_ruler")
#patterns = [{'label': 'MathTerm', 'pattern': [{'text': 'Markov'}]},
#            {'label': 'MathTerm', 'pattern': [{'text': 'Monte'}, {'text': 'Carlo'}]},
#            {'label': 'Terms', 'pattern': [{'lower': 'CIFAR-10'}]}, {'label': 'Terms', 'pattern': [{'lower': 'MCMC'}]},
#            {'label': 'Terms', 'pattern': [{'lower': 'CIFAR-100'}]}, {'label': 'Terms', 'pattern': [{'lower': 'SVHN'}]}]
#
#
#ruler.add_patterns(patterns)
# ruler.to_disk("./add2.jsonl")
#
doc1 = nlp(
    " The vulnerability of deep networks to adversarial attacks is a central problem for deep learning from the perspective of both cognition and security. The current most successful defense method is to train a classifier using adversarial images created during learning. Another defense approach involves transformation or purification of the original input to remove adversarial signals before the image is classified. We focus on defending naturally-trained classifiers using Markov Chain Monte Carlo (MCMC) sampling with an Energy-Based Model (EBM) for adversarial purification. In contrast to adversarial training, our approach is intended to secure highly vulnerable pre-existing classifiers. To our knowledge, no prior defensive transformation is capable of securing naturally-trained classifiers, and our method is the first to validate a post-training defense approach that is distinct from current successful defenses which modify classifier training. The memoryless behavior of long-run MCMC sampling will eventually remove adversarial signals, while metastable behavior preserves consistent appearance of MCMC samples after many steps to allow accurate long-run prediction. Balancing these factors can lead to effective purification and robust classification. We evaluate adversarial defense with an EBM using the strongest known attacks against purification. Our contributions are 1) an improved method for training EBM's with realistic long-run MCMC samples for effective purification, 2) an Expectation-Over-Transformation (EOT) defense that resolves ambiguities for evaluating stochastic defenses and from which the EOT attack naturally follows, and 3) state-of-the-art adversarial defense for naturally-trained classifiers and competitive defense compared to adversarial training on CIFAR-10, SVHN, and CIFAR-100. ")
print([(ent.text, ent.label_, ent.ent_id_) for ent in doc1.ents])

# import json
# import os
#
# directory = 'EXP_NER'
#
# for filename in os.scandir(directory):
#
#     fname = directory + "/" + filename.name
#
#     with open(fname, "r") as read_file:
#         data = json.load(read_file)
#
#         cnt = len(data['ner'][0]['Dataset']) + len(data['ner'][0]['Metrics']) + len(data['ner'][0]['ISO']) + len(
#             data['ner'][0]['ProgLang']) + len(data['ner'][0]['Dataset Name']) + len(data['ner'][0]['MathTerm']) + len(
#             data['ner'][0]['IT Framework']) + len(data['ner'][0]['Terms'])
#
#         if cnt>5:
#             print(filename.name)
#             print(cnt)
#
#
#

import json
import os
import spacy
import os.path


# Load the English tokenizer, tagger, parser, NER and word vectors

nlp = spacy.load("en_core_web_sm")


directory = 'JSON_IN'
exp_directory = 'EXP_NER'
for filename in os.scandir(directory):
    #print(filename.name)
    data =[]
    text =''
    paper =''
    if filename.is_file() and filename.name.endswith('.json'):
        fname = directory + "/" + filename.name
        expfname = exp_directory + "/NER_" + filename.name
        #print(fname)

        if 2<1:
            print ('found')
        else:
            with open(fname, "r") as read_file:
                data = json.load(read_file)

                # Process each file and append results in directory
                fnl_List = []

                for x in range(len(data['pdf_parse']['abstract'])):
                    text = data['pdf_parse']['abstract'][x]['text']
                    paper = text + ' ' + paper

            #for x in range(len(data['pdf_parse']['body_text'])):
             #   text = data['pdf_parse']['body_text'][x]['text']
              #  paper = text + ' ' + paper

            # Perform linguistic analysis using SpaCy
            doc = nlp(paper)

            # Identify any term that exists prior to the word "Model"
            terms_prior_to_model = []
            for token in doc:
                if token.text.lower() == "dataset":
                    for ancestor in token.ancestors:
                        if ancestor.text != " ":
                            terms_prior_to_model.append(ancestor.text)

            # Display the identified terms
           # if len(terms_prior_to_model) > 0:
              #  print("Terms that exist prior to the word 'Dataset':", terms_prior_to_model)


            # Initialize a variable to find the leading word "Dataset"
            leading_word = "dataset"
            found_leading_word = False

            # Analyze the document for named entities prior to "Dataset"
            for token in doc:
                if token.text == leading_word:
                    found_leading_word = True
                    #print(f"Leading word: {token.text}")
                    #print(f"Lemma: {token.lemma()}")
                    #print(f"POS: {token.pos_}")
                    #print(f"Tag: {token.tag_}")
                    #print(f"Dependency: {token.dep_}")
                    #print(f"Shape: {token.shape_}")
                    #print(f"Is alpha: {token.is_alpha}")
                    #print(f"Is stop: {token.is_stop}")
                    #break

            # Look for named entities prior to the leading word "Dataset"
            #if found_leading_word:
                    for ent in doc.ents:
                        if ent.end < token.i:  # Check if the entity ends before the leading word's index
                            print("\nNamed Entities prior to the leading word:")
                            print(f"Entity: {ent.text}, Label: {ent.label_}")





