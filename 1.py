import json
booll = True
with open('en-uk.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
with open('uk-en.json', 'r', encoding='utf-8') as f:
    text1 = json.load(f)
while booll:
    fq = input("pick mode:\na. translate Ukr-Eng\nb. translate Eng-Ukr\nc. add word\n")
    if fq == "a":
        translate_uk = input("print your word: ")
        if translate_uk in text:
            print(text.get(translate_uk))
        else:
            print(text)
    if fq == "b":
        translate_eng = input("print your word: ")
