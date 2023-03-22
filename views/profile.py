from .base import BaseView
from services.profile import ProfileService
from pprint import pprint
from flask import request
from helpers.request import get_body
from validators.profile import ProfileValidator
import traceback

class ProfileView(BaseView):
    
    init_every_request = False

    # decorators = [login_required]

    def index(self):
        json = {'error': False}
        try:
            json.update(ProfileService().paginate(request.args))
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
            form = ProfileValidator()
            if not form.validate():
                json["errors"] = form.errors
                raise Exception("Check fields")
            
            json["data"] = ProfileService().create(form.data)

        except Exception as e:
            json["message"] = str(e)
            json["error"] = True
        return json

    def show(self, id = 0):
        json = {'error': False}
        try:
            json["data"] = ProfileService().find(id, True)
        except Exception as e:
            print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        return json

    def edit(self, id = 0):
        json = {'error': False, "form": {}}
        try:
            json["data"] = ProfileService().find(id, True)
        except Exception as e:
            json["message"] = str(e)
            json["error"] = True
        return json

    def update(self, id = 0):
        json = {'error': False}
        try:
            form = ProfileValidator()
            if not form.validate():
                json["errors"] = form.errors
                raise Exception("Check fields")
            
            json["data"] = ProfileService().update(id, get_body(request))
        except Exception as e:
            print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        return json

    def detroy(self, id):
        json = {'error': False}
        try:
            json["data"] = ProfileService().delete(id)
        except Exception as e:
            # print(traceback.format_exc())
            json["message"] = str(e)
            json["error"] = True
        return json
    
