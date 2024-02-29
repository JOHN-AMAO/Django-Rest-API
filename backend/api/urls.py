from django.urls import path
from rest_framework.authtoken.views import obtain_auth_tokens
from . import views 

urlpatterns = [
    path("auth/", obtain_auth_tokens),
    path("", views.api_home)
]