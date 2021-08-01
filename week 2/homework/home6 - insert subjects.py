import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                password="ice0989842537",
                                host="127.0.0.1",
                                port="5432",
                                database="mydb")

    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO Subjects ( subject_id, subject_name, credit, teacher_id) VALUES (%s,%s,%s,%s)"""
    record_to_insert = [
                        ('060233112','DATA ENGINEERING','3','STS'),
                        ('060233113','ADVANCED COMPUTER PROGRAMMIN','3','AMK'),
                        ('040203111','ENGINEERING MATHEMATICS I','3','DPR')
                        ]

    cursor.executemany(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count,"Record inserted successfully in to students table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into students table", error)
finally:
    if(connection):
        cursor.close()
        connection.close()
        print("mydb connection is closed")