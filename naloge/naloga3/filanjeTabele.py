import mysql.connector
import csv
from datetime import datetime

def toFloat(x):
    try:
        y = float(x)
    except ValueError:
        y = None
    return y

def toDate(x):
    date = datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    date.strftime("%Y-%m-%d %H:%M:%S")
    return date

def csvInput(x):
    return csv.reader(open(x), delimiter = ";")

def insert(query, input, cursor):
    cursor.execute(query, input)


database = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    database = "naloga3"
)

print(database)
cursor = database.cursor()

#pacient
#csvFile = csvInput('pacient.csv')
#stevec = 1
#header = True
#query = 'INSERT IGNORE INTO Pacient(KZZ, starost, spol) VALUES (%s, %s, %s)'
#print('Vstavljanje pacientov:')
#for row in csvFile:
#    if header:
#        header = False
#        continue
#    kzz = int(row[0])
#    starost = int(row[1])
#    spol = row[2]
#    insert(query, [kzz, starost, spol], cursor)
#    stevec += 1
#    print(stevec)
#database.commit()


#preiskava
#csvFile = csvInput('preiskava.csv')
#stevec = 1
#header = True
#query = 'INSERT IGNORE INTO preiskava(ime_preiskave, sifra_preiskave, enota, '\
#        'min_rez, max_rez, min_m, max_m, min_z, max_z) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
#print('Vstavljanje preiskav:')
#for row in csvFile:
#    if header:
#        header = False
#        continue
#    ime_preiskave = row[0]
#    sifra_preiskave = row[1]
#    min_rez = toFloat(row[2].replace(",", "."))
#    max_rez = toFloat(row[3].replace(",", "."))
#    min_m = toFloat(row[4].replace(",", "."))
#    max_m = toFloat(row[5].replace(",", "."))
#    min_z = toFloat(row[6].replace(",", "."))
#    max_z = toFloat(row[7].replace(",", "."))
#    enota = row[8]
#    insert(query, [ime_preiskave, sifra_preiskave, enota, min_rez, max_rez, min_m, max_m, min_z, max_z], cursor)
#    stevec += 1
#    print(stevec)
#database.commit()


#oddelek
#csvFile = csvInput('oddelek.csv')
#stevec = 1
#header = True
#query = 'INSERT IGNORE INTO oddelek(sifra_oddelka) VALUES (%s)'
#print('Vstavljanje oddelkov:')
#for row in csvFile:
#    if header:
#        header = False
#        continue
#    sifra_oddelka = row[0]
#    insert(query, [sifra_oddelka], cursor)
#    stevec += 1
#    print(stevec)
#database.commit()


#obravnava
csvFile = csvInput('obravnava.csv')
stevec = 1
header = True
query = 'INSERT IGNORE INTO obravnava(st_obravnave, kzz, sifra_oddelka) '\
        ' VALUES (%s, %s, %s)'
print('Vstavljanje obravnav:')
for row in csvFile:
    if header:
        header = False
        continue
    kzz = int(row[0])
    st_obravnave = int(row[1])
    oddelek = int(row[2])
    insert(query, [st_obravnave, kzz, oddelek], cursor)
    stevec += 1
    print(stevec)
database.commit()


#izvid
#csvFile = csvInput('izvid.csv')
#stevec = 1
#header = True
#query = 'INSERT IGNORE INTO izvid(st_obravnave, ime_preiskave, datum_ura, vrednost) '\
#        ' VALUES (%s, %s, %s, %s)'
#print('Vstavljanje izvidov:')
#for row in csvFile:
#    if header:
#        header = False
#        continue
#    st_obravnave = int(row[0])
#    datum_ura = toDate(row[1])
#    ime_preiskave = row[2]
#    vrednost = toFloat(row[3].replace(',', '.'))
#    insert(query, [st_obravnave, ime_preiskave, datum_ura, vrednost], cursor)
#    stevec += 1
#    print(stevec)
#database.commit()