from django.urls import path
from . import views as v

urlpatterns = [
    path('room', v.RoomView.as_view(), name='room_view'),
    path('create_room', v.CreateRoomView.as_view(), name='create_room'),
]
