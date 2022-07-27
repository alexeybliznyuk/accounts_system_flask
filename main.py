from flask import Flask
from flask_restful import Api, Resource, reqparse
import db





app = Flask(__name__)
api = Api()
db.connect_cursor()
accounts = {
    1: {"login": "Python", "password": "rty"},
    2: {"login": "Java", "password": "qwe"}
}



class Main(Resource):
    def get(self, account_id):
        answer = db.test_get(db.cursor, 'test_login')

        return answer
#        if account_id == 0:
 #           return accounts
#        else:
 #           return accounts[account_id]

    def delete(self, account_id):
        del accounts[account_id]
        return accounts

    def post(self, account_id):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("password", type=str)
        account_data = parser.parse_args()
        answer = db.test_get(db.cursor, account_data['login'])
        if answer['password'] == account_data['password']:
            return answer
        else:

  #          return answer
 #           return "Incorrect login or password"
#        if account_data['login'] == answer['login']:
  #          return account_data
 #       else:
            return "incorrect login or password"
  #      accounts[account_id] = parser.parse_args()




    def put(self, account_id):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("password", type=str)
        accounts[account_id] = parser.parse_args()
        return accounts


api.add_resource(Main, "/api/courses/<int:account_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
