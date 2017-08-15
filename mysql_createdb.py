import MySQLdb
# Open database connection ( If database is not created don't give dbname)
db = MySQLdb.connect("localhost","root","","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# For creating create db
# Below line  is hide your warning 
cursor.execute("SET sql_notes = 0; ")
# create db here....
cursor.execute("create database IF NOT EXISTS yourdbname")



# create table
cursor.execute("SET sql_notes = 0; ")
cursor.execute("create table IF NOT EXISTS test (email varchar(70),pwd varchar(20));")
cursor.execute("SET sql_notes = 1; ")

#insert data
cursor.execute("insert into test (email,pwd) values('test@gmail.com','test')")

# Commit your changes in the database
db.commit()

# disconnect from server
db.close()
