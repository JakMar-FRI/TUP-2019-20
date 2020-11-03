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
csvFile = csvInput('pacient.csv')
stevec = 1
header = True
query = 'INSERT INTO Pacient(KZZ, starost, spol) VALUES (%s, %s, %s)'
print('Vstavljanje pacientov:')
for row in csvFile:
    if header:
        header = False
        continue
    kzz = int(row[0])
    starost = int(row[1])
    spol = row[2]
    insert(query, [kzz, starost, spol], cursor)
    stevec += 1
    print(stevec)

database.commit()