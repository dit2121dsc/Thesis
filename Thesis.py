import json
import os
import spacy
import os.path

from cso_classifier import CSOClassifier

cc = CSOClassifier(modules="both", enhancement="first", explanation=False)

nlp = spacy.load("en_core_web_sm")
new_ruler = nlp.add_pipe("entity_ruler").from_disk("./additional.jsonl")

directory = 'JSON_IN'
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

        if os.path.isfile(expfname):
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

                ner_result = cc.run(paper)
                doc = nlp(paper)

         #   print(list(set([e.text for e in doc.ents if e.label_ == "Metrics"])))

           # for ent in doc.ents:
                ner_result["Metrics"] = list(set([e.text for e in doc.ents if e.label_ == "Metrics"]))
                ner_result["ProgLang"] = list(set([e.text for e in doc.ents if e.label_ == "ProgLang"]))
                ner_result["Dataset"] = list(set([e.text for e in doc.ents if e.label_ == "Dataset"]))
                ner_result["MathTerm"] = list(set([e.text for e in doc.ents if e.label_ == "MathTerm"]))
                ner_result["IT Framework"] = list(set([e.text for e in doc.ents if e.label_ == "IT Framework"]))
                ner_result["ISO"] = list(set([e.text for e in doc.ents if e.label_ == "ISO"]))
                ner_result["Technology"] = list(set([e.text for e in doc.ents if e.label_ == "Technology"]))
                ner_result["Terms"] = list(set([e.text for e in doc.ents if e.label_ == "Terms"]))

                # Collect all entities that are uppercase or have the first letter capitalized

                entities_before_dataset = []

                datasets = [token.i for token in doc if token.lemma_ == "dataset"]
                #print(datasets)
                if  datasets!=[]:
                    for ent in doc.ents:
                        if len(ent.text) > 1:
                        # Check if the entity is a word with its first letter capitalized
                            if (ent.text[0].isupper() or ent.text[1].isupper()) and any(
                                (dataset_index - 5 < ent.start) and (dataset_index > ent.start) for dataset_index in
                                datasets):                            entities_before_dataset.append(ent.text)
                        #if entities_before_dataset != []:  print("Entities before 'dataset':", entities_before_dataset)

                datasets = [token.i for token in doc if token.lemma_ == "technology"]
                #print(datasets)
                if datasets!=[]:
                    for ent in doc.ents:
                        # Check if the entity is a word with its first letter capitalized
                        #if ent.text[0].isupper() and any(dataset_index > (ent.start+2) for dataset_index in datasets):
                        if len(ent.text) > 1:
                            if (ent.text[0].isupper() or ent.text[1].isupper()) and any((dataset_index - 5 < ent.start) and (dataset_index > ent.start) for dataset_index in datasets):
                                entities_before_dataset.append(ent.text)
                 #   if entities_before_dataset != []:  print("Entities before 'dataset':", entities_before_dataset)

                datasets = [token.i for token in doc if token.lemma_ == "classifier"]
                #print(datasets)
                if datasets!=[]:
                    for ent in doc.ents:
                        # Check if the entity is a word with its first letter capitalized
                        if len(ent.text) > 1:
                            if (ent.text[0].isupper() or ent.text[1].isupper()) and any(
                                (dataset_index - 5 < ent.start) and (dataset_index > ent.start) for dataset_index in
                                datasets):                            entities_before_dataset.append(ent.text)
                 #   if entities_before_dataset != []:  print("Entities before 'dataset':", entities_before_dataset)

                datasets = [token.i for token in doc if token.lemma_ == "model"]
                #print(datasets)
                if datasets!=[]:
                    for ent in doc.ents:
                        # Check if the entity is a word with its first letter capitalized
                        if len(ent.text) > 1:
                            if (ent.text[0].isupper() or ent.text[1].isupper()) and any(
                                (dataset_index - 5 < ent.start) and (dataset_index > ent.start) for dataset_index in
                                datasets):                            entities_before_dataset.append(ent.text)

                ner_result["TechName"] = entities_before_dataset
                if entities_before_dataset!=[]:  print("Entities before 'dataset':", entities_before_dataset)

            #fnl_List.append([(ent.label_) for ent in doc.ents])
              #  print([(ent.text, ent.label_) for ent in doc.ents])
           # print(ner_result)

                fnl_List.append(ner_result)

                data['ner'] = fnl_List

            # Convert and write JSON object to file

                with open(expfname, "w") as outfile:
                    json.dump(data, outfile)
