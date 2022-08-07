from django.urls import include, path
from .views import *
from myadmin.views import *
app_name='home'
urlpatterns=[
    path('', index_view, name='index'),
    path('announcements/', AnnouncementsList.as_view(), name='announcements'),
]