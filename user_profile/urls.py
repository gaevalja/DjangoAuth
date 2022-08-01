from django.urls import path
from .views import *

app_name = 'profile'

urlpatterns =[
    path('<int:id>', profile_index_view, name='profile_index'),
]