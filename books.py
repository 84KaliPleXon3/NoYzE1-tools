import sqlite3

connection = sqlite3.connect("books.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY, book_name VARCHAR(255), page VARCHAR(255));
""")

def show_tables():
    cursor.execute("SELECT * FROM books;")
    result = cursor.fetchall()
    print("")
    for r in result:
        print(r)
    print("")

def main():
    run = True
    while run:
        print("")
        print("Menu:")
        print("1: New Book")
        print("2: Update Book")
        print("3: Exit")
        print("")
        i = input()
        if i == "1":
            i = input("Book Name: ")
            cursor.execute("INSERT INTO books (book_name) VALUES ('{0}');".format(i))
            show_tables()
        elif i == "2":
            show_tables()
            i = input("Book ID: ")
            i2 = input("Page: ")
            cursor.execute("UPDATE books SET page='{1}' WHERE book_id={0};".format(int(i), i2))
            show_tables()
        elif i == "3":
            run = False
        elif i == "Debug":
            pass

        connection.commit()

show_tables()
main()
