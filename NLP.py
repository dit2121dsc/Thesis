# for y in range (len(itlist)):
#   print (itlist[y])
#  tmp.append({"lower": itlist[y]  })
# if y+1 < len(itlist): tmp+=','
# {"lower":"root"},{"lower":"mean"},{"lower":"squared"},{"lower":"error"}
# print(tmp)
# patterns.append({'label': 'Syntactic', 'pattern':[tmp]})
#patterns = [{"label":"Metrics","pattern":[{"text":"MAE"}]} , {"label":"Metrics","pattern":[{"text":"MSE"}]}]
       # patterns = [{"label": "Syntactic", "pattern": [{"text": "3d printers"}]}]



   # patterns = "["

import spacy
from spacy.pipeline import EntityRuler
import json
import os
import spacy
import os.path
from spacy import displacy
from pathlib import Path

nlp = spacy.blank("en")
new_ruler = nlp.add_pipe("entity_ruler")


directory = 'EXP_NER'
for filename in os.scandir(directory):
    if os.path.isfile("images/IMG_" + filename.name + ".html"):
        print('found')
        continue
    print(filename.name)
    paper = ''
    patterns = []
    tmp = ''
    data = []
    text = ''
    itlist = []
 #   new_ruler.clear()
    if filename.is_file() and filename.name.endswith('.json'):
        fname = directory + "/" + filename.name

        with open(fname, "r") as read_file:
            data = json.load(read_file)

        # Process each file and append results in directory
        fnl_List = []

        for x in range(len(data['pdf_parse']['abstract'])):
            text = data['pdf_parse']['abstract'][x]['text']
            paper =  paper + ' ' + text

        # ------------- Union/CSO ----------------
        for x in range(len(data['ner'][0]['union'])):
            #print(len(data['ner'][0]['syntactic'][x].split()))
            if len(data['ner'][0]['union'][x].split())>1:
                itlist = data['ner'][0]['union'][x].split()
                if len(data['ner'][0]['union'][x].split())==5:
                    patterns.append({'label': 'CSO', 'pattern': [{"lower":  itlist[0]},{"lower":  itlist[1]},{"lower":  itlist[2]},{"lower":  itlist[3]},{"lower":  itlist[4]}]})
                if len(data['ner'][0]['union'][x].split())==4:
                    patterns.append({'label': 'CSO', 'pattern': [{"lower":  itlist[0]},{"lower":  itlist[1]},{"lower":  itlist[2]},{"lower":  itlist[3]}]})
                if len(data['ner'][0]['union'][x].split())==3:
                    patterns.append({'label': 'CSO', 'pattern': [{"lower":  itlist[0]},{"lower":  itlist[1]},{"lower":  itlist[2]}]})
                if len(data['ner'][0]['union'][x].split())==2:
                    patterns.append({'label': 'CSO', 'pattern': [{"lower":  itlist[0]},{"lower":  itlist[1]}]})
            else:
                patterns.append({"label": "CSO", "pattern":[{"lower":  data['ner'][0]['union'][x]}]})

    #-------------Metrics -------------
    for x in range(len(data['ner'][0]['Metrics'])):
        # print(len(data['ner'][0]['syntactic'][x].split()))
        if len(data['ner'][0]['Metrics'][x].split()) > 1:
            itlist = data['ner'][0]['Metrics'][x].split()
            if len(data['ner'][0]['Metrics'][x].split()) == 5:
                patterns.append({'label': 'Metrics',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}, {"lower": itlist[4]}]})
            if len(data['ner'][0]['Metrics'][x].split()) == 4:
                patterns.append({'label': 'Metrics',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}]})
            if len(data['ner'][0]['Metrics'][x].split()) == 3:
                patterns.append(
                    {'label': 'Metrics', 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]}]})
            if len(data['ner'][0]['Metrics'][x].split()) == 2:
                patterns.append({'label': 'Metrics', 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}]})
        else:
            patterns.append({"label": "Metrics", "pattern": [{"lower": data['ner'][0]['Metrics'][x]}]})


    #-------------ProgLang =-------------
    for x in range(len(data['ner'][0]['ProgLang'])):
        # print(len(data['ner'][0]['syntactic'][x].split()))
        if len(data['ner'][0]['ProgLang'][x].split()) > 1:
            itlist = data['ner'][0]['ProgLang'][x].split()
            if len(data['ner'][0]['ProgLang'][x].split()) == 5:
                patterns.append({'label': 'ProgLang',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}, {"lower": itlist[4]}]})
            if len(data['ner'][0]['ProgLang'][x].split()) == 4:
                patterns.append({'label': 'ProgLang',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}]})
            if len(data['ner'][0]['ProgLang'][x].split()) == 3:
                patterns.append({'label': 'ProgLang',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]}]})
            if len(data['ner'][0]['ProgLang'][x].split()) == 2:
                patterns.append({'label': 'ProgLang', 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}]})
        else:
            patterns.append({"label": "ProgLang", "pattern": [{"lower": data['ner'][0]['ProgLang'][x]}]})


    #-------------Dataset =-------------
    for x in range(len(data['ner'][0]['Dataset'])):
        # print(len(data['ner'][0]['syntactic'][x].split()))
        if len(data['ner'][0]['Dataset'][x].split()) > 1:
            itlist = data['ner'][0]['Dataset'][x].split()
            if len(data['ner'][0]['Dataset'][x].split()) == 5:
                patterns.append({'label': 'Dataset',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}, {"lower": itlist[4]}]})
            if len(data['ner'][0]['Dataset'][x].split()) == 4:
                patterns.append({'label': 'Dataset',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}]})
            if len(data['ner'][0]['Dataset'][x].split()) == 3:
                patterns.append({'label': 'Dataset',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]}]})
            if len(data['ner'][0]['Dataset'][x].split()) == 2:
                patterns.append({'label': 'Dataset', 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}]})
        else:
            patterns.append({"label": "Dataset", "pattern": [{"lower": data['ner'][0]['Dataset'][x]}]})

    # -------------MathTerm =-------------
    for x in range(len(data['ner'][0]['MathTerm'])):

        if len(data['ner'][0]['MathTerm'][x].split()) > 1:
            itlist = data['ner'][0]['MathTerm'][x].split()
            if len(data['ner'][0]['MathTerm'][x].split()) == 5:
                patterns.append({'label': 'MathTerm',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}, {"text": itlist[4]}]})
            if len(data['ner'][0]['MathTerm'][x].split()) == 4:
                patterns.append({'label': 'MathTerm',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}]})
            if len(data['ner'][0]['MathTerm'][x].split()) == 3:
                patterns.append({'label': 'MathTerm',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]}]})
            if len(data['ner'][0]['MathTerm'][x].split()) == 2:
                patterns.append({'label': 'MathTerm', 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}]})
        else:
            patterns.append({"label": "MathTerm", "pattern": [{"text": data['ner'][0]['MathTerm'][x]}]})

    # -------------IT Framework =-------------
    for x in range(len(data['ner'][0]['IT Framework'])):

        if len(data['ner'][0]['IT Framework'][x].split()) > 1:
            itlist = data['ner'][0]['IT Framework'][x].split()
            if len(data['ner'][0]['IT Framework'][x].split()) == 5:
                patterns.append({'label': 'IT Framework',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}, {"text": itlist[4]}]})
            if len(data['ner'][0]['IT Framework'][x].split()) == 4:
                patterns.append({'label': 'IT Framework',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}]})
            if len(data['ner'][0]['IT Framework'][x].split()) == 3:
                patterns.append({'label': 'IT Framework',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]}]})
            if len(data['ner'][0]['IT Framework'][x].split()) == 2:
                patterns.append({'label': 'IT Framework', 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}]})
        else:
            patterns.append({"label": "IT Framework", "pattern": [{"text": data['ner'][0]['IT Framework'][x]}]})

    # -------------ISO-------------
    for x in range(len(data['ner'][0]['ISO'])):
        if len(data['ner'][0]['ISO'][x].split()) > 1:
            itlist = data['ner'][0]['ISO'][x].split()
            if len(data['ner'][0]['ISO'][x].split()) == 2:
                patterns.append({'label': 'ISO', 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}]})
        else:
            patterns.append({"label": "ISO", "pattern": [{"lower": data['ner'][0]['ISO'][x]}]})

    # -------------TechName-------------
    for x in range(len(data['ner'][0]['TechName'])):

        if len(data['ner'][0]['TechName'][x].split()) > 1:
            itlist = data['ner'][0]['TechName'][x].split()
            if len(data['ner'][0]['TechName'][x].split()) == 5:
                patterns.append({'label': 'TechName',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}, {"lower": itlist[4]}]})
            if len(data['ner'][0]['TechName'][x].split()) == 4:
                patterns.append({'label': 'TechName',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]},
                                             {"lower": itlist[3]}]})
            if len(data['ner'][0]['TechName'][x].split()) == 3:
                patterns.append({'label': 'TechName',
                                 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}, {"lower": itlist[2]}]})
            if len(data['ner'][0]['TechName'][x].split()) == 2:
                patterns.append({'label': 'TechName', 'pattern': [{"lower": itlist[0]}, {"lower": itlist[1]}]})
        else:
            patterns.append({"label": "TechName", "pattern": [{"lower": data['ner'][0]['TechName'][x]}]})


    # -------------Terms------------
    for x in range(len(data['ner'][0]['Terms'])):

        if len(data['ner'][0]['Terms'][x].split()) > 1:
            itlist = data['ner'][0]['Terms'][x].split()
            if len(data['ner'][0]['Terms'][x].split()) == 5:
                patterns.append({'label': 'Terms',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}, {"text": itlist[4]}]})
            if len(data['ner'][0]['Terms'][x].split()) == 4:
                patterns.append({'label': 'Terms',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}]})
            if len(data['ner'][0]['Terms'][x].split()) == 3:
                patterns.append({'label': 'Terms',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]}]})
            if len(data['ner'][0]['Terms'][x].split()) == 2:
                patterns.append({'label': 'Terms', 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}]})
        else:
            patterns.append({"label": "Terms", "pattern": [{"text": data['ner'][0]['Terms'][x]}]})


    # -------------Technology------------
    for x in range(len(data['ner'][0]['Technology'])):

        if len(data['ner'][0]['Technology'][x].split()) > 1:
            itlist = data['ner'][0]['Technology'][x].split()
            if len(data['ner'][0]['Technology'][x].split()) == 5:
                patterns.append({'label': 'Technology',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}, {"text": itlist[4]}]})
            if len(data['ner'][0]['Technology'][x].split()) == 4:
                patterns.append({'label': 'Technology',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]},
                                             {"text": itlist[3]}]})
            if len(data['ner'][0]['Technology'][x].split()) == 3:
                patterns.append({'label': 'Technology',
                                 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}, {"text": itlist[2]}]})
            if len(data['ner'][0]['Technology'][x].split()) == 2:
                patterns.append({'label': 'Technology', 'pattern': [{"text": itlist[0]}, {"text": itlist[1]}]})
        else:
            patterns.append({"label": "Technology", "pattern": [{"text": data['ner'][0]['Technology'][x]}]})


    if patterns!=[]:
        print(paper)
        print(patterns)

        new_ruler.add_patterns(patterns)
        doc = nlp(paper)
        print([(ent.text, ent.label_) for ent in doc.ents])

        colors = {"Technology":"#BF11C8","CSO":"#E74C3C","Metrics": "#9B59B6","ProgLang":"#3498DB","Dataset":"#1ABC9C","MathTerm":"#27AE60","IT Framework":"#F1C40F","ISO":"#D35400","TechName":"#95A5A6","Terms":"#5D6D7E"}
        options = {"ents":["Technology","CSO","Metrics","ProgLang","Dataset","MathTerm","IT Framework","ISO","TechName","Terms"], "colors": colors}


        #displacy.serve(doc, style="ent", options=options)
        svg = displacy.render(doc, style="ent", options=options,minify=True)
        output_path = "images/IMG_" + filename.name + ".html"
        # output_path.open("w", encoding="utf-8").write(svg)
        with open(output_path, "w") as outfile:
            outfile.write(svg)

    #break