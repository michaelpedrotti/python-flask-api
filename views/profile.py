from .base import BaseView

class ProfileView(BaseView):
    
    init_every_request = False

    # decorators = [login_required]

    def index(self):
        return {"error": False, "message": "index override"}