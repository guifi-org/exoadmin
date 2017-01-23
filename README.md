# Status

Warning this django admin web application is under heavy development.

At the moment app migrations will not be uploaded: I destroy them regularly. Heavy changes on data model can happen, which would be lot of pain if you use this application in production. At your own risk.

# Installation

Assuming Debian 8 Jessie
```
apt-get install --no-install-recommends python3-pip graphviz
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
python3 manage.py runserver
```

if you want to preserve new data, I recommend:

```
python3 manage.py dumpdata --exclude=contenttypes --exclude=auth --exclude=sessions --exclude=admin --indent 4 --natural-foreign --natural-primary > new_fixture.json
```

regenerate data model diagram:

```
python3 manage.py graph_models -a -g -o data_model_diagram.png
```

# Known issues and bad practices

- Avoid including ForeignKey fields in `__str__` or `__unicode__` methods for other Models. src http://www.joshuakehn.com/2014/8/28/djangos-admin-in-production.html -> Related Lookups
- The django admin default theme is not responsive. I could not found a proper theme for django in its latest version `1.10.5`.
