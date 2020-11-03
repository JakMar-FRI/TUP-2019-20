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


#SQL query
query = "\
    select \
        p.ime, \
        p.priimek, \
        n.ulica, \
        n.hisna_stevilka, \
        k.kraj, \
        k.posta \
    from \
        pacient p \
    left join naslov n on p.naslovID = n.naslovID \
left join kraj k on n.posta = k.posta"

cursor.execute(query)
for row in cursor:
    print(f"\
            {row[0]}\t\
            {row[1]}\t\
            {row[2]}\t\
            {row[3]}\t\
            {row[4]}\t\
            {row[5]}"
        )


rez = mongoDB.naslov.aggregate([{
    "$lookup": {
        "from": "pacient",
        "localField": "naslovID",
        "foreignField": "naslovID",
        "as": "pacient"
    }
    }, {
        "$unwind": {
            "path": "$pacient"
        }
    }, {
        "$lookup": {
            "from": "kraj",
            "localField": "posta",
            "foreignField": "posta",
            "as": "kraj"
        }
    }, {
        "$unwind": {
            "path": "$kraj"
        }
    }
])

for doc in rez:
    print(f"\
            {doc['pacient']['ime']}\t\
            {doc['pacient']['priimek']}\t\
            {doc['ulica']}\t\
            {doc['hisna_stevilka']}\t\
            {doc['kraj']['posta']}\t\
            {doc['kraj']['kraj']}"
        )