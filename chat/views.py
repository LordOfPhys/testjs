from django.shortcuts import render
from django.utils.safestring import mark_safe
from chat.models import Room, Message
import json
import random

def take_numbers(request):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    data = {'lenght': a, 'height': b, 'success': True}
    return HttpResponse(json.dumps(data))

def pole(request):
    return render(request, 'chat/pole.html', {})

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    room = Room.objects.get_or_create(label=room_name)
    room = Room.objects.get(label=room_name)
    messages = list(Message.objects.filter(room=room))
    answer = []
    for i in range(len(messages)):
        answer.append(messages[i].get_Text())
    print(answer)
    return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)), 'old_messages': mark_safe(json.dumps(answer))})
