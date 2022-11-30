
from xml.dom.minidom import Document
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect


from .models import User
from course.models import Major


def signUp(request):
    if request.method == 'POST':
        user_number = request.POST.get('user_number')
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        major = request.POST.get('majoritem')

        m = Major.objects.get(pk=major)
        user = User(user_number=user_number, user_name=user_name, user_password=user_password, major =m)
        user.save()
        return HttpResponseRedirect('/index/') #httpresponseRedirect로 main.html로 가게 만들 것

    return render(request, 'user/signUp.html')

def signIn(request):
    if request.method == "POST":
        user_number = request.POST.get('user_number')
        user_password = request.POST.get('user_password')

        try:
            user = User.objects.get(user_number=user_number, user_password=user_password)
            request.session['user_number'] = user_number
            # return render(request, 'templates/index.html')
            return HttpResponseRedirect('/index/')
        except User.DoesNotExist:
            return HttpResponse('로그인실패')
      
    return render(request, 'user/signIn.html')

def signOut(request):
    del request.session['user_number'] # 개별 삭제
    request.session.flush() # 전체 삭제

    return HttpResponseRedirect('/index/')

