FirstDjango

# Инструкция по развертыванию

python3 -m venv venv_name

source django_venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver

deactivate

### Запуск antares.AppImage
./Antares-0.7.34-linux_x86_64.AppImage --no-sandbox


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