# inicializar django
cd /sistema_ventas
pip install django-humanize
pip install django-weasyprint
pip install WeasyPrint
#python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
superuser admin:administrador1.