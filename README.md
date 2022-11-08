#Scheduler calendar reservation project server
## REST API
This project is completed by using Python, Django & Django REST framework.
### Description:
This project a server part of complete application that allows users to reserve a 
timescale in calendar by providing some information. Also, it provides an administration interface to check all reservations made.  
### For use:
- Download or clone de project.
- Create and activate virtual environment with command `python3 -m venv venv`.
- Download dependencies with command: `pip install -r requirements.txt`
- Activate virtual environment with command `source venv/bin/activate` on linux or `cd venv/Scripts` and `activate` on Windows.
- Run the server with command `manage.py runserver` or `python manage.py runserver`

### Database using:
- Make some migrations with commands `manage.py makemigrations` and `manage.py makemigrations`
- Run the server with: `manage.py runserver`.

### Make requests:
- Use Postman or others tools in url: `127.0.0.1:8000/client_reserv/reservation/` with adapted HTTP method GET/POST.
- Data Model: ```{"Name":"Alice",
                "Email":"alice@gmail.com", 
                "TimeSlot":"2015-03-25T12:00:00-06:30Z"
                ```
  
### Administration:
- create superuser with command: `manage.py createsuperuser`
- Open web browser on: `127.0.0.1:8000/admin`
- Add username and password provided in creation.

### Units tests
- Run the tests by setting : `export DJANGO_SETTINGS_MODULE=reserv.settings` on Linux or `set DJANGO_SETTINGS_MODULE=reserv.settings` on Windows.
- Run command `python -m unittest`
  



  