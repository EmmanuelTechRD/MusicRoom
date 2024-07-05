from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from . import models as m
from . import serializers as s
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = m.Room.objects.all()
    serializer_class = s.RoomSerializer
    
class GetRoom(APIView):
    serializer_class = s.RoomSerializer
    lookup_url_kwarg = 'code'
    
    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code != None:
            room = m.Room.objects.filter(code=code)
            if len(room) > 0:
                data = s.RoomSerializer(room[0]).data
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)
            return Response({'Room Not Found': 'Invalid Room Code.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request': 'Code parameter not found in request.'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class CreateRoomView(APIView):

    serializer_class = s.CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = m.Room.objects.filter(host=host)

            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(s.RoomSerializer(room).data, status=status.HTTP_200_OK)
            
            else:
                room = m.Room(
                        host=host, 
                        guest_can_pause=guest_can_pause, 
                        votes_to_skip=votes_to_skip
                    )
                room.save()
                return Response(s.RoomSerializer(room).data, status=status.HTTP_201_CREATED)
                
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)