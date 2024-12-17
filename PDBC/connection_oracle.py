import oracledb
# cn=oracledb.connect("manager/tiger@localhost:1521/XE")
# print("connection established")

connection = oracledb.connect("manager/tiger@localhost:1521/XE")
print("Connection Establish..")
cur = connection.cursor()
query = "insert into Students values(1,'Harshal')"
cur.execute(query)
print("Student Added..!")
connection.close()
