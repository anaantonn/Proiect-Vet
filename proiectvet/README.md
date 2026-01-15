# Proiect-Vet

## Getting started

1. Clone the repo and enter the directory

    ```bash
        git clone https://github.com/anaantonn/Proiect-Vet.git
        cd Proiect-Vet/proiectvet
    ```

2. Copy and fill in the `.env.example` file

    ```bash
    cp .env.sample .env
    ```

    Make sure to fill in the variables!

3. Build and start the containers

    ```bash
    docker compose up --build -d
    ```

4. Run migrations

    ```bash
    docker compose exec app python manage.py makemigrations
    docker compose exec app python manage.py migrate
    ```

5. Create an `admin` user for the django admin page:

    ```bash
    docker compose exec app python manage.py createsuperuser
    ```

6. Access the application

    ```bash
    Development server: http://localhost:8000/
    Admin panel: http://localhost:8000/admin/
    ```

### Using POSTMAN

To make sure everything works smoothly if you are using POSTMAN, whenever you are making a request there should be a trailing forward slash at the end, like so: `http://localhost:8000/rasa/`.\
 If you are making `PUT` or `POST` requests, make sure to insert the data in the _body_ section of POSTMAN.
