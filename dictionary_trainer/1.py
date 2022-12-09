import json
import random
import sqlite3

sqlite_connection = sqlite3.connect('tr.db')
cursor = sqlite_connection.cursor()
cursor.execute("""SELECT * from language""")
records = cursor.fetchall()
print(records)
with open('en-uk.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
text1 = {v: k for k, v in text.items()}
rand = random.randint(0, len(text)-1)
def asking():
    fq = input("pick mode:\na. translate Ua-En\nb. translate En-Ua\nc. add word\nd. game\n")

    if fq == "a":
        translate_ukToEn()
    if fq == "b":
        translate_EnToUk()
    if fq == "c":
        create_word()
    if fq == "d":
        game()


def translate_ukToEn():
    xy = input("print ur word: ")
    cursor.execute("SELECT eng FROM language WHERE ua = :namee ", {'namee': xy})
    data_2 = cursor.fetchall()
    print(data_2)


def translate_EnToUk():
    xy1 = input("print ur word: ")
    cursor.execute("SELECT ua FROM language WHERE eng = :names ", {'names': xy1})
    data_1 = cursor.fetchall()
    print(data_1)


def create_word():
    e = input("print eng word")
    u = input("print uk word")
    cursor.execute("""INSERT INTO language(ua, eng)
        VALUES(:u, :e)""", {'u': u, 'e': e})
    sqlite_connection.commit()


def game():
    xyz = random.choice(list(text.keys()))
    xyz1 = text.get(xyz)
    ask_game = input(xyz)
    if ask_game == xyz1:
        print("You won")
    else:
        print("you lost")
asking()