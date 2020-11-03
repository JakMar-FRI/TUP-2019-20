import mysql.connector
import csv


database =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "naloga3"
)

print(database)

cursor = database.cursor(buffered=True)

#csvFile = csv.reader(open("ang_kode.csv"), delimiter = ";")
#stevec = 1
#header = True
#query = "INSERT INTO koda_diagnoza(id_kode, who_koda, en_opis) VALUES (%s, %s, %s)"
#print("Vstavljanje angleških kod")
#
#for row in csvFile:
#    #print(row)
#    en_opis = row[1]
#    who_koda = row[0]
#    cursor.execute(query, [stevec, who_koda, en_opis])
#    print(stevec)
#    stevec += 1
#database.commit()

csvFile = csv.reader(open("kodeBolezni.csv"), delimiter = ";")
x = 1
header = True
queryInsert = "INSERT IGNORE INTO koda_diagnoza(id_kode, si_opis, mkb_koda) VALUES (%s, %s, %s)"
queryUpdate = "UPDATE koda_diagnoza SET si_opis = %s, mkb_koda = %s WHERE id_kode = %s"
print("Vstavljanje kod")

#for row in csvFile:
#    if header:
#        header = False
#        continue
#    si_opis = row[1]
#    mkb_koda = row[0]
#    testnaKoda = mkb_koda.replace('.', '')
#    testnaKoda = "%" + testnaKoda + "%"
#    cursor.execute("SELECT id_kode from koda_diagnoza WHERE who_koda LIKE %s", [testnaKoda])
#    rezultat = cursor.fetchone()
#    if rezultat is not None:
#        id_kode = rezultat[0]
#        cursor.execute(queryUpdate, [si_opis, mkb_koda, id_kode])
#        print(str(x) + " posodabljam")
#    else:
#        cursor.execute(queryInsert, [stevec, si_opis, mkb_koda])
#        print(x)
#        stevec += 1
#    x += 1

for row in csvFile:
    if header:
        header = False
        continue
    si_opis = row[1]
    mkb_koda = row[0]
    cursor.execute(queryInsert, [x, si_opis, mkb_koda])
    print(x)
    x += 1

database.commit()
print("Končano")