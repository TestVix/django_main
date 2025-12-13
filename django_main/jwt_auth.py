import jwt
from django_main.settings import SECRET_KEY
from functools import wraps

ALGORITHM = "HS256"

def jwt_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get("access_token")
        request.user_jwt = None  # default: user yo‘q
        if token:
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                request.user_jwt = payload.get("sub")  # username yoki user_id
            except jwt.ExpiredSignatureError:
                request.user_jwt = None
            except jwt.InvalidTokenError:
                request.user_jwt = None

        return view_func(request, *args, **kwargs)

    return wrapper
