from rest_framework import serializers
from . import models as m

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 
                  'votes_to_skip', 'created_at')
        
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Room
        fields = ('guest_can_pause', 'votes_to_skip')