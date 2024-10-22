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


##          dirty read      ##

def vstavi():
    db = connect()
    cursor = db.cursor()
    #cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED")
    x = 99999999
    for i in range(1):
        query = "INSERT INTO ODDELEK(sifra_oddelka) VALUES (%s)"
        cursor.execute(query, [x])
        x += 1
        time.sleep(10)
        db.rollback()

def beriOddelek():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE")
    time.sleep(0.25)
    cursor.execute("SELECT * FROM ODDELEK")
    rez = cursor.fetchall()
    for row in rez:
        print(row[0])


##          izgubljeno ažuriranje       ##

def posodobi1():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL SERIZABLE")
    query = "UPDATE pacient SET starost = 96 WHERE kzz = 500004"
    cursor.execute(query)
    db.commit()

def posodobi2():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL SERIZABLE")
    query = "UPDATE pacient SET starost = 97 WHERE kzz = 500004"
    cursor.execute(query)
    db.commit()

def beriAzuiranje():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM PACIENT WHERE kzz = 500004")
    rez = cursor.fetchone()
    print(rez)


##          non-repeatable read     ##

def posodobiNonRepeatable():
    db = connect()
    cursor = db.cursor()
    time.sleep(2)
    query = "UPDATE pacient SET starost = 28889 WHERE kzz = 500004"
    cursor.execute(query)
    db.commit()

def berinonRepeatable():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
    cursor.execute("SELECT * FROM PACIENT WHERE kzz = 500004")
    rez = cursor.fetchone()
    print(rez)
    time.sleep(3)
    cursor.execute("SELECT * FROM PACIENT WHERE kzz = 500004")
    rez = cursor.fetchone()
    print(rez)


##          phantom read        ##

def vstaviPhantom():
    db = connect()
    cursor = db.cursor()
    time.sleep(2)
    query = "INSERT INTO pacient(kzz, starost, spol) VALUES (999998, 30, 'M')"
    cursor.execute(query)
    db.commit()

def beriPhanton():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ")
    cursor.execute("SELECT * FROM pacient WHERE starost BETWEEN 10 AND 30 ORDER BY starost, kzz")
    rez = cursor.fetchall()
    for row in rez:
        print(row)
    time.sleep(3)
    cursor.execute("SELECT * FROM pacient WHERE starost BETWEEN 10 AND 30 ORDER BY starost, kzz")
    rez = cursor.fetchall()
    for row in rez:
        print(row)


def dirtyRead():
    db = connect()
    cursor = db.cursor()
    Thread(target = vstavi).start()
    Thread(target = beriOddelek).start()
    time.sleep(10)
    Thread(target = beriOddelek).start()


def azuriranje():
    Thread(target = posodobi1).start()
    Thread(target = posodobi2).start()
    time.sleep(2)
    Thread(target = beriAzuiranje).start()


def nonRepeatable():
    Thread(target = berinonRepeatable).start()
    Thread(target = posodobiNonRepeatable).start()


def phantonRead():
    Thread(target = beriPhanton).start()
    Thread(target = vstaviPhantom).start()