# Requirements

```
apt-get install --no-install-recommends python3-pip
pip3 install virtualenv
git clone https://github.com/pedro-nonfree/exoadmin
cd exoadmin
virtualenv env
source env/bin/activate
pip3 install django pyparsing pydot django-extensions
# TODO: add a fake database
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
