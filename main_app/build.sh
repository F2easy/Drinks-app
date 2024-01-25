pip install -r requirements.txt
pip install django
python manage.py collectstatic --no-input
python manage.py migrate