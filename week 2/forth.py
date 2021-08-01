import psycopg2

def updateEmail(name, new_email) :
    try :
        connection = psycopg2.connect(user="postgres",
                                    password="ice0989842537",
                                    host='127.0.0.1',
                                    port='5432',
                                    database='mydb')

        cursor = connection.cursor()
        postgresSQL_select_Query = "select * from students where f_name = %s"
        cursor.execute(postgresSQL_select_Query, (name,))
        print("Before Update")
        student_records = cursor.fetchall()
        for row in student_records :
            print(row,'\n')

        postgresSQL_select_Query = "update students set e_mail = %s where f_name = %s"
        cursor.execute(postgresSQL_select_Query, (new_email, name))
        connection.commit()

        postgresSQL_select_Query = "select * from students where f_name = %s"
        cursor.execute(postgresSQL_select_Query, (name,))
        print("After Update")
        student_records = cursor.fetchall()
        for row in student_records :
            print(row, '\n')
    except (Exception, psycopg2.Error) as error :
        print("Error while fetching data from PostgreSQL", error)

    finally :
        if(connection) :
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

updateEmail('Panumas', 'panumas3000@outlook.com')