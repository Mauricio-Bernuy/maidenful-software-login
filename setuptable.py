import sqlite3

con = sqlite3.connect('login.db', check_same_thread=False)

cur = con.cursor()


def createtable():
    # Create tabl
    cur.execute('''CREATE TABLE users
                (username text, password text)''')
    con.commit()

def registeruser(new_user, new_password):
    # add register
    cur.execute("insert into users values (?, ?)", (new_user, new_password))
    con.commit()

def verifyuser(user_to_verify, password_to_verify):
    # search username
    for result in cur.execute("SELECT * from users WHERE username=:user",{"user":user_to_verify}):
        if result[0] == user_to_verify and result[1] == password_to_verify:
            return True
        else:
            return False
                    
    return False

