import spacy
import sys

nlp = spacy.load("en_core_web_sm")
doc = nlp(sys.argv[1])
propns = []
digits = []
for token in doc:
    if token.pos_ ==  "PROPN":
        propns.append(token.text)
        
    if token.pos_ == "NUM":
        if len(token.text) > 1:
            for string in token.text:
                if string.isdigit():
                    digits.append(string)
        else:
            digits.append(token.text)
print(""" <table>
   <caption>Find tokens:</caption>""")
print("""  <tr>
    <th>Token name:</th>
    <th>Count:</th>
   </tr>
""")
for propn in propns:
    print(f"<tr><td>{propn}</td><td>{propns.count(propn)}</td></tr>")

for digit in digits:
    print(f"<tr><td>{digit}</td><td>{digits.count(digit)}</td></tr>")

print("</table>")
