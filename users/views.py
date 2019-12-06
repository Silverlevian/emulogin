from django.shortcuts import render, redirect

# Create your views here.

def welcome(request):
    return render(request, "users/welcome.html")

def register(request):
    return render(request, "users/register.html")

def login(request):
    return render(request, "users/login.html")

def logout(request):
	return redirect('/')

#Log out

from django.contrib.auth import logout as do_logout

def logout(request):

    do_logout(request)

    return redirect('/')

# implementando la pagina de bienvenida

def welcome(request):
    # si es exitoso devolvemos a la pagina de inicio (welcome)
    if request.user.is_authenticated:
        return render(request, "users/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

#implementando el login
	
	#importacion de librerias
from django.contrib.auth import authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

	#implementacion

def login(request):

	form = AuthenticationForm()
	if request.method == "POST":

		form = AuthenticationForm(data=request.POST)
		#si esta correcto
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			#verificacion de usuario
			user = authenticate(username=username, password=password)

			if user is not None:
				do_login(request,user)
				return redirect('/')
	return render(request, "users/login.html", {'form': form})

#creacion de usuarios

	#importacion de librerias
from django.contrib.auth.forms import UserCreationForm

#creacion del registro

def register(request):

	form = UserCreationForm()
	if request.method == "POST":

		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			#si esta todo bien
			user = form.save()
			#lo llevamos a hacer login normalmente
			if user is not None:
				do_login(request,user)
				return redirect('/')

	return render(request, "users/register.html", {'form': form})