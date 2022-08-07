from django.urls import path
from .views import *

urlpatterns = [
    path('announcements/', Announcements_view.as_view(), name='announcements'),
    # path('announcements/create/', announcements_create_view, name='announcements_create'),
    # path('announcements/<int:announcement_id>', Announcements_detail_view.as_view(), name='announcements_detail'),
    # path('annoucnements/<int:announcement_id>/check'),
]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

app_name = 'myadmin'

urlpatterns = [
    path('announcements/', Announcements_view.as_view(), name='admin_announcements'),
    path('announcements/<int:pk>/', AdminAnnouncementsDetail.as_view(), name='admin_announcements_detail'),
    path('announcements/<int:pk>/check/', AdminAnnouncementsCheckDetail.as_view(), name='admin_announcements_check'),
]

urlpatterns = format_suffix_patterns(urlpatterns)