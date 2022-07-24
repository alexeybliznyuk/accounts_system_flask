import db #current test_db.py





db.connect_cursor()
#test_insert(cursor)
db.test_get(db.cursor)

db.close_connect(db.cursor, db.connection)



