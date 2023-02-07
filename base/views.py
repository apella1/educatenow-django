from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic, Message
from .forms import RoomForm, MessageForm

# using function based views

# user profile view


def user_profile(request, pk):
    user = User.objects.get(id=pk)
    # getting children of the room object
    rooms = user.room_set.all()
    comments = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms,
               'comments': comments, 'topics': topics}

    return render(request, 'base/user_profile.html', context)


def login_view(request):
    page = 'login'
    # a logged in user should not access the login page
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        # converting the username to lower as in the registration form
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credentials do not match')

    context = {'page': page}
    return render(request, 'base/user_auth.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # using commit=False to be able to access the user right away
            user = form.save(commit=False)

            # manipulating the input
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'base/user_auth.html', context)


def home(request):
    # assignment using inline if
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # case sensitivity for icontains(makes it case insensitive with i included) - for matching url queries
    # django using & and | instead of 'and' and 'or'
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()

    # showcasing messages related to a specific search query
    comments = Message.objects.filter(Q(room__topic__name__icontains=q))
    context = {'rooms': rooms, 'topics': topics,
               'room_count': room_count, 'comments': comments}
    return render(request, 'base/home.html', context)


def room_view(request, pk):
    room = Room.objects.get(id=pk)

    ''' Set of messages related to the room
        meesage_set - message is the model but it's not capitalized
        all the comments available for the room are then accessed
    '''
    comments = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            # 'body' is the name given to the input field within the comment form
            body=request.POST.get('body')
        )
        # adding a user to the participants list after contributing
        room.participants.add(request.user)

        # processing page rerender with a get request
        return redirect('room', pk=room.id)

    context = {'room': room, 'comments': comments,
               'participants': participants}
    return render(request, 'base/room.html', context)


# creating room form input
# using login_required decorator to limit access to create room functionality

@login_required(login_url='login')
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

@login_required(login_url='login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    context = {'form': form}

    if request.user != room.host:
        return HttpResponse('You are not authorized to manipulate this page!')

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/room_form.html', context)


# deleting a room

@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse('You are not authorized to manipulate this page!')

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})

# editing a message


@login_required(login_url='login')
def update_message(request, pk):
    comment = Message.objects.get(id=pk)
    form = MessageForm(instance=comment)
    context = {'form': form}

    if request.user != comment.user:
        return HttpResponse("You can't edit others' comments")

    if request.method == 'POST':
        form = MessageForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/message_form.html', context)

# deleting a message


@login_required(login_url='login')
def delete_message(request, pk):
    comment = Message.objects.get(id=pk)

    if request.user != comment.user:
        return HttpResponse("You can't delete others' comments.")

    if request.method == 'POST':
        comment.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': comment})
