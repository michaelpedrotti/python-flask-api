from .base import BaseView


class UserView(BaseView):

    def index(self):
        return {"error": False, "message": "index override"}