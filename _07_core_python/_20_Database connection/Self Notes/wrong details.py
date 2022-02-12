import psycopg2

try:
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="12345",  # given password is wrong
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()

except Exception as error:
    print(error)

finally:
    cursor.close()
    conn.close()