# fanclubApi
**fanclub is a web chatting app, where you can creater groups send messages and images via websockets with dark and light mode, also have google and facebook registration**

This is the repository for the **backend** application of fanclub. Click [here](https://github.com/GAUTAMSAHARAN/fanclub) to go to the frontend repository.

# Setup instructions:

- Clone this repository to a folder on your device.
- create a new virtual environment 
- Run `pip install -r requirements.txt`.
- To set up the database:
  - Create a database with the name of "discord".
  - Then change database settings in settings.py
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'discord',
            'USER': '<your mysql username>',
            'PASSWORD': '<your mysql password',
            'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
            'PORT': '8000',
        }
    }
    ```
- To set up google and facebook registration
  - `python manage.py createsuperuser` run this command in the terminal, then put username and password.
  - Go to http://127.0.0.1:8000/admin/ if you are running your project at 8000.
  - Login with your superuser credential and then your have to register google and facebook client Id and App Id into 'social applications' table. (for google and facebook client id register on google developer and facebook developer portal)
  
- In the root directory of the project run:
  - `python3 manage.py makemigrations` to create tables in the database
  - `python3 manage.py migrate` to apply the newest database representation to the app
  - `sudo docker run -p 6379:6379 -d redis:5`
  - `python manage.py runserver` to... run the server! your development server is running at http://127.0.0.1:8000/
  
- You are ready to use the app! Bon testing :)
