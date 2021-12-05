from datetime import timedelta
from os import environ

JWT_AUTH_REFRESH_COOKIE = 'refresh'
JWT_AUTH_COOKIE = 'jwt-auth'
REST_USE_JWT = True
REST_SESSION_LOGIN = False
CORS_ALLOW_CREDENTIALS = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': environ.get('SECRET_KEY'),
}
