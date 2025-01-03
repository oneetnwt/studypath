from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def login(request):
    if request.method == "POST":
        studentId = request.POSt('studentID')
        password = request.POST('password')

        if len(studentId) == 0 or len(password) >= 10:
            messages.error(request, 'Invalid student ID')
            return redirect('login')
        elif password == "":
            messages.error(request, 'Fill the password field')
            return redirect('login')
        else:
            pass
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST('first_name')
        last_name = request.POST('last_name')
        email = request.POST('email')
        studentId = request.POST('studentID')
        password = request.POST('password')
        password2 = request.POST('password2')

        if len(studentId) == 0 or len(password) >= 10:
            messages.error(request, 'Invalid student ID')
            return redirect('register')
        elif len(password) < 8:
            messages.error(request, 'Password must be at least 8 characters')
            return redirect('register')
        elif password != password2:
            messages.error(request, 'Password does not match')
            return redirect('register')
        else:
            pass
    return render(request, 'register.html')