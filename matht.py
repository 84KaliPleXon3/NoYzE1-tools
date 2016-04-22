import random
import sys
import sqlite3
import sys

class score:
    add = 0
    sub = 0
    mul = 0
    div = 0

def get_cursor():
    connection = sqlite3.connect("matht.db")
    cursor = connection.cursor()
    return cursor

def read_score():
    cursor = get_cursor()
    cursor.execute("SELECT score FROM scores")
    score.add = cursor.fetchone()[0]
    score.sub = cursor.fetchone()[0]
    score.mul = cursor.fetchone()[0]
    score.div = cursor.fetchone()[0]

def setup_db():
    connection = sqlite3.connect("matht.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE scores (score_id INTEGER PRIMARY KEY, score_name VARCHAR(255), score INTEGER);")
    cursor.execute("INSERT INTO scores (score_name, score) VALUES ('add', 0);")
    cursor.execute("INSERT INTO scores (score_name, score) VALUES ('sub', 0);")
    cursor.execute("INSERT INTO scores (score_name, score) VALUES ('mul', 0);")
    cursor.execute("INSERT INTO scores (score_name, score) VALUES ('div', 0);")
    connection.commit()
    print("Done.")

def store_score():
    connection = sqlite3.connect("matht.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE scores SET score={0} WHERE score_name='add';".format(score.add))
    cursor.execute("UPDATE scores SET score={0} WHERE score_name='sub';".format(score.sub))
    cursor.execute("UPDATE scores SET score={0} WHERE score_name='mul';".format(score.mul))
    cursor.execute("UPDATE scores SET score={0} WHERE score_name='div';".format(score.div))
    connection.commit()

def print_score():
    cursor = get_cursor()
    cursor.execute("SELECT score_name, score FROM scores")
    result = cursor.fetchall()
    for r in result:
        print(r)
    print("")

def print_menu():
    print("1: +")
    print("2: -")
    print("3: *")
    print("4: /")
    print("5: random\n")

def add():
    a = random.SystemRandom().randint(0, 100)
    b = random.SystemRandom().randint(0, 100)
    print(a, "+", b, "=", end=" ")
    while True:
        answer = input()
        if answer == "exit":
            sys.exit()
        elif float(answer) == a + b:
            print("correct!\n")
            score.add += 1
            store_score()
            print_score()
            break
        else:
            print("false! try again!\n")
            print(a, "+", b, "=", end=" ")

def subtract():
    a = random.SystemRandom().randint(0, 100)
    b = random.SystemRandom().randint(0, 100)
    if b > a:
        c = a
        d = b
        a = d
        b = c
    print(a, "-", b, "=", end=" ")
    while True:
        answer = input()
        if answer == "exit":
            sys.exit()
        elif float(answer) == a - b:
            print("correct!\n")
            score.sub += 1
            store_score()
            print_score()
            break
        else:
            print("false! try again!\n")
            print(a, "-", b, "=", end=" ")


def multiply():
    a = random.SystemRandom().randint(0, 10)
    b = random.SystemRandom().randint(0, 10)
    print(a, "*", b, "=", end=" ")
    while True:
        answer = input()
        if answer == "exit":
            sys.exit()
        elif float(answer) == a * b:
            print("correct!\n")
            score.mul += 1
            store_score()
            print_score()
            break
        else:
            print("false! try again!\n")
            print(a, "*", b, "=", end=" ")


def divide():
    while True:
        a = random.SystemRandom().randint(1, 100)
        b = random.SystemRandom().randint(1, 100)
        if a % b == 0 and not a == b and not a > (b * 10):
            break
    if b > a:
        c = a
        d = b
        a = d
        b = c
    print(a, "/", b, "=", end=" ")
    while True:
        answer = input()
        if answer == "exit":
            sys.exit()
        elif float(answer) == a / b:
            print("correct!\n")
            score.div += 1
            store_score()
            print_score()
            break
        else:
            print("false! try again!\n")
            print(a, "/", b, "=", end=" ")


def main():
    print_score()
    print_menu()

    i = input()
    print("")
    if i == "1":
        while True:
            add()
    elif i == "2":
        while True:
            subtract()
    elif i == "3":
        while True:
            multiply()
    elif i == "4":
        while True:
            divide()
    elif i == "5":
        while True:
            rnd = random.SystemRandom().randint(1, 4)
            if rnd == 1:
                add()
            elif rnd == 2:
                subtract()
            elif rnd == 3:
                multiply()
            elif rnd == 4:
                divide()
    elif i == "exit":
        sys.exit()
    else:
        print("Try again!\n")

if len(sys.argv) > 1:
    if sys.argv[1] == "-i":
        setup_db()
else:
    read_score()
    while True:
        main()
