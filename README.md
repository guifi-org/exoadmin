# Requirements

```
apt-get install --no-install-recommends python3-pip
pip3 install virtualenv
git clone https://github.com/pedro-nonfree/exoadmin
cd exoadmin
virtualenv env
source env/bin/activate
pip3 install django pyparsing pydot django-extensions
python3 manage.py loaddata fixture_base.json
# add next line if you want to test with fake data
python3 manage.py loaddata fixture_demo.json
python3 manage.py makemigrations
python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" | python manage.py shell
python3 manage.py runserver
```

if you want to preserve new data, I recommend:

`python3 manage.py dumpdata --exclude=contenttypes --exclude=auth --exclude=sessions --exclude=admin --indent 4 --natural-foreign --natural-primary > new_fixture.json`
