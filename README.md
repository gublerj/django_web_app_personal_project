
# Overview

{Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.}

{Provide a description of your app.  Describe how to use the app.}

{Describe your purpose for creating this app.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the app running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Development Environment

{Describe the tools that you used to develop the app}

{Describe the programming language that you used and any libraries.}

# Useful Websites
* [Django for beginners](https://djangoforbeginners.com/pages-app/)
* [Tutorial](https://www.youtube.com/watch?v=ovql0Ui3n_I)
* [button help](https://stackoverflow.com/questions/7594348/i-want-a-button-on-my-website-that-will-execute-a-python-script)


# Future Work

* Combine
* Item 2
* Item 3


- django-admin startproject todo_webapp_project

# Commands to set up venv and django (first navigate to the folder you want to work in)
- py -m venv env
- .\env\Scripts\activate
- python -m pip install Django
- py -m django --version

command to run server
- python manage.py runserver

__condensing what I learned__
To add a new webpage you need...
- create a .html file under 'templates'
- fill that in with sime html
- in options/views.py add a new class with a new tamplate_name
- under options/urls.py, add the new view you want to import (after 'from .views import...'). also add a new path()
- yay! you have a new page!! to access it, run 'python manage.py runserver' and go to http://127.0.0.1:8000/NewPageName

