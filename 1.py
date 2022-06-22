import json
import random
booll = True
with open('en-uk.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
with open('uk-en.json', 'r', encoding='utf-8') as f:
    text1 = json.load(f)
while booll:
    fq = input("pick mode:\na. translate Eng-Ukr\nb. translate Ukr-Eng\nc. add word\nd. game\n")
    if fq == "a":
        translate_uk = input("print your word: ")
        if translate_uk in text:
            print(text.get(translate_uk))
        else:
            print(text)
    if fq == "b":
        translate_eng = input("print your word: ")
        if translate_eng in text1:
            print(text1.get(translate_eng))
    if fq == "c":
        e = input("print eng word")
        u = input("print uk word")
        eu = {e: u}
        text.update(eu)
        with open('en-uk.json', 'w') as f:
            json.dump(text, f)
        ue = {u: e}
        text1.update(ue)
        with open('uk-en.json', 'w') as f:
            json.dump(text1, f)
    if fq == "d":
        hq = random.choice(list(text.values()))
        print("print translate of word:")
        gq = input(hq)
        if text.get(gq) == hq:
            print("You won")
        else:
            print("you lost")
