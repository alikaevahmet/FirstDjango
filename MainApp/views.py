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
    

items = [
 {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
 {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
 {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
 {"id": 7, "name": "Картофель фри" ,"quantity":0},
 {"id": 8, "name": "Кепка" ,"quantity":124},
]



def item(req, i):
    res = filter(lambda x: x if x['id'] == i else None, items)
    return HttpResponse(res)
    



