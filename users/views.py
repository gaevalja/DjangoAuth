from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .models import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password) # user가 인증되면 user객체 반환, 인증되지 않으면 None객체 반환
        if user is not None:
            # A backend authenticated the credentials
            print('인증성공')
            login(request, user)
            return redirect('home:index')
        else:
            # No backend authenticated the credentials
            print('인증실패')
            if not User.objects.filter(username=username).exists():
                content = '아이디를 확인해주세요'
            else:
                content = '비밀번호를 확인해주세요'
            return render(request, 'users/login.html', {'content':content})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('users:login')

def signup_view(request):
    if request.method == 'POST':
        print(request.POST)


        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        age = request.POST['age']

        if User.objects.filter(username=username).exists():
            return render(request, 'users/signup.html', {'content':'이미 사용중인 아이디입니다.'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'users/signup.html', {'content':'이미 사용중인 이메일입니다.'})
        
        if username and email and password and firstname and lastname and age:
            print(username)
            print(email)
            print(password)
            print(firstname)
            print(lastname)
            print('age: ', age)
            
            user = User.objects.create_user(username, email, password, first_name=firstname, last_name=lastname, age=age)
            user.save()
            
            login(request, user)
            return redirect('home:index')
        else:
            print(request.POST)
            return render(request, 'users/signup.html', {'content':'양식을 제대로 입력하세요'})
    return render(request, 'users/signup.html')