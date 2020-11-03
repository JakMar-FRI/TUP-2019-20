import mysql.connector
import csv


database =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "naloga3-2"
)

print(database)

f = open("tabela.txt", "w")

cursor = database.cursor(buffered=True)

query = "select koda, count(koda) from diagnoza inner join koda k on diagnoza.si_koda = k.id where k.en_koda is null group by koda order by count(koda) desc limit 20;"
cursor.execute(query)
rez = cursor.fetchall()

for row in rez:
    f.write(str(row[0]) + " & " + str(row[1]) + "\\\\\n")

f.close()
