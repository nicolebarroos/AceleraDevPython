import jwt

#ref: https://pyjwt.readthedocs.io/en/latest/

secret = 'acelera'

def create_token(data, secret):
    encoded_jwt = jwt.encode(data, secret, algorithm='HS256')
        
    return encoded_jwt   

def verify_signature(token):
    try:
        decoded_jwt = jwt.decode(token, secret, algorithms=['HS256'])

    except jwt.InvalidTokenError:
        decoded_jwt = {'error': 2}

    return decoded_jwt