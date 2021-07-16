import sqlite3

while True:
    conn = sqlite3.connect('user.db')
    
    try:
        exit = input("Enter 'quit' to break or hit Enter: ")
        if exit == 'quit':
            print("You're teminated")
            break
        name = input("Name: ")
        email = input("Email: ")
        phone_no = int(input("Phone no: "))
        age = input("Age: ")
        dob = input("Dob: ")

        sql = """INSERT INTO users
                (name, email, phone_no, age, dob)
                VALUES ('{}','{}','{}','{}','{}');""".format(name, email, phone_no, age, dob)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Data is Inserted into users table...")
        cursor.close()
    except sqlite3.Error as e:
        print("Error while Inserting data", e)

    finally:
        if (conn):
            conn.close()
            print("Connectin Closed")