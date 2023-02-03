from django.shortcuts import render
from .models import Room

rooms = [
    {'id':1, 'name': 'Open Source Contribution Guidelines'},
    {'id':2, 'name': 'Fullstack JavaScript'},
    {'id':3, 'name': 'Pythonistas Assemble'},
    {'id':4, 'name': 'Gophers Dynasty'},
]

# using function based views 

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room_view(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i 
    context = {'room': room}
    return render(request, 'base/room.html', context)
