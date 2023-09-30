# srdce

Homey cybernetic platform.

## Development

This is a [Django](https://www.djangoproject.com/) codebase. Check out the
[Django docs](https://docs.djangoproject.com/) for general technical documentation.

### Structure

The Django project is [`srdce`](/srdce). There is one Django app,
[`main`](/main) Django app, with all business logic.

### Dependencies

Using [venv](https://docs.python.org/3/library/venv.html):

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

This project also uses [pip-tools](https://github.com/jazzband/pip-tools) for
dependencies management.

### Environment variables

You need to create a new file named `.envrc` in the root of this project once you cloned it.

`.envrc` should contain the following env variables:
```
SECRET_KEY="thisisthesecretkey"
DATABASE_URL="postgres://srdce@127.0.0.1:5432/srdce"
EMAIL_HOST_USER="smtp_user"
EMAIL_HOST_PASSWORD="smtp_password"
```

When on production use also include:

```
NODEBUG=1
```

### Database

This project uses PostgreSQL. See above on how to configure it using the
`.envrc` file.

After creating your local database, you need to create the schema and apply
the migrations:

```sh
python manage.py migrate
```

### Serve

To run the Django development server:

```sh
python manage.py runserver
```

## Testing

```sh
python manage.py test
```

For coverage, run:

```sh
coverage run --source='.' --omit 'venv/*' manage.py test
coverage report -m
```

## Code linting & formatting

The following tools are used:

* [black](https://github.com/psf/black) for code formatting.
* [isort](https://github.com/pycqa/isort) for imports order consistency.
* [flake8](https://gitlab.com/pycqa/flake8) for code linting.

```sh
make format
make lint
```

## Deployment

Deployment [is configured](uwsgi.ini) using the production-grade
[uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) server.

```sh
uwsgi --ini=uwsgi.ini -H venv/
```

You also need to populate your shell environment:

```sh
export SECRET_KEY="thisisthesecretkey"
export DATABASE_URL="postgres://username:password@localhost:5432/db_name"
export EMAIL_HOST_USER="smtp_user"
export EMAIL_HOST_PASSWORD="smtp_password"
```

## Management

In addition to the standard Django management commands, there is also:

```sh
python manage.py reset_dev_database
```

Which fills some sample data for a development database.

## License

This software is licensed under the MIT license.
For more information, read the [LICENSE](LICENSE) file.
