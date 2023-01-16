from django .shortcuts import render,redirect
from .models import user,roomies,facility
from django .contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == "POST":
        name = request.POST['username']
        age = request.POST['age']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        user(name=name, age=age, address=address, email=email, password=password).save()

    return render(request, 'registration.html')

def login(request):
    if request.method == "POST":
        if user.objects.filter(email=request.POST['email'], password=request.POST['password']):
            userdetails = user.objects.get(email=request.POST['email'], password=request.POST['password'])
        else:
            messages.success(request, 'invalid email or password')
    return render(request, 'login.html')

def roompage(request):
    rom = roomies.objects.all()
    return render(request, 'rooms.html', {'rom': rom})

def facilitypage(request):
    if request.method == "POST":
        name = request.POST['username']
        bookno = request.POST.get('bookno')
        email = request.POST['email']
        facility(name=name, bookno=bookno, email=email).save()
    return render(request, 'facilities.html')
