import mysql.connector
conn = mysql.connector.connect(host='loclhost', database = 'PythonAutomation', \
                               user='root', password='ssqa')

print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchone()
print(row)
print(row[3])

rows = cursor.fetchall() # a list of tuples

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK", 'Jmeter')
cursor.execute(query, data)
conn.commit()

# delete from customerInfo where couseName = 'SebServices'; 
conn.close()

