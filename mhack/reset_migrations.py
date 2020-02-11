import os

os.remove("db.sqlite3") 
os.system('find . -path "*/migrations/*.py" -not -name "__init__.py" -delete')
os.system('find . -path "*/migrations/*.pyc"  -delete')
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')
os.system('python manage.py runserver')