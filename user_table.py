import sqlite3

try:
        
    conn = sqlite3.connect('user.db')
    #sql will be defined here
    sql = """
            CREATE TABLE users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone_no INTEGER NOT NULL,
                age INTEGER NOT NULL,
                dob TEXT NOT NULL

              );
          """
    
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("Table created")


    cursor.close()
except sqlite3.Error as e:
    print("Connection Error", e)

finally:
    if (conn):
        conn.close()
        print("Connectin Closed")