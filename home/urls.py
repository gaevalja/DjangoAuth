from django.urls import include, path
from .views import *

app_name='home'
urlpatterns=[
    path('', index_view, name='index'),
]