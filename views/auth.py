from services.authentication import Authentication
from flask import request
# import traceback


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

def verify():
    pass

def me():
    pass