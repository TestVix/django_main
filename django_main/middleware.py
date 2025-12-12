from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import authenticate

class JWTAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        auth = request.headers.get("Authorization")
        if not auth:
            return

        try:
            prefix, token = auth.split()
            if prefix.lower() != "bearer":
                return
        except:
            return

        user = authenticate(request, token=token)
        if user:
            request.user = user
