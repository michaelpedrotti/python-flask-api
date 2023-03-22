import jwt
from os import getenv
from models.user import UserModel
from helpers.password import password_compare


class Authentication():
    
    def authenticate(self, email = '', password = ''):
        model = UserModel.query.filter_by(email=email).first()
        
        if model is None:
            raise Exception('E-mail was not found')
        
        if password_compare(password, model.password) == False:
             raise Exception('E-mail or Password were wrong')
        
        return model.serialize


    def generate(self, user_id):
        
        return jwt.encode(
            {"id": user_id}, 
            getenv('JWT_SECRET', 'secret'), 
            algorithm="HS256"
        )

    def verify(self, token = ''):
        return jwt.decode(
            token, 
            getenv('JWT_SECRET', 'secret'), 
            algorithms=["HS256"]
        )
    
    def expires(self, token: str = ''):
        pass