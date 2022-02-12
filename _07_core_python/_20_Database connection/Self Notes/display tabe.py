import psycopg2
conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="1234",
                            host="localhost",
                            port="5432")

cursor = conn.cursor()
query = "SELECT * FROM STU"
cursor.execute(query)
print("\n-----Retrieving records from db table Test-------")
records = cursor.fetchall()
print("Records from db ", records)
conn.commit()
for i in records:
    print(i)

print("---------retrieve values successfully----------")