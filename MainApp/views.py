from django.shortcuts import render, HttpResponse

# Create your views here.

def weather(request):
    text = 'погода'
    return HttpResponse(text)


def task1(req):
    text = 'Изучаем django'
    name = 'Аликаев А.И.'
    res = f'''<h1>{text}</h1>
    <strong>Автор</strong>: <i>{name}</i>'''
    return HttpResponse(res)



name1 = 'Иван'
name2 = 'Петрович'
name3 = 'Иванов'
phone = '8-923-600-01-02'
email ='vasya@mail.ru'
def task2(req):
    res = f'''Имя: {name1}
        Отчество: {name2}
        Фамилия: {name3}
        телефон: {phone}
        email: {email}
    '''
    return HttpResponse(res)
    

ITEMS = [
 {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
 {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
 {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
 {"id": 7, "name": "Картофель фри" ,"quantity":0},
 {"id": 8, "name": "Кепка" ,"quantity":124},
]



def item(req, i):    
    for j in ITEMS:
        if j['id'] == i:
            res = f'{j['name']}: {j['quantity']}'
            break
        else:
            res = f'Товар с id={i} не найден'
    back = '<p><a href="http://127.0.0.1:8000/items">назад к списку товаров</a></p>'
    res += back
    return HttpResponse(res)


def items(req):
    res = ''
    i = 1
    for j in ITEMS:
        link = f'<a href="http://127.0.0.1:8000/item/{j['id']}">%s</a>'
        res += link % f'<p>{i}. {j['name']}: {j['quantity']} </p>'        
        i += 1
    return HttpResponse(res)




