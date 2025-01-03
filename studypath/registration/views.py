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
        pass
    return render(request, 'register.html')