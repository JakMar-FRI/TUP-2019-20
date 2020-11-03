import mysql.connector
from pymongo import MongoClient
import sys


#povaezava na MongoDB bazo
mongoClient  = MongoClient()
mongoDB = mongoClient.tup_naloga5

#povezava na MySQL bazo
cnx = mysql.connector.connect(
    user = 'root',
    database = 'naloga5'
)
cursor = cnx.cursor()


mongoDB.kraj.drop()
mongoDB.naslov.drop()
mongoDB.pacient.drop()


collection = mongoDB.kraj
query = "SELECT * FROM kraj"
cursor.execute(query)
cus = dict()

id = 1
for row in cursor:
    cus['_id'] = id
    cus['posta'] = row[0]
    cus['kraj'] = row[1]
    print(collection.insert_one(cus).inserted_id)
    id += 1


collection = mongoDB.naslov
query = "SELECT * FROM naslov"
cursor.execute(query)
cus = dict()

for row in cursor:
    cus['posta'] = row[0]
    cus['ulica'] = row[1]
    cus['hisna_stevilka'] = row[2]
    cus['_id'] = row[3]
    cus['naslovID'] = row[3]
    print(collection.insert_one(cus).inserted_id)


collection = mongoDB.pacient
query = "SELECT * FROM pacient"
cursor.execute(query)
cus = dict()

id = 1
for row in cursor:
    print(row)
    cus ['_id'] = id
    cus['kzz'] = row[0]
    cus['naslovID'] = row[1]
    cus['ime'] = row[2]
    cus['priimek'] = row[3]
    cus['rojstni_datum'] = row[4]
    cus['spol'] = row[5]
    print(collection.insert_one(cus).inserted_id)
    id += 1