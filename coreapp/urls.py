from django.urls import path, include
from rest_framework import routers
from .views import SignupUserView, LoginUserView, LogoutUserView

router = routers.DefaultRouter()

router.register('signup', SignupUserView, basename='signup')
router.register('login', LoginUserView, basename='login')
router.register('logout', LogoutUserView, basename='logout')

urlpatterns = [
    path('', include(router.urls)),
]