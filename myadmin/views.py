from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from .models import Announcements
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AnnouncementsSerializer
from django.http import Http404
class Announcements_view(APIView):
     def post(self, request):
        serializer = AnnouncementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminAnnouncementsDetail(APIView):
    def get_announcement(self, pk):
        try:
            return Announcements.objects.get(pk=pk)
        except Announcements.DoesNotExist:
            raise Http404

    #00-16 조회
    def get(self, request, pk):
        announcement = self.get_announcement(pk)
        serializer = AnnouncementsSerializer(announcement)
        return Response(serializer.data, status=status.HTTP_200_OK)

    #00-13 수정
    def put(self, request, pk):
        announcement = self.get_announcement(pk)
        serializer = AnnouncementsSerializer(announcement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #00-14 삭제
    def delete(self, request, pk):
        announcement = self.get_announcement(pk)
        announcement.delete()
        return Response(status=status.HTTP_200_OK)


#00-15 important, visible 수정
class AdminAnnouncementsCheckDetail(APIView):
    def get_object(self, pk):
        try:
            return Announcements.objects.get(pk=pk)
        except Announcements.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementsSerializer(announcement, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AnnouncementsList(APIView):
    #04-01 공지 리스트 전체 조회
    def get(self, request):
        Announcementss = Announcements.objects.all()
        serializer = AnnouncementsSerializer(Announcementss, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
