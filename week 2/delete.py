import psycopg2

def deleteStudent(name):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="ice0989842537",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="mydb")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from students "
        cursor.execute(postgreSQL_select_Query, (name,))
        print("Before Update \n")
        student_records = cursor.fetchall()
        for row in student_records:
            print(row , '\n')

        postgreSQL_select_Query = "delete from students where f_name = %s"
        cursor.execute(postgreSQL_select_Query,(name,))
        connection.commit()

        postgreSQL_select_Query = "select * from students"
        cursor.execute(postgreSQL_select_Query, (name,))
        print("After Delete \n")
        student_records = cursor.fetchall()
        for row in student_records:
            print(row, '\n')

    except (Exception, psycopg2.Error) as error:
        print("-", error)
    finally:
        if(connection):
            cursor.close()
            connection.close()
            print("mydb connection is closed")

deleteStudent('Patsakon')