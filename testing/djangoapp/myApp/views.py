from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import connection
from .models import User, Feedback


# LOGIN 

def login_view(request):

    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        query = f"SELECT * FROM myApp_user WHERE username='{username}' AND password='{password}'"
        with connection.cursor() as cursor:
            cursor.execute(query)
            user = cursor.fetchone()
        if user:
            request.session['user'] = username
            return redirect('/dashboard')
        else:
            error = "Invalid credentials"
    return render(request, 'login.html', {"error": error})


# REGISTRATION 

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        User.objects.create(username=username, password=password)
        return redirect('/login')
    return render(request, 'register.html')


# DASHBOARD

def dashboard_view(request):
    user = request.session.get('user')
    if not user:
        return redirect('/login')
    return render(request, 'dashboard.html', {'user': user})


# FEEDBACK PAGE (STORED XSS VULNERABILITY)

@login_required(login_url="/login")
def feedback_view(request):

    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
    
        Feedback.objects.create(name=name, message=message)
    data = Feedback.objects.all()
    return render(request, 'feedback.html', {'data': data})



def admin_panel(request):
    user = request.session.get('user')
    if not user:
        return redirect('/login')
    
    users = User.objects.all()
    return render(request, 'adminpanel.html', {'user': user, 'users': users})
    

# IDOR
def profile(request, id):
    user = User.objects.get(id=id)
    return render(request, 'dashboard.html', {'user': user})


# LOGOUT
def logout_view(request):   
    request.session.flush()
    return redirect('/login')