import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



# Подключение к базе данных
def connect_cursor():
    global connectection, cursor
    try:

        connection = psycopg2.connect(user="postgres",

                                    password="qwerty",
                                    host="localhost",
                                    port="5433")
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")


    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
 #   finally:
  #      if connection:
  #          cursor.close()
  #          connection.close()
  #          print("Соединение с PostgreSQL закрыто")


    #test insert
def test_insert(cursor):
    cursor.execute(
        """INSERT INTO users (login, password) VALUES
        ('test_login2', 'test_password2');"""
    )
    print("[INFO] Data was succefully inserted")



def test_get(cursor):
    cursor.execute(
        """SELECT password FROM users WHERE login = 'test_login2';"""
    )
    print(cursor.fetchone())









connect_cursor()
#test_insert(cursor)
test_get(cursor)









#create table

 #   cursor.execute(
  #      """CREATE TABLE users(
   #         id serial PRIMARY KEY,
   #         login varchar(50) NOT NULL,
  #          password varchar(50) NOT NULL);"""
  #  )
 #   connection.commit()
    #   print("[INFO] Table created successfully")









    #test insert
 #   cursor.execute(
  #      """INSERT INTO users (login, password) VALUES
   #     ('test_login', 'test_password');"""
   # )
   # print("[INFO] Data was succefully inserted")


#test get reauest

#    cursor.execute(
#        """SELECT password FROM users WHERE login = 'test_login';"""
 #   )
 #   print(cursor.fetchone())










