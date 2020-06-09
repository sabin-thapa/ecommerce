from store.models import *
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from store.views import store
from store.models import Customer
from django.contrib.auth.forms import UserCreationForm

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('store')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)


def register(request):
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')

				Customer.objects.create(user=user,)

				messages.success(request, 'Account was created for ' + username)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def logoutPage(request):
	logout(request)
	return redirect('login')