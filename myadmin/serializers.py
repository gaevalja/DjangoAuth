from rest_framework import serializers
from .models import Announcements
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'

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

class AnnouncementList(APIView):
    #04-01 공지 리스트 전체 조회
    def get(self, request):
        announcements = Announcements.objects.all()
        serializer = AnnouncementsSerializer(announcements , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)