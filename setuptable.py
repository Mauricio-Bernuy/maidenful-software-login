import sqlite3
import time
import os
from threading import Lock
lock= Lock()

con = sqlite3.connect('login.db', check_same_thread=False)
cur = con.cursor()

def createtable():
    lock.acquire(True)
    # Create tabl
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS users( 
            username text NOT NULL,
            password text
        )
        '''
    )
    cur.execute(
        '''
        CREATE UNIQUE INDEX IF NOT EXISTS idx_users_username
        ON users(username)
        '''
    )
    con.commit()
    lock.release()

def droptable():
    lock.acquire(True)
    cur.execute(
        '''
        DROP TABLE IF EXISTS users
        '''
    )
    cur.execute(
        '''
        DROP INDEX IF EXISTS idx_users_username
        '''
    )
    con.commit()
    lock.release()
    

def registeruser(new_user, new_password):
    lock.acquire(True)
    # add register
    cur.execute("insert into users values (?, ?)", (new_user, new_password))
    con.commit()
    lock.release()

def verifyuser(user_to_verify, password_to_verify):
    lock.acquire(True)
    # search username
    for result in cur.execute("SELECT * from users WHERE username=:user",{"user":user_to_verify}):
        if result[0] == user_to_verify and result[1] == password_to_verify:
            lock.release()
            return True
        else:
            lock.release()
            return False
    lock.release()
    return False
