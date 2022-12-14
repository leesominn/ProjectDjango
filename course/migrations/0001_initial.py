# Generated by Django 3.2.5 on 2022-07-22 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'major',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.IntegerField()),
                ('course_credit', models.FloatField()),
                ('course_lectureroom', models.CharField(max_length=45)),
                ('course_time', models.CharField(max_length=45)),
                ('course_cnt', models.IntegerField()),
                ('course_professor', models.CharField(max_length=45)),
                ('course_grade', models.IntegerField()),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course.major')),
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]
