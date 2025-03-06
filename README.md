# First steps

Clone the repo using ```git clone https://github.com/anaantonn/Proiect-Vet.git```\
Navigate to the newly created directory.\
Create a virtual enviroment using your preferred method.\
Install the necessary packages and dependencies using ```pip install -r requirements.txt```\
Create a new ```.env``` file in the first ```proiectvet``` directory.\
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

### Using POSTMAN

To make sure everything works smoothly if you are using POSTMAN, whenever you are making a request there should be a trailing forward slash at the end, like so: ```http://localhost:8000/rasa/```.\
 If you are making ```PUT``` or ```POST``` requests, make sure to insert the data in the *body* section of POSTMAN.
