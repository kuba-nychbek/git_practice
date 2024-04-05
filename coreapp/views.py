from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db import IntegrityError


class SignupUserView(APIView):
    def post (self, request):
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = get_user_model().objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return Response({'message': 'User created successfully'})
            except IntegrityError:
                return Response({'error': 'That username has already taken. Please choose a new username'}, status=400)

        else:
            return Response({'error': 'Passwords did not match'}, status=400)

class LoginUserView(APIView):
    def post(self, request):
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return Response({'error': 'Username and password did not match'}, status=400)
        else:
            login(request, user)
            return Response({'message': 'User logged in successfully'})
        
class LogoutUserView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully'})
