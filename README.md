

## Tech Stack
1. Python 
2. Django 
3. Django REST Framework 
4. React JS


## Django 

`cd backend`

#### (for installation - pip install virtualenv)
`/django $ virtualenv venv`

#### activate venv
`/django $ source venv/bin/activate`

#### deactivate venv
`/django $ deactivate`

#### Install Django & required packages
`sh
(venv) $ pip install -r requirements.txt
`



#### Migrate models & create superuser 
`sh
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
`

#### Run  server in port 8002
`sh
(venv) $ python manage.py runserver 8002
`
#### For admin access use below url in browser
`sh
http://127.0.0.1:8002/admin/  (or)  http://yourip:8002/admin  
`

#### React JS

In the project directory, you can run:

### `cd frontend`

### `cd todo`

### `npm start`