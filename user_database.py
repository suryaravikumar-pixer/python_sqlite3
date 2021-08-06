import sqlite3

try:
        
    conn = sqlite3.connect('user.db')
    cursor = conn.cursor()
    print("Data base created")

    sql = "select sqlite_version() "
    cursor.execute(sql)

    results = cursor.fetchall()
    print("Version: ", results)
    cursor.close()
except sqlite3.Error as e:
    print("Connection Error", e)

finally:
    if (conn):
        conn.close()
        print("Connectin Closed")