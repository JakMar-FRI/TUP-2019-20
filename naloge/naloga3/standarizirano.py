import mysql.connector
import csv


database =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "naloga3-2"
)
print(database)

cursor = database.cursor(buffered=True)


id = 1
header = True

queryInsert = "INSERT IGNORE INTO koda(id, en_koda, en_opis) VALUES (%s, %s, %s)"
csvFile = csv.reader(open("ang_kode.csv"), delimiter = ";")

stevec = 1

for row in csvFile:
    cursor.execute(queryInsert, [id, row[0], row[1]])
    id += 1
    print(id)


database.commit()


csvFile = csv.reader(open("slo-kode-normalizirane.csv"), delimiter = ";")
header = True

queryInsert = "INSERT INTO koda(id, si_koda, normalizirana_koda, si_opis) VALUES (%s, %s, %s, %s)"
queryUpdate = "UPDATE koda SET si_koda = %s, si_opis = %s, normalizirana_koda = %s WHERE id = %s"

stevec = 0

for row in csvFile:
    if header:
        header = False
        continue
    cursor.execute("SELECT id FROM koda WHERE en_koda = %s", [row[1]] )
    rez = cursor.fetchone()
    if rez is not None:
        cursor.execute(queryUpdate, [row[0], row[2], row[1], int(rez[0])])
    else:
        #print("TUKAJ")
        cursor.execute(queryInsert, [id, row[0], row[1], row[2]])
        id += 1

    stevec += 1
    print(stevec)


database.commit()



csvFile = csv.reader(open("diag_standarizirana.csv"), delimiter = ";")
id = 1
header = True

queryInsert1 = "INSERT INTO diagnoza(koda, obravnava, st_diagnoze, si_koda) VALUES (%s, %s, %s, %s)"
queryInsert2 = "INSERT INTO diagnoza(koda, obravnava, st_diagnoze) VALUES (%s, %s, %s)"

cursor.execute("SELECT id FROM koda WHERE si_koda = 'I11.0'")
rez = cursor.fetchall()
for row in rez:
    print(row)

for row in csvFile:
    if header:
        header = False
        continue
    query = "SELECT id FROM koda WHERE si_koda = '" + row[2] + "'"
    rez = cursor.execute(query)
    rez = cursor.fetchone()
    #print(query + " --> " + str(rez))
    if rez is None:
        cursor.execute(queryInsert2, [row[2], row[0], row[1]])
    else:
        cursor.execute(queryInsert1, [row[2], row[0], row[1], rez[0]])
    print(id)
    id +=1

database.commit()