# First steps

Create a new ```.env``` file in the main ```proiectvet``` directory.\
*Example:*

```bash

ENGINE=django.db.backends.postgresql
DB_NAME=name
DB_USERNAME=username
DB_PASSWORD=passwd
DB_HOST=hostname
DB_PORT=portnr
DJANGO_SECRET_KEY=yoursecretkey
DJANGO_DEBUG=True
DJANGO_TIMEZONE=yourtimezone

```

## Make migrations and start the server

Make sure you are in the right directory:

```bash
/path-to-your-directory/proiectvet
```

```python
python3 manage.py makemigrations proiectvet
python3 manage.py migrate
python3 manage.py runserver
```
