from django.contrib import admin
from django.urls import include, path
import config.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('course/', include('course.urls')),
    path('index/', views.index),
    path('', views.index),
]
