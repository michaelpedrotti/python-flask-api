from flask.views import MethodView
from flask import request
from pprint import pprint

class BaseView(MethodView):

    init_every_request = False

    def index(self):
        return {"error": False, "message": "index was not implemented"}

    def create(self):
        return {"error": False, "message": "create was not implemented"}

    def store(self):
        return {"error": False, "message": "store was not implemented"}

    def show(self, id):
        return {"error": False, "message": "show was not implemented"}

    def edit(self, id):
        return {"error": False, "message": "edit was not implemented"}

    def update(self, id):
        return {"error": False, "message": "update was not implemented"}

    def detroy(self, id):
        return {"error": False, "message": "detroy was not implemented"}


    def get(self, id = None):

        path = request.url_rule.__str__()

        if id: # show
            if path.endswith("edit"):
                return self.edit(id)
            else:
                return self.show(id)
        else: # Index
            if path.endswith("new"):
                return self.create()
            else:
                return self.index()

    def post(self):
        return self.store()

    def put(self, id = 0):
       return self.update(id)

    def delete(self, id = 0):
        return self.detroy(id)