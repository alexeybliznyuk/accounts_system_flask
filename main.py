from flask import Flask
from flask_restful import Api, Resource, reqparse
import db
from config import flask_host, flask_port







app = Flask(__name__)
api = Api()
db.connect_cursor()





class Main(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("password", type=str)
        account_data = parser.parse_args()
        answer = db.get_by_login(db.cursor, account_data['login'])
        if answer['password'] == account_data['password']:
            return answer
        else:


            return "incorrect login or password"






#добавляет api
api.add_resource(Main, "/api/login")




#по post запросу на /api/reg при уникальности логина возвращает id зарегестрированного аккаунта
#а пре неудачной возвращает "
class Registration(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("password", type=str)
        account_data = parser.parse_args()
        answer = db.reg(db.cursor, account_data['login'], account_data['password'])
        return answer





api.add_resource(Registration, "/api/reg")  #добавляет api
api.init_app(app)





#Запускает flask сервер
if __name__ == "__main__":
    app.run(debug=True, port=flask_port, host=flask_host)
