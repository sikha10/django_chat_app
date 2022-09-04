from django.urls import path
from chat.views import home
from chat.views import room
from chat.views import checkview
from chat.views import send
from chat.views import getMassages

urlpatterns = [
    path('', home, name='home'),
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('send', send, name='send'),
    path('getMessages/<str:room>/', getMassages, name='getMassages')
]