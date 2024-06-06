from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='home'),
    path('join', v.index, name='join_room'),
    path('create', v.index, name='create_room')
]