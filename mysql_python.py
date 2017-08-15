#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root123", db="pets")

#create a cursor for the select
cur = db.cursor()

#execute an sql query
cur.execute("SELECT name FROM pets.cats")

##Iterate 
for row in cur.fetchall() :
      #data from rows
        name = str(row[0])

        print("This Person's name is " + name )

# close the cursor
cur.close()

# close the connection
db.close ()
