#pip install spacy
from spacy.lang.en import English
#python -m spacy download en_core_web_sm
import en_core_web_sm

with open(r'C:\Users\Saad Malik\Documents\cT blog\wiki.txt') as f:
    lines1 = f.read()
    print(lines1)


nlp = English()

analysis = nlp(lines1)
print(analysis)

token_list = []
for token in analysis:
    token_list.append(token.text)
print(token_list)



#####Entity Detection#####


nlp2 = en_core_web_sm.load()
doc = nlp2(lines1)

for ent in doc.ents:
    if ent.label_ == 'GPE':
        print(ent.text, ent.label_)
