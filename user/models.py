from django.db import models
from course.models import Major, Course

class User(models.Model):
    user_number = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=45)
    user_grade = models.IntegerField(default=1)
    user_maxcredit = models.IntegerField(default=19)
    user_password = models.CharField(max_length=15)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)
    course = models.ManyToManyField(Course)
    

    class Meta:
        db_table = 'user'