from django.http import HttpResponse
from django.shortcuts import render
from users.models import *
# Create your views here.
def profile_index_view(request, id):
    if request.method == 'POST':
        return HttpResponse(request.POST)
    elif request.method =='GET':
        user = User.objects.get(id=id)
        return render(request, 'user_profile/profile_main.html', {'user':user})