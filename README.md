# InformationAboutCars
# PROJECT DESCRIPTION:
**Technology stack:**
- Python.
- Django.
- Django REST Framework (DRF) for API implementation.
- SQLite database.
- Basic HTML/CSS for minimal page design.

**API:**
- GET /api/cars/ — getting a list of cars.
- GET /api/cars/<id>/ — getting information about a specific car.
- POST /api/cars/ — create a new car.
- PUT /api/cars/<id>/ — updating information about the car.
- DELETE /api/cars/<id>/ — delete a car.
- GET /api/cars/<id>/comments/ — get comments on a car.
- POST /api/cars/<id>/comments/ — adding a new comment to the car.

**Views and html templates (the following pages are implemented):**
1. The main page with the title “Information about cars" (information_about_cars.html ), where it shows the entire list of created cars from users (which can be clicked on to go to the corresponding cars/<id> page) and at the top offers the opportunity to register or authorize.
2. From the main page, click on registration (registration.html ), where it prompts you to enter a username and password with password confirmation, if such a username is busy, it will inform you on the current page “Such a username is busy!".
3. From the main page, click on authorization (authorization.html ), where it prompts you to enter your username and password, if the data is entered incorrectly, it will inform you on the current page “You entered your username or password incorrectly.”
4. Administration page (admin.html ), left as a blank for the implementation of “About the company”, etc.
5. Django administrative dashboard, where all data, users, car models, and comments are available.
6. The User's page (user.html ), which you can log in to after logging in with your username and password. 
7. The User's Page (user.html ), has a form for adding a new car (create_car.html ), a form for editing and deleting a car (edit_car.html ), and their corresponding buttons.
8. The page for creating a car record (create_car.html ), suggests entering the car model with the fields: make of car (make), model of car (model), year of manufacture (year), description of car (description). And the “Create record” button, after which data is written to the database + the date and time of creation of the record (created_at) and a foreign key for the user who created the record (owner).
9. The page for editing the car entry (edit_car.html ), suggests making changes to an existing record with fields that already specify: make, model, year of manufacture, and description of the car. And the “Save changes” button, after which data is written to the database + the date and time of the last update of the record (updated_at).
10. From the main page, click on one of the cars to go to the page (cars.html ) with information about a specific car and comments (cars/<id>), as well as a form for adding comments (comments are available only to registered users). After adding a comment, it shows: login, date, text. The comment model itself with fields contains: the content of the comment (content), the date and time when the comment was created (created_at), the foreign key for the car (car), the foreign key for the user (author).

# WEBSITE VERSION:
Version 1.0 implements all the basic stuff.
Note: it requires some design improvements, adding a photo of the car, links to a video of the car, changing the full name in your personal account, adding a photo in your personal account. Unit testing. Vulnerability check.

# SETUP AND INSTALLATION INSTRUCTIONS:
Install Python software from the official website on your OS (Linux/Windows/macOS) “https://www.python.org /”. 

**Install all necessary pip dependencies from the file requirements.txt.**
pip install -r requirements.txt
Note: First make sure that you have python and pip installed (the latest current versions).

**Create a project in any convenient folder.**
Note: Open a terminal command prompt and run:
django-admin startproject information_about_cars
cd information_about_cars
python manage.py startapp cars

Move all the above folder files to your created project, replace them, and save them.

# INSTRUCTIONS FOR USE:
Note: Execute the following commands in the terminal exclusively where it is located manage.py

**Generate new migrations for changes in the database models.**
python manage.py makemigrations

**Apply migrations to the database.**
python manage.py migrate

**Create a superuser account for the Django admin panel.**
python manage.py createsuperuser

**Start the server.**
Note: On the command line, go to where you have manage located.py and run:
python manage.py runserver

**Addition:**
To combine the old migrations.
python manage.py squashmigrations

To reset the database.
python manage.py reset_db


# RESULT:
You should have a link to the server (at http://127.0.0.1:8000 /). Open it in any browser.
