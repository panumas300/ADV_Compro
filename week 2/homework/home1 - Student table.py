import psycopg2
from psycopg2 import Error
try:
    connection = psycopg2.connect(user="postgres",
                                password="ice0989842537",
                                host="127.0.0.1",
                                port="5432",
                                database="mydb")

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE Students
        (Student_id     CHAR(13)    PRIMARY KEY,
        f_name          VARCHAR(30) NOT NULL,
        l_name          VARCHAR(30) NOT NULL,
        e_mail          VARCHAR(50) ); '''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table create successfully in PostgreSQL ")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")