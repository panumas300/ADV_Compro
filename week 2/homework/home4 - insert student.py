import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                password="ice0989842537",
                                host="127.0.0.1",
                                port="5432",
                                database="mydb")

    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO Students ( student_id, f_name, l_name, e_mail) VALUES (%s,%s,%s,%s)"""
    record_to_insert = [
                        ('6306022610024','Panumas','Sangthong','6306022610024@fitm.kmutnb.ac.th'),
                        ('6306022630017','Chisanuphong','Nuntta','6306022630017@fitm.kmutnb.ac.th'),
                        ('6306022610016','Patsakon','Tanee','630622610016@fitm.kmutnb.ac.th')
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