import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.pyplot import figure

def narediGraf(rez, title):
    bolezni = []
    pojavitve = []
    for row in rez:
        bolezni.append(row[0])
        pojavitve.append(row[1])
    y_pos = bolezni
    plt.bar(y_pos, pojavitve, align = "center", alpha = 0.5)
    plt.xticks(y_pos, bolezni, rotation = "270")
    plt.ylabel("Pojavitve")
    plt.title(title)
    plt.subplots_adjust(bottom=0.4, top=0.8)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
    return

def poOddelkih(cursor, database):
    oddelki = "select * from oddelek"
    cursor.execute(oddelki)
    oddelki = cursor.fetchall()

    query = "select kd.si_opis, count(d.ICD_diagnoza) as 'Stevilo pojavitev' from koda_diagnoza kd inner join diagnoza d on d.ICD_diagnoza = kd.mkb_koda inner join obravnava o on d.st_obravnave = o.st_obravnave and o.sifra_oddelka = %s group by d.ICD_diagnoza order by count(d.ICD_diagnoza) DESC limit 10;"

    for row in oddelki:
        oddelek = row[0]
        cursor.execute(query, [oddelek])
        rez = cursor.fetchall()
        narediGraf(rez, "Najpogostejše diagnoze v " + str(oddelek))
    return
        

def poSpolu(cursor, database):
    query =  "select kd.si_opis, count(d.ICD_diagnoza) as 'Stevilo pojavitev' from koda_diagnoza kd inner join diagnoza d on d.ICD_diagnoza = kd.mkb_koda inner join obravnava o on d.st_obravnave = o.st_obravnave inner join pacient p on o.kzz = p.kzz and p.spol = %s group by d.ICD_diagnoza order by count(d.ICD_diagnoza) DESC limit 10;"
    cursor.execute(query, ["m"])
    rez = cursor.fetchall()
    narediGraf(rez, "Najpogostejše diagnoze pri moških")
    cursor.execute(query, ["z"])
    rez = cursor.fetchall()
    narediGraf(rez, "Najpogostejše diagnoze pri ženskah")
    return

database =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "naloga3"
)

print(database)

cursor = database.cursor(buffered=True)

poSpolu(cursor, database)

