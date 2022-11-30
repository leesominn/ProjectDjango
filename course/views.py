from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from course.models import Course
from user.models import User

def getCourse(request): #전체과목 조회
    get_course = Course.objects.all()
    return render(request, 'course/getCourse.html', { #html은 C를 대문자로
        'get_course': get_course # ''안에 들어가는 get_course가 html로
    })

def insertCourse(request): #수강신청
    course_id = request.GET.get('course_id')
    user_id = request.session.get('user_number')

    # 로그인되어 있는 사용자의 User 객체 조회
    user = User.objects.get(pk=user_id)
    course = Course.objects.get(pk=course_id)
    
    course.user_set.add(user)
    # 또는... 아래 / 위 둘 중 한개만 사용
    # user.course.add(course)

    return JsonResponse(model_to_dict(course))

def showmyCourse(request):
    user_id = request.session.get('user_number')

    user = User.objects.get(pk=user_id)
    courselist = user.course.all()
    
    return render(request, 'course/courseList.html', {
        'courseList': courselist
    })

def deleteCourse(request): #수강신청
    course_id = request.GET.get('course_id')
    user_id = request.session.get('user_number')
    
    # 로그인되어 있는 사용자의 User 객체 조회
    user = User.objects.get(pk=user_id)
    course = Course.objects.get(pk=course_id)
    
    course.user_set.remove(user)
    # 또는... 아래 / 위 둘 중 한개만 사용
    # user.course.add(course)

    return JsonResponse(model_to_dict(course))