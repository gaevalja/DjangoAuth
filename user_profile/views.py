from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from users.models import *
# Create your views here.
def profile_index_view(request, id):
    if request.method == 'POST':
        return HttpResponse(request.POST)
    elif request.method =='GET':
        if request.user.is_authenticated and request.user.id == id:
            user = User.objects.get(id=id)
            context = {
                'user':user,

            }
            
            return render(request, 'user_profile/profile_main.html', context)
        else:
            # 다른유저의 프로필 접속 시도
            logout(request)
            return redirect('home:index')