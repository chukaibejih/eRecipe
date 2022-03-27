# eRecipe
A Recipe API

This is repo for the eRecipe content.

## Table of Content

- [e-Data](#e-data)
  - [Table of Content](#table-of-content)
  - [Technologies](#technologies)
  - [How to setup locally](#how-to-setup-locally)
    - [Testing Account](#testing-account)
  - [How to run tests](#how-to-run-tests)
  - [The ER Diagram](#the-er-diagram)

## Technologies

1. Python
2. Django Rest Framework
3. JSON WebToken
4. OpenAPI (SwaggerAPI)
5. [Model Baker](https://pypi.org/project/model-bakery/)

## How to setup locally

1. Create a new virtual environment for this project. *Virtualenv* and *anaconda* are popular choices. ***Please make sure to create a new environment for this project.***
2. Install dependencies:
3. Copy `example.env` to `.env` file and substitute values:

   ```bash
   cp example.env .env
   ```

   ```env
    SECRET_KEY = "YOUR_SECRET_KEY"
    DEBUG= YOUR_DEBUG_BOOLEAN
   ```

4. Install dependencies by running the following command in your terminal:

  ```bash
  pip install -r requirements.txt
  ```

5. Setup database migrations:

   ```bash
   python manage.py migrate

  ```

6. To visit the API endpoints in your browser at port <http://localhost:8000>, start e-Data (Python) server:

   ```bash
   python manage.py runserver
   ```

7. OPTIONAL: Create a super admin account

   ```bash
   python manage.py createsuperuser
   ```

   Visit `/admin/` and login with credentials to have access to the admin dashboard.

### Testing Account

- Admin:
  - email: admin@gmail.com
  - password: asdf

## How to run tests

Run the following command in your terminal:

```bash
pytest
```

The command runs the `tests` folder in `eRecipe`. See how many tests passed.

## The ER Diagram

The Entity-Relation Diagram of this project.

<figure class="video_container">
  <iframe src="https://dbdiagram.io/embed/623c470cbed6183873ef3227" allowfullscreen="true" frameborder="0"> </iframe>
</figure>

You can also visit the ER diagram at: <https://dbdiagram.io/d/623c470cbed6183873ef3227>
