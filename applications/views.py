from django.shortcuts import render, redirect
from .models import Application
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    apps = Application.objects.filter(user=request.user).order_by('-applied_date')
    return render(request, 'home.html', {'apps': apps})


def add_application(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        role = request.POST.get('role')
        status = request.POST.get('status')
        applied_date = request.POST.get('applied_date')
        notes = request.POST.get('notes') or ""

        if not company or not role or not applied_date:
            return render(request, 'add.html', {'error': 'Please fill all required fields'})

        Application.objects.create(
            user=request.user,
            company=company,
            role=role,
            status=status,
            applied_date=applied_date,
            notes=notes
        )

        return redirect('home')

    return render(request, 'add.html')


@login_required
def edit_application(request, id):
    app = Application.objects.get(id=id)

    if request.method == 'POST':
        app.company = request.POST.get('company')
        app.role = request.POST.get('role')
        app.status = request.POST.get('status')
        app.applied_date = request.POST.get('applied_date')
        app.notes = request.POST.get('notes') or ""

        app.save()
        return redirect('home')

    return render(request, 'edit.html', {'app': app})


@login_required
def delete_application(request, id):
    app = Application.objects.get(id=id)
    app.delete()
    return redirect('home')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')