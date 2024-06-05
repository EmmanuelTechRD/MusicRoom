from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from . import models as m
from . import serializers as s

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = m.Room.objects.all()
    serializer_class = s.RoomSerializer