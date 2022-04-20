# eRecipie

This is repo for the eRecipe content.

## Table of Content

- [eRecipe](#eRecipe)
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

6. To visit the API endpoints in your browser at port <http://localhost:8000>, start eRecipe (Python) server:

   ```bash
   python manage.py runserver
   ```

7. OPTIONAL: Create a super admin account

   ```bash
   python manage.py createsuperuser
   ```

   Visit `/admin/` and login with credentials to have access to the admin dashboard.

That's all! For the API Documentation, visit:

- SwaggerAPI: <http://localhost:8000/>

### Testing Account

- Admin:
  - email: admin@gmail.com
  - password: admin

## How to run tests

Run the following command in your terminal:

```bash
pytest
```

The command runs the `tests` folder in `erecipe`. See how many tests passed.

## The ER Diagram

The Entity-Relation Diagram of this project.

<figure class="video_container">
  <iframe src="https://dbdiagram.io/d/623c470cbed6183873ef3227" allowfullscreen="true" frameborder="0"> </iframe>
</figure>

You can also visit the ER diagram at: <https://dbdiagram.io/d/623c470cbed6183873ef3227>