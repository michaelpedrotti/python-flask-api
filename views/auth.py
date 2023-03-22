from decorators.authentication import is_authenticated
from services.authentication import Authentication
from services.user import UserService
from helpers.password import password_generator
from flask import g, request
# from pprint import pprint
import traceback

class AuthView():

    def login(email = '', password = ''):
        
        json = {'error': False}

        try:
            service = Authentication()

            user = service.authenticate(
                request.form.get('email'), 
                request.form.get('password')
            )

            token = service.generate(user["id"])

            json["data"] = {
                "token": token,
                "expires": 'time'
            }

        except Exception as e:
            # print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        
        return json

    @is_authenticated
    def verify():
        pass

    @is_authenticated
    def my_self():
        
        json = {'error': False}

        try:
            user = g.get('user')
        
            if(user is None):
                raise Exception('User not found')

            user: dict = UserService().find(user.get('id'), True)

            user.pop('id')
            user.pop('profile_id')

            del user["profile"]["id"]


            json["data"] = user

        except Exception as e:
            print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        
        return json

    @is_authenticated
    def set_auth_setting():
        json = {'error': False}

        try:

            user_id = g.get('user').get('id')

            data = {'name': request.form['name']}

            if 'new_password' in request.form:
                password, encrypt = password_generator(request.form['new_password'])
                data['password'] = encrypt
            
            UserService().update(user_id, data)

        except Exception as e:
            print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        
        return json

    @is_authenticated
    def get_auth_setting():
        json = {'error': False, "form": {}}

        try:
            user_id = g.get('user').get('id')

            user: dict = UserService().find(user_id, True)

            user.pop('id')
            user.pop('profile_id')

            del user["profile"]["id"]

            json["data"] = user

        except Exception as e:
            print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        
        return json