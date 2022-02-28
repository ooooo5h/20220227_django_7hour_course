from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1, 'name':"Let's learn python"},
    {'id':2, 'name':"Desing with me"},
    {'id':3, 'name':"Frontend developters"},
]


def home(request):
    return render(request, 'home.html', {'rooms' : rooms})

def room(request):
    return render(request, 'room.html')