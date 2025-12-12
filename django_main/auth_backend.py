from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from jose import jwt, JWTError
from .settings import SECRET_KEY, Algorithm

SECRET_KEY = SECRET_KEY  # FastAPI'dagi bilan bir xil
ALGORITHM = Algorithm

User = get_user_model()

class JWTBackend(BaseBackend):
    def authenticate(self, request, token=None):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("user_id")

            return User.objects.get(id=user_id)

        except (JWTError, User.DoesNotExist):
            return None
