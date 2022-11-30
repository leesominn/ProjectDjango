from . import views
from django.urls import path

app_name = 'course'

urlpatterns = [
    path('getcourse/', views.getCourse),
    path('showMyCourse/', views.showmyCourse),
    path('insertCourse/', views.insertCourse),
    path('deleteCourse/', views.deleteCourse),
    
]