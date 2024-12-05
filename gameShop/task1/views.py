from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def menu(request):
    return render(request, 'menu.html')


def home(request):
    return render(request, 'home.html')


def game(request):
    title = "Games"
    name = "Игры"
    button = "Купить"
    games = Game.objects.all()
    context = {
        'title': title,
        'name': name,
        'button': button,
        'games': games,
    }
    return render(request, 'game.html', context)


def cart(request):
    return render(request, 'cart.html')


def sign_up_by_html(request):
    buyers = Buyer.objects.all()
    info = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if Buyer.objects.filter(name=username).exists():
            info["error"] = "Пользователь уже существует!"
        elif password != repeat_password:
            info["error"] = "Пароли не совпадают!"
        elif age < "18":
            info["error"] = "Вы должны быть старше 18!"
        else:
            Buyer.objects.create(name=username, balance=1000.0, age=age)
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, "registration.html", info)
