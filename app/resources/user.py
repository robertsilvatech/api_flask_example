import uuid
from flask_restful import Resource, reqparse
from flask import request
from app.models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name', required=True, help='Field first_name is required')
    parser.add_argument('last_name', required=True, help='Field last_name is required')
    parser.add_argument('email', required=True, help='Field email is required')
    parser.add_argument('password', required=True, help='Field password is required')

    def get(self):
        userid = request.args.get('userid')
        email=request.args.get('email')
        if userid:
            user=UserModel.query.get(userid)
        elif email:
            user=UserModel.find_by_email(email)
        else:
            return {'result': 'Invalid parameter'}, 400
            
        if user:
            print(user.json())
            return {'result': user.json()}
        return {'result': 'User not found'}, 404
        

    def post(self):
        data = User.parser.parse_args()
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        if UserModel.find_by_email(email):
            return {'result': 'Email {} is already registered'.format(email)}, 400
        
        user = UserModel(userid=str(uuid.uuid1()),
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        password=password)
        user.set_password()

        try: 
            user.save_to_db()
            return user.json()
        except Exception as err:
            return {'result': 'There was an error while registering your email {}'.format(email)}, 500

    def delete(self):
        data_json = request.get_json()
        userid = data_json.get('userid')
        if userid:
            user = UserModel.query.get(userid)
            if user:
                user.delete_to_db()
                return {'result': 'User deleted'}
        return {'result': 'Invalid parameters'}

    def put(self):
        data_json = request.get_json()
        userid = data_json.get('userid')
        print(userid)
        if userid:
            print('if aqui')
            user = UserModel.query.get(userid)
            print(user)
            if user is not None:
                first_name = data_json.get('first_name')
                last_name = data_json.get('last_name')
                email = data_json.get('email')
                password = data_json.get('password')
                if first_name:
                    user.first_name = first_name
                if last_name:
                    user.last_name = last_name
                if email:
                    user.email = email
                if password:
                    user.password = password
                    user.set_password()
                user.save_to_db()
                return user.json()
        return {'result': 'Invalid parameters'}, 400