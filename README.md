# eRecipe
A Recipe API

This is repo for the eRecipe content.

Table of Content
Technologies
How to setup locally
Testing Account
How to run tests
The ER Diagram
Technologies
Python
Django Rest Framework
JSON WebToken
OpenAPI (SwaggerAPI)
Model Baker
How to setup locally
Create a new virtual environment for this project. Virtualenv and anaconda are popular choices. Please make sure to create a new environment for this project.

Install dependencies:

Copy example.env to .env file and substitute values:

cp example.env .env
 SECRET_KEY = "YOUR_SECRET_KEY"
 DEBUG= YOUR_DEBUG_BOOLEAN
Install dependencies by running the following command in your terminal:

pip install -r requirements.txt
Setup database migrations:

python manage.py migrate

6. To visit the API endpoints in your browser at port <http://localhost:8000>, start eRecipe (Python) server:

 ```bash
 python manage.py runserver
OPTIONAL: Create a super admin account

python manage.py createsuperuser
Visit /admin/ and login with credentials to have access to the admin dashboard.

That's all! For the API Documentation, visit:

SwaggerAPI: http://localhost:8000/
ReDoc: http://localhost:8000/redoc/
Testing Account
Admin:
email: admin@gmail.com
password: admin
How to run tests
Run the following command in your terminal:

pytest
The command runs the tests folder in edata. See how many tests passed.

The ER Diagram
The Entity-Relation Diagram of this project.

<iframe src="https://dbdiagram.io/d/623c470cbed6183873ef3227" allowfullscreen="true" frameborder="0"> </iframe>
You can also visit the ER diagram at: https://dbdiagram.io/d/623c470cbed6183873ef3227

