from threading import Thread
import mysql.connector
import time


def connect():
    return mysql.connector.connect(
                    user = "root",
                    host = "localhost",
                    port = "3306",
                    database = "naloga3"
    )

def posodobi1():
    db = connect()
    cursor = db.cursor()
    query = "UPDATE pacient SET starost = 96 WHERE kzz = 500004"
    cursor.execute(query)
    db.commit()

def posodobi2():
    db = connect()
    cursor = db.cursor()
    query = "UPDATE pacient SET starost = 97 WHERE kzz = 500004"
    cursor.execute(query)
    db.commit()

def beri():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM PACIENT WHERE kzz = 500004")
    rez = cursor.fetchone()
    print(rez)


if __name__ == '__main__':
    Thread(target = posodobi1).start()
    Thread(target = posodobi2).start()
    time.sleep(2)
    Thread(target = beri).start()
    