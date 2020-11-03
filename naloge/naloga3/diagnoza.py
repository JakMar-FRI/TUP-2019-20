import mysql.connector
import csv


database =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "naloga3"
)

print(database)

cursor = database.cursor(buffered=True)

csvFile = csv.reader(open("diagnoza.csv"), delimiter = ";")
stevec = 1
header = True
query = "INSERT INTO diagnoza(st_obravnave, st_diagnoze, ICD_diagnoza) VALUES (%s, %s, %s)"

header = True

for row in csvFile:
    if header:
        header = False
        continue
    obravnava = int(row[0])
    st_diagnoze = int(row[1])
    diagnoza = row[2]
    cursor.execute(query, [obravnava, st_diagnoze, diagnoza])
    print(obravnava)
    stevec += 1

database.commit()
print("Končano")