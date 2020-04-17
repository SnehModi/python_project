from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def index(request):
    my_dict = {'insert_me': 'Hello , Now I am from first_app -  index.html !'}
    return render(request, 'first_app/index.html', context=my_dict)


def home_view(request):
    return render(request, 'first_app/home.html')


def about_view(request):
    return render(request, 'first_app/about.html')


def earth_view(request):
    return render(request, 'first_app/earthquake.html')


def flood_view(request):
    return render(request, 'first_app/flood.html')


def drth_view(request):
    return render(request, 'first_app/drought.html')


def land_view(request):
    return render(request, 'first_app/landslide.html')


def thankyou_view(request):
    return render(request, 'first_app/thankyou.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login the user
            login(request, user)
            return redirect('first_app:home')
    else:
        form = UserCreationForm()
    return render(request, 'first_app/registration_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('first_app:home')
    else:
        form = AuthenticationForm()
    return render(request, 'first_app/login_form.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('first_app:login')


def donate_view(request):
    if request.method == 'GET':
        return redirect('first_app:earthquake')


def donate2_view(request):
    if request.method == 'GET':
        return redirect('first_app:flood')


def donate3_view(request):
    if request.method == 'GET':
        return redirect('first_app:drought')


def donate4_view(request):
    if request.method == 'GET':
        return redirect('first_app:landslide')


def donate1_view(request):
    if request.method == 'GET':
        return redirect('first_app:thankyou')

