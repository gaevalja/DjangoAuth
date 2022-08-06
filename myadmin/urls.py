from django.urls import path
from .views import *

app_name = 'myadmin'
urlpatterns = [
    path('announcements/', announcements_view, name='announcements'),
    # path('announcements/<int:announcement_id>'),
    # path('annoucnements/<int:announcement_id>/check'),
]