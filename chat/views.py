from email.message import Message
from django.shortcuts import render, redirect
from .models import Room, Massage
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'main.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room).name
    context = {
        'username': username,
        'room': room,
        'room_details': room_details
    }
    return render(request, 'room.html', context)

def checkview(request):
    room = request.POST.get('room_name')
    username = request.POST.get('username')
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        Room.objects.create(name=room)
        return redirect('/' + room + '/?username=' + username)

def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_name = request.POST.get('room_name')

    Massage.objects.create(value=message, user=username, room=room_name)
    return HttpResponse('massage sent succesfully')

def getMassages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Massage.objects.filter(room=room_details.name)

    return JsonResponse({'messages':list(messages.values())})