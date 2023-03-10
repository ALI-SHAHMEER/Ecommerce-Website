import sqlite3


#creating  a database
connection = sqlite3.connect('signup.db')

cursor = connection.cursor()
# Create a table in data base

# sql_create_table = "CREATE TABLE person(username TEXT,password TEXT))"


cursor.execute("CREATE TABLE person(username TEXT,email TEXT,password TEXT)")

connection.commit()
cursor.close()