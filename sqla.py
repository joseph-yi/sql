import sqlite3

#create the connection
conn = sqlite3.connect("new.db")

#cursor object... similar to paramiko!
cursor = conn.cursor()

create_statement = """CREATE TABLE population
(city TEXT, state TEXT, population INT) """

cursor.execute(create_statement)
conn.close()
