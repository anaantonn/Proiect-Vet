# Proiect-Vet

## Getting started

1. Clone the repo and enter the directory

    ```bash
        git clone https://github.com/anaantonn/Proiect-Vet.git
        cd Proiect-Vet
    ```

2. Create a python virtual enviroment
3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Copy and fill in the `.env.example` file

    ```bash
    cp proiectvet/.env.example proiectvet/.env
    ```

5. Make migrations + migrate

    ```bash
    python3 proiectvet/manage.py makemigrations proiectvet
    python3 proiectvet/manage.py migrate
    ```

6. Create an `admin` user for the django admin page:

    ```bash
    python3 proiectvet/manage.py createsuperuser
    ```

7. Start the development server

    ```bash
    python3 manage.py runserver
    ```

### Using POSTMAN

To make sure everything works smoothly if you are using POSTMAN, whenever you are making a request there should be a trailing forward slash at the end, like so: ```http://localhost:8000/rasa/```.\
 If you are making ```PUT``` or ```POST``` requests, make sure to insert the data in the *body* section of POSTMAN.
