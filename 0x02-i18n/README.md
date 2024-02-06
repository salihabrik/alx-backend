# Flask i18n Project



## Overview
This project focuses on internationalization (i18n) and localization in a Flask web application. The goal is to create a basic Flask app that can display content in different languages based on user preferences and URL parameters.

# Tasks

# Task 0: Basic Flask app
Set up a basic Flask app with a single route ("/") and an index.html template.
Display "Welcome to Holberton" as the page title and "Hello world" as the header.
# Task 1: Basic Babel setup
Install the Babel Flask extension (flask_babel version 2.0.0).
Instantiate the Babel object in the app and create a Config class with language settings.
# Task 2: Get locale from request
Create a get_locale function using the babel.localeselector decorator.
Use request.accept_languages to determine the best-matching language.
# Task 3: Parametrize templates
Use the _ or gettext function to parametrize templates with message IDs.
Set up translation files using pybabel for English and French.
# Task 4: Force locale with URL parameter
Implement a way to force a particular locale by passing the locale=fr parameter in the app's URLs.
# Task 5: Mock logging in
Create a user table to mock a database.
Implement a login system using a login_as URL parameter.
Display a welcome message or a default message in the HTML template based on login status.
# Task 6: Use user locale
Change the get_locale function to prioritize a user's preferred locale.
Test by logging in as different users.
# Task 7: Infer appropriate time zone
Define a get_timezone function using the babel.timezoneselector decorator.
Prioritize time zone from URL parameters, user settings, and request headers.
Validate the time zone using pytz.timezone and handle exceptions.
Usage
Clone the repository:

```
git clone https://github.com/your-username/alx-backend.git
cd alx-backend/0x02-i18n
```
Install dependencies:


``````
pip3 install -r requirements.txt
`````
Run the Flask app:


``````
python3 0-app.py
``````
Access the app in your browser at` http://127.0.0.1:5000/`

License
Copyright © 2024 SALIHA BRIK || ALX. All rights reserved.
