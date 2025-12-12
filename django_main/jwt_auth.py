import jwt
from django.conf import settings
from django.http import JsonResponse

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

def jwt_required(view_func):
    def wrapper(request, *args, **kwargs):
        token = request.COOKIES.get("access_token")
        if not token:
            return JsonResponse({"message": "Token yo‘q"}, status=401)

        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            request.user_jwt = payload["sub"]  # username
        except jwt.ExpiredSignatureError:
            return JsonResponse({"message": "Token muddati tugagan"}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({"message": "Token noto‘g‘ri"}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapper
