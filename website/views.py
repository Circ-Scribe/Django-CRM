from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, AddRecordForm
from .models import Record
def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect ('home')
        else:
            messages.success(request, "Invalid credentials")
            return redirect ('home')
    else:
        return render(request, 'home.html',{'records':records})
def logout_user(request):
    logout(request)
    messages.success(request, "You are now logged out")
    return redirect('home')
def signup(request):
    form = SignUpForm(request.POST)
    if request.method == "POST":
        if User.objects.filter(username='username').exists():
            messages.error(request, "Username already exists")
        if form.is_valid():
            form.save()
            #here we authenticate the users
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You are now Registered!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            form = SignUpForm()
            return render(request, 'signup.html', {'form': form})
    else:
        return render(request, 'signup.html', {'form': form})
def customer_record(request, pk):
        if request.user.is_authenticated:
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record': customer_record})
        else:
            messages.error(request, "You are not logged in")
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, "Record Deleted")
        return redirect('home')
    else:
        messages.error(request, "You are not logged in")
        return redirect("home")
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added")
                return redirect('home')
        return render(request, 'add_record.html',{'form': form})
    else:
        messages.error(request, "You are not logged in")
def update_record(request, pk):
    if User.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated")
            return redirect('home')
        return render(request, 'update_record.html',{'form': form})
    else:
        messages.error(request, "You are not logged in")