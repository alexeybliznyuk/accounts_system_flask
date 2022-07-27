from flask import Flask
from flask_restful import Api, Resource, reqparse
import db





app = Flask(__name__)
api = Api()
db.connect_cursor()


#parser = reqparse.RequestParser()
#parser.add_argument("name", type=str)
#parser.add_argument("password", type=int)


class Main(Resource):

    def post(self):
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






api.add_resource(Main, "/api/login")
#api.init_app(app)




class Registration(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("login", type=str)
        parser.add_argument("password", type=str)
        account_data = parser.parse_args()
        answer = db.reg(db.cursor, account_data['login'], account_data['password'])
        return answer





api.add_resource(Registration, "/api/reg")
api.init_app(app)






if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
