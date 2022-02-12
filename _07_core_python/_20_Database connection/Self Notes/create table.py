import psycopg2
conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="1234",
                            host="localhost",
                            port="5432")

cursor = conn.cursor()
query = "CREATE TABLE stu(student_name varchar(50),student_id varchar(20),address varchar(100))"
cursor.execute(query)
conn.commit()

print("---------Table student_details created successfully----------")