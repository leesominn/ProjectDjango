from . import views
from django.urls import path

app_name = "user"

urlpatterns = [

    path('signup/', views.signUp),
    path('signin/', views.signIn),
    path('signout/', views.signOut),
]