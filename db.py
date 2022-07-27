import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import requests
import json


login_col = 'login'
password_col = 'password'
table_name = 'users'
#login_request = 'test_login2'
#password_request = 'test_password3'
#id_request = "1"



# Подключение к базе данных
def connect_cursor():
    global connection, cursor
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





def close_connect(cursor, connection):

    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")







    #test insert
def test_insert(cursor):
    cursor.execute(
        f"""INSERT INTO users ({login_col}, {password_col}) VALUES
        ('{login_request}', '{password_request}');"""
    )
    print("[INFO] Data was succefully inserted")



#def test_get(cursor):
 #   cursor.execute(
#        """SELECT password FROM users WHERE login = 'test_login2';"""
#    )
 #   print(cursor.fetchone())


def test_get(cursor, login_request):
 #   global password_col, table_name, login_col, login_reqest
    cursor.execute(
        f"""SELECT {password_col} FROM {table_name} WHERE {login_col} = '{login_request}';"""
    )
 #   answer = {'login': login_request, 'password':cursor.fetchone()[0]}

 #   return answer
    cursor_fetch = cursor.fetchone()
    if cursor_fetch == None:

        answer = {'login': login_request, 'password': cursor_fetch}
        return answer




    else:
        cursor.execute(
            f"""SELECT id FROM {table_name} WHERE {login_col} = '{login_request}';"""
        )
        account_id = cursor.fetchone()
        answer = {'login': login_request, 'password': cursor_fetch[0], 'id': account_id[0]}
        return answer

#    else:
 #       answer = {'login': login_request, 'password': cursor.fetchone()}
 #       return answer






def check_presence(cursor, login):
 #   global password_col, table_name, login_col, login_reqest
    cursor.execute(
        f"""SELECT id FROM {table_name} WHERE {login_col} = '{login}';"""
    )
    account_id = cursor.fetchone()
 #   print(account_id)
    if account_id == None:
        return "This login is free"
    else:
        return "This login already used"


def reg(cursor, login, password):
    presence = check_presence(cursor, login)
    if presence == "This login is free":
        cursor.execute(
            f"""INSERT INTO users ({login_col}, {password_col}) VALUES
            ('{login}', '{password}');"""
        )
        cursor.execute(
            f"""SELECT id FROM {table_name} WHERE {login_col} = '{login}';"""
        )
        account_id = cursor.fetchone()
        return account_id[0]
    else:
        return presence

#connect_cursor()
#test_insert(cursor)
#print(reg(cursor, login_request, password_request))
#print(test_get(cursor, login_request))
#print(str(type(test_get(cursor, 'test_login'))))
#rint(json.dumps(test_get(cursor, 'test_login')))
#close_connect(cursor, connection)


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









