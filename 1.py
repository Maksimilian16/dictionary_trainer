import json
import random
with open('en-uk.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
text1 = {v: k for k, v in text.items()}
rand = random.randint(0, len(text)-1)
def asking():
    fq = input("pick mode:\na. translate En-Ua\nb. translate Ua-En\nc. add word\nd. game\n")
    xy = input("print ur word: ")
    if fq == "b":
        translate_EnToUk(xy)
    if fq == "a":
        translate_ukToEn(xy)
    if fq == "c":
        create_word()
    if fq == "d":
        game()


def translate_ukToEn(ask):
    if ask in text:
        print(text[ask])


def translate_EnToUk(ask):
    if ask in text1:
        print(text1[ask])


def create_word():
    e = input("print eng word")
    u = input("print uk word")
    eu = {e: u}
    text.update(eu)
    with open('en-uk.json', 'w') as f:
        json.dump(text, f)


def game():
    xyz = random.choice(list(text.values()))
    xyz1 = text.get(xyz)
    ask_game = input(xyz)
    if ask_game == xyz1:
        print("You won")
    else:
        print("you lost")
asking()