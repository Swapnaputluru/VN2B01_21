import psycopg2
conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="1234",
                            host="localhost",
                            port="5432")

cursor = conn.cursor()
value1 = "insert into stu values ('swapna', '124','tapatri')"
value2 = "insert into stu values ('sony', '12','anantapur')"
value3 = "insert into stu values ('sunny', '14','tirupathi')"

cursor.execute(value1)
cursor.execute(value2)
cursor.execute(value3)
conn.commit()

print("---------insert values successfully----------")
print(value1)