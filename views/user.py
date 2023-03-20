from .base import BaseView
from services.user import UserService
from pprint import pprint
from flask import request
from helpers import get_body
import traceback

class UserView(BaseView):
    
    # decorators = [login_required]

    def index(self):
        json = {'error': False}
        try:
            json.update(UserService().paginate(request.args))
        except Exception as e:
            print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        return json

    def create(self):
        return {"error": False, "form": {}}

    def store(self):
        json = {'error': False}
        try:
            json["data"] = UserService().create(get_body(request))
        except Exception as e:
            print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        return json

    def show(self, id = 0):
        json = {'error': False}
        try:
            json["data"] = UserService().find(id)
        except Exception as e:
            json["message"] = str(e)
            json["error"] = True
        return json

    def edit(self, id = 0):
        json = {'error': False, "form": {}}
        try:
            json["data"] = UserService().find(id)
        except Exception as e:
            json["message"] = str(e)
            json["error"] = True
        return json

    def update(self, id = 0):
        json = {'error': False}
        try:
            json["data"] = UserService().update(id, get_body(request))
        except Exception as e:
            # print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        return json

    def detroy(self, id):
        json = {'error': False}
        try:
            json["data"] = UserService().delete(id)
        except Exception as e:
            # print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        return json
    
