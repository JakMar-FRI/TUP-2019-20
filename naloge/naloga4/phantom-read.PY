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

def posodobi():
    db = connect()
    cursor = db.cursor()
    time.sleep(2)
    query = "UPDATE pacient SET starost = 26 WHERE kzz = 500004"
    cursor.execute(query)
    db.commit()

def beri():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pacient WHERE starost BETWEEN 10 AND 30")
    rez = cursor.fetchall()
    print(rez)
    time.sleep(3)
    cursor.execute("SELECT * FROM pacient WHERE starost BETWEEN 10 AND 30")
    rez = cursor.fetchall()
    print(rez)


if __name__ == '__main__':
    Thread(target = beri).start()
    Thread(target = posodobi).start()
    