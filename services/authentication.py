import jwt
import os
from models.user import UserModel
from helpers import passwordCompare


class Authentication():
    
    def authenticate(self, email = '', password = ''):
        model = UserModel.query.filter_by(email=email).first()
        
        if model is None:
            raise Exception('E-mail was not found')
        
        if passwordCompare(password, model.password) == False:
             raise Exception('E-mail or Password were wrong')
        
        return model.serialize


    def generate(self, user_id):
        
        return jwt.encode(
            {"id": user_id}, 
            os.environ.get('JWT_SECRET', 'secret'), 
            algorithm="HS256"
        )

    def verify(self, token = ''):
        return jwt.decode(
            token, 
            os.environ.get('JWT_SECRET', 'secret'), 
            algorithms=["HS256"]
        )
    
    def expires(self, token: str = ''):
        pass