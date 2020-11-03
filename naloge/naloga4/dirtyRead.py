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

def vstavi():
    db = connect()
    cursor = db.cursor()
    x = 99999
    for i in range(1):
        query = "INSERT INTO ODDELEK(sifra_oddelka) VALUES (%s)"
        cursor.execute(query, [x])
        x += 1
        time.sleep(10)
        db.rollback()

def beri():
    db = connect()
    cursor = db.cursor()
    time.sleep(0.25)
    cursor.execute("SELECT * FROM ODDELEK")
    rez = cursor.fetchall()
    for row in rez:
        print(row[0])


db = connect()
cursor = db.cursor()
cursor.execute("SET GLOBAL TRANSACTION ISOLATION LEVEL READ UNCOMMITTED")
Thread(target = vstavi).start()
Thread(target = beri).start()
time.sleep(10)
Thread(target = beri).start()