import sqlite3

conn=sqlite3.connect('user.db')
def read():
    name = input("Enter name: ")
    cursor=conn.execute(f"SELECT * FROM users where name='{name}'")
    # rows= cursor.fetchone()
    for row in cursor:
        print(row)
    else:
        print("User Not Found")
    
read()