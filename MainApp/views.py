from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
# Create your views here.

def weather(request):
    text = 'погода'
    return HttpResponse(text)


def home(request):
    # text = 'Изучаем django'
    # name = 'Аликаев А.И.'
    # res = f'''<h1>{text}</h1>
    # <strong>Автор</strong>: <i>{name}</i>'''
    # return HttpResponse(res)
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
    # for j in ITEMS:
    #     if j['id'] == i:
    #         res = f'{j['name']}: {j['quantity']}'
    #         break
    #     else:
    #         res = f'Товар с id={i} не найден'
    # back = '<p><a href="/items">назад к списку товаров</a></p>'
    # res += back
    # return HttpResponse(request)

    item = next((item for item in ITEMS if item['id'] == itemId), None)
    if item is not None:
        context = {
            'item': item,
        }
        return render(request, 'itemPage.html', context)

    return HttpResponseNotFound(f'Item with id={itemId} not found')


def getItems(request):
    # res = ''
    # i = 1
    # for j in ITEMS:
    #     link = f'<a href="/item/{j['id']}">%s</a>'
    #     res += link % f'<p>{i}. {j['name']}</p>'        
    #     i += 1
    # return HttpResponse(res)

    context = {
        'items': ITEMS
    }
    return render(request, 'itemsList.html', context)



