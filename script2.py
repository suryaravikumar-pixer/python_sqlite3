import sqlite3

conn=sqlite3.connect('user.db')
def read():
    cursor=conn.execute("SELECT * FROM users")
    rows= cursor.fetchall()
    name = input("Enter name: ")
    for row in rows:
        if name == row[1]:
            print(row)
        else:
            print("User Not Found")
    
read()