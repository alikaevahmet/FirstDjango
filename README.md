FirstDjango

# Инструкция по развертыванию

python3 -m venv venv_name

source django_venv/bin/activate

pip install -r requirements.txt

создание миграции
python3 manage.py makemigrations

применение миграции
python3 manage.py migrate

python3 manage.py runserver

deactivate

### Запуск antares.AppImage
./Antares-0.7.34-linux_x86_64.AppImage --no-sandbox
либо удалить `AppArmor`:
    sudo systemctl disable --now apparmor 
    sudo apt remove --assume-yes --purge apparmor 
    restart OS


# Запуск 'ipython' в контексте приложения django
python  namage.py shell_plus --ipython


# Дополнительно
Полезное дополнение для шаблонов "Django"
'''
ext install batisteo.vscode-django
'''

добавить в 'settings.json'
'''
"emmet.includeLanguages": {
    "django-html": "html",
}
"files.associations": {
    "*.html": "django-html"
}
'''

# Модели
Поля
https://docs.djangoproject.com/en/5.1/ref/models/fields


# DB
Делаем записи в БД
python manage.py shell_plus --ipython

## Создание объекта
item = Item(name="Кроссовки", brand="abibas", count=10)
item.save()

## Получение объектов
items = Item.objects.all()
items = Item.objects.get(id=1)


# Связанные объекты
## Добавить связь
item1 = Item.objects.get(id=1)
item1.colors.add(color1)
## Получить 
item1 = Item.objects.get(id=1)
item1.colors.all()
items = Item.objects.filter(colors__name='green')


# Выгрузка и загрузка данных из БД
## Выгрузить все модели
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items_wcolors.json

## Выгрузить определенные модели
python manage.py dumpdata MainApp.item --indent 4 > ./fixtures/only_items.json
python manage.py dumpdata MainApp.color --indent 4 > ./fixtures/only_colors.json

## Загрузить
python manage.py loaddata ./fixtures/items.json

# очистка бд
python manage.py flush

# Проверка существования цвета
item.colors.exists()