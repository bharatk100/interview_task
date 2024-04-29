## versions

- Python: 3.8.x

- MySQL: 8.0.x

- Framework: Django 4.2.x , DjangoRestFramework 3.15.x


## How to Setup Locally

Clone Repository:

- $ ``git clone git clone ``

Setup Environment Variables:

- Copy .env file from project and paste it in root folder of repository.

Database Dump

 - Import the lastest .sql dump present in project

#### Python
Create a virtual environment:

- $ ``python -m venv env``

Activate the environment:

- $ ``  .\env\Scripts\activate``

Install Dependencies:

- (env) $ ``pip install -r requirements.txt``

Run Django Server:

- (env) $ ``python manage.py runserver``