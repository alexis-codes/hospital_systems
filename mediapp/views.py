from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from mediapp.models import *


# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def departments(request):
    return render(request, 'departments.html')


def appointment(request):
    if request.method == 'POST':
        myappointment = Appointment1(
            name = request.POST ['name'],
            email = request.POST ['email'],
            phone = request.POST ['phone'],
            date = request.POST ['date'],
            department = request.POST ['department'],
            doctor = request.POST ['doctor'],
            message = request.POST ['message']
        )
        myappointment.save()
        return redirect('/show')

    else:
        return render(request,'appointment.html')


def contact(request):
    if request.method == 'POST':
        mycontact = contact2 (
        name= request.POST ['name'],
        email= request.POST ['email'],
        subject = request.POST['subject'],
        message = request.POST['message']
        )
        mycontact.save()
        return redirect('/contact')

    else:
        return render(request,'contact.html')


def show(request):
    all = Appointment1.objects.all()
    return render(request, 'show.html', {'all':all})

def delete (request, id):
   deletedappointment= Appointment1.objects.get(id=id)
   deletedappointment.delete()
   return redirect('/show')

def displaycontacts (request):
    contacts = contact2.objects.all()
    return render (request, 'displaycontacts.html', {'all':contacts})

def edit(request,id):
    editinfo = get_object_or_404(Appointment1,id=id)
    if request.method == 'POST':
        editinfo.name = request.POST.get('name')
        editinfo.email = request.POST.get('email')
        editinfo.phone = request.POST.get('phone')
        editinfo.date = request.POST.get('date')
        editinfo.department = request.POST.get('department')
        editinfo.doctor = request.POST.get('doctor')
        editinfo.message = request.POST.get('message')
        editinfo.save()
        return redirect("/show")

    else:
        return render (request,'edit.html', {'editinfo':editinfo})

def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request,user)
            messages.success(request, "You are now logged in!")
            return redirect('index')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')


