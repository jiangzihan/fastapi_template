import spacy
import csv
import json

#load spacy
nlp = spacy.load("en_core_web_sm")

#get the root of this phrase, e.g. very good -> good, but 'not good' also gets 'good', need to use score to identify.
#but not quite useful for verb phrases, e.g. had such high hopes -> have
def getRootLemma(text):
    doc=nlp(text)
    root=list(doc.sents)[0].root
    for token in doc:
        if token==root:
            return token.lemma_

#get the opinions, store as set
csvFile = open("/Users/reai01/Downloads/bogooexport1206.csv","r")
reader = csv.DictReader(csvFile)
opinions=[]
for dict in reader:
  opinion = dict['opinions']
  opinions.append(opinion)
setOp=set(opinions)

#iterate and get the roots as keys
result={}
for op in setOp:
    key = getRootLemma(op)
    if key in result:
        result[key].append(op)
    else:
        result[key]=[op]

#this dict has key as group name and value as array of appeared variances.
print(json.dumps(result, indent=1))