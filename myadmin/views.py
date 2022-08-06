from django.shortcuts import render
from .models import Announcements
# Create your views here.

def announcements_view(request):
    context = {
        'announcements': Announcements.objects.all()
    }
    return render(request, 'myadmin/announcements_index.html', context)

def announcements_detail_view(request):
    pass

def announcements_update_view(request):
    pass

def announcements_delete_view(request):
    pass

