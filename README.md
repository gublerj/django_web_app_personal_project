
# Overview

- I created this Django web app to teach myself Django and learn about web apps. I am especially interested in this because I want to use web apps to deploy machine learning models.
- This web app is a simple to do list

[Software Demo Video](https://youtu.be/Z9MhUpVsyEc)

# Development Environment

- I am using the Django framework in python
- VScode is my editor
- Im using a vertual environment

# Useful Websites
* [Django for beginners](https://djangoforbeginners.com/pages-app/)
* [Tutorial](https://www.youtube.com/watch?v=ovql0Ui3n_I)
* [button help](https://stackoverflow.com/questions/7594348/i-want-a-button-on-my-website-that-will-execute-a-python-script)


# Future Work
* Create a webapp with a machine learning model deployed in it.
* Add user validation
* Combine work from first web app iteration


#### Commands to set up venv and django (first navigate to the folder you want to work in)
- py -m venv env
- .\env\Scripts\activate
- python -m pip install Django
- py -m django --version
- python manage.py runserver

#### Condensing what I learned about making new pages
- create a .html file under 'templates'
- fill that in with same html
- in options/views.py add a new class with a new tamplate_name
- under options/urls.py, add the new view you want to import (after 'from .views import...'). also add a new path()
- yay! you have a new page!! to access it, run 'python manage.py runserver' and go to http://127.0.0.1:8000/NewPageName

