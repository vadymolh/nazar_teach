from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Categories
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

def buy_Skyrim(request):
	return HttpResponse("""<h1>This is America</h1>
							<a href ="https://steamcommunity.com/profiles/76561198269458856">a</a>""")
def Bethesda(request):
		return render(request, "store/home.html", {'News' : Product.objects.all})

def show_categories(request):
	return render(request, "store/categories.html",{'cat': Categories.objects.all})

def separator(request, url_slug):
	categories_urls = [c.url_slug for c in Categories.objects.all()]
	if url_slug in categories_urls:
		posts = Product.objects.filter(news_caregory__url_slug = url_slug)
	return HttpResponse("Not a category")

def _Registration(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect("Store:home")
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}:{form.error_messages[msg]}")
	form = NewUserForm
	return render(request, "store/registration.html", {"form" : form})

def logout_(request):
	logout(request)
	messages.info(request, "ЦЕ ВИ! Hапевно...")
	return redirect("Store:home")

def login_(request):
	if request.method =="POST":
		form = AuthenticationForm(request = request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				messages.success(request, f"Привіт {username}")
				return redirect("Store:home")
			else:
				messages.info(request, f"""Що це таке {username} ?, або неправильний пароль)""")
		else:
			messages.error(request, f"""Неправильне ім'я або пароль""")
	form = AuthenticationForm
	return render(request, "store/login.html", {"form" : form})

def Ubisoft(request, number):
	return HttpResponse("""<h1>Lol you are %s</h1>""" % number)