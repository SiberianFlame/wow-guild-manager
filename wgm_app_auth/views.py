import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from wgm_app_auth.models import UserProfile


class SignUpView(APIView):
    """
    Class for creating new user, new profile and basket
    """

    def post(self, request: Request, *args, **kwargs) -> HttpResponse:
        """
        Creating user, profile and login new user
        :param request: Request object from user
        :return: HttpResponse with status 200 if everything is ok, 500 if something went wrong
        """

        body = json.loads(request.body)
        username = body['username']
        password = body['password']
        first_name = body['name']

        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        profile = UserProfile.objects.create(user=user)

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=500)

