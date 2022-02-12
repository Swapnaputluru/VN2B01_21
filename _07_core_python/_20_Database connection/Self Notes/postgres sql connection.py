import psycopg2
conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="1234",
                            host="localhost",
                            port="5432")

cursor = conn.cursor()
quary1 = "create table login(mailid varchar(20),moible_no varchar(10), password varchar(10))"
cursor.execute(quary1)

records = [("swapna@gmail.com", '8765432122', 'abcd'),
           ("hanu@gmail.com", '264213521', 'efgh'),
           ("divi@gmail.com", '786526542', 'ihjkl'),
           ("manu@gmail.com", '647251245', 'mnop')]
for record in records:
    query2 = "INSERT INTO login VALUES(%s, %s, %s)"
    cursor.execute(query2, record)

conn.commit()
