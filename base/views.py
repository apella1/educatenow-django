from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

# using function based views 

def home(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()

    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context)

def room_view(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


# creating room form input
def create_room(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


# updating room details

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    context = {'form': form}
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'base/room_form.html', context)


# deleting a room

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request, 'base/delete.html', {'obj': room})