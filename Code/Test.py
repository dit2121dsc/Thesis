# Example input text

import json
import os
import spacy
import os.path


# Load the English tokenizer, tagger, parser, NER and word vectors

nlp = spacy.load("en_core_web_sm")


directory = 'Input'
exp_directory = 'EXP_NER'
for filename in os.scandir(directory):
    print(filename.name)
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
#text = "The COCO dataset is widely used. The Pascal Dataset is also important. Another example is the IMAGENET dataset. The TextClassification DATASET provides various data. """
# Process the text
#import spacy

#nlp = spacy.load("en_core_web_sm")
#doc = nlp(text)
# Collect all occurrences of "dataset" (case insensitive)
#
            datasets = [token.i for token in doc if token.lemma_ == "dataset"] # Collect all entities that are uppercase or have the first letter capitalized
            print(datasets)
            entities_before_dataset = []
            for dataset_index in datasets:
                print(dataset_index)
                for ent in doc.ents:
            # Check if the entity is a word with its first letter capitalized or fully uppercase
                    print(ent.text + ' st ' + str(ent.start))
                    if ent.text[0].isupper() and (dataset_index - 5 < ent.start) and (dataset_index > ent.start):
              #  if ent.text[0].isupper() and any((dataset_index - 4 < ent.start) and (dataset_index > ent.start) for dataset_index in datasets):
                        entities_before_dataset.append(ent.text)
            if entities_before_dataset != []:
                print("Entities before 'dataset':", entities_before_dataset)
                print("All 'dataset' occurrences:", [doc[dataset_index].text for dataset_index in datasets])