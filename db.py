import psycopg2

from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import db_host, db_port, db_user, db_password




table_name = 'users'




# Подключение к базе данных
def connect_cursor():
    global connection, cursor
    try:

        connection = psycopg2.connect(user=db_user,

                                    password=db_password,
                                    host=db_host,
                                    port=db_port)
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




#отключение сервера
def close_connect(cursor, connection):

    cursor.close()
    connection.close()
    print("Соединение с PostgreSQL закрыто")





#получение пароля  по логину из дб
def get_by_login(cursor, login_request):

    cursor.execute(
        f"""SELECT password FROM {table_name} WHERE login = '{login_request}';"""
    )
    
    cursor_fetch = cursor.fetchone()
    if cursor_fetch == None:

        answer = {'login': login_request, 'password': cursor_fetch}
        return answer




    else:
        cursor.execute(
            f"""SELECT id FROM {table_name} WHERE login = '{login_request}';"""
        )
        account_id = cursor.fetchone()
        answer = {'login': login_request, 'password': cursor_fetch[0], 'id': account_id[0]}
        return answer







#проверяет наличие в дб по логину для reg
def check_presence(cursor, login):

    cursor.execute(
        f"""SELECT id FROM {table_name} WHERE login = '{login}';"""
    )
    account_id = cursor.fetchone()
 #   print(account_id)
    if account_id == None:
        return "This login is free"
    else:
        return "This login already used"

#регистрация при удаче возвращает id, при неудаче "This login already used"
def reg(cursor, login, password):
    presence = check_presence(cursor, login)
    if presence == "This login is free":
        cursor.execute(
            f"""INSERT INTO users (login, password) VALUES
            ('{login}', '{password}');"""
        )
        cursor.execute(
            f"""SELECT id FROM {table_name} WHERE login = '{login}';"""
        )
        account_id = cursor.fetchone()
        return account_id[0]
    else:
        return presence














