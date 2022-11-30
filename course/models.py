from django.db import models

class Major(models.Model):
    major_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'major'

class Course(models.Model):
    course_name = models.IntegerField()
    course_credit = models.FloatField()
    course_lectureroom = models.CharField(max_length=45)
    course_time = models.CharField(max_length=45)
    course_cnt = models.IntegerField()
    course_professor = models.CharField(max_length=45)
    course_grade = models.IntegerField()
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'course'
