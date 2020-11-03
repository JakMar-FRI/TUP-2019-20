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
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE")
    time.sleep(2)
    query = "UPDATE pacient SET starost = 47 WHERE kzz = 500004"
    cursor.execute(query)
    db.commit()

def beri():
    db = connect()
    cursor = db.cursor()
    #cursor.execute("SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED")
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE")
    cursor.execute("SELECT * FROM PACIENT WHERE kzz = 500004")
    rez = cursor.fetchone()
    print(rez)
    time.sleep(3)
    cursor.execute("SELECT * FROM PACIENT WHERE kzz = 500004")
    rez = cursor.fetchone()
    print(rez)
    db.close()


if __name__ == '__main__':
    Thread(target = beri).start()
    time.sleep(3)
    Thread(target = posodobi).start()
    time.sleep(6)
    Thread(target = beri).start()
    