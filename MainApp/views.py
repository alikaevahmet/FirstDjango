from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from .models import Item
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    context = {
        'name': 'Аликаев А.И.',
        'email': 'mail@mail.ru'
    }
    return render(request, 'index.html', context)

def about(request):
    author = {
        'name': 'Иван',
        'middleName': 'Петрович',
        'lastName': 'Иванов',
        'phone': '8-923-600-01-02',
        'email': 'vasya@mail.ru',
    }
    return render(request, 'about.html', {'author': author})
    
ITEMS = [
 {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
 {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
 {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
 {"id": 7, "name": "Картофель фри" ,"quantity":0},
 {"id": 8, "name": "Кепка" ,"quantity":124},
]

def getItem(request, itemId: int):
    try:
        item = Item.objects.get(id=itemId)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Item with id={itemId} not found')
    else:
        context = {
            'item': item,
        }
        return render(request, 'itemPage.html', context)

def getItems(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'itemsList.html', context)



