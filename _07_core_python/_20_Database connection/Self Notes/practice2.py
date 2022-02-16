import psycopg2
import psycopg2.extras
conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                         password="1234",
                        port="5432")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute("drop table if exists employee_details")
create_table = "create table if not exists employee_details(e_name varchar(30), e_id varchar(10), e_salary varchar(30))"
cur.execute(create_table)
insert_way = "insert into employee_details(e_name, e_id, e_salary) values(%s, %s, %s)"
insert_values =[("Sunny", "1", "10000"), ("Sony", "2", "12000"), ("Syam", "3", "13000"), ("Ram", "4", "14000")]
for i in insert_values:
    cur.execute(insert_way, i)
# cur.execute( '''update employee_details SET e_salary = 20000 where e_id = 3''')
cur.execute("select * from employee_details")
for i in cur.fetchall():
    print(i)
    print(i["e_name"], i ["e_salary"])
conn.commit()

print("=========================By using with=================================")

with psycopg2.connect(database="postgres",
                        host="localhost",
                        user="postgres",
                         password="1234",
                        port="5432") as connection:
  with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    cur.execute("drop table if exists employee_detail")
    create_table = "create table if not exists employee_detail(e_name varchar(30), e_id varchar(10), e_salary varchar(30))"
    cur.execute(create_table)
    insert_way = "insert into employee_detail(e_name, e_id, e_salary) values(%s, %s, %s)"
    insert_values =[("Sunny", "1", "10000"), ("Sony", "2", "12000"), ("Syam", "3", "13000"), ("Ram", "4", "14000")]
    for i in insert_values:
        cur.execute(insert_way, i)
    # cur.execute( '''update employee_details SET e_salary = 20000 where e_id = 3''')
    cur.execute("select * from employee_detail")
    for i in cur.fetchall():
        print(i)
        print(i["e_name"], i ["e_salary"])
    conn.commit()