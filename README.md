# My personal site

[![angelospanag](https://circleci.com/gh/angelospanag/my-site.svg?style=svg)](https://app.circleci.com/pipelines/github/angelospanag/my-site)

My personal site (under heavy development) currently hosted on: https://www.angelospanag.me

## Description

### What did you use to make this?

I started this blog from scratch using Python 3, Django 3 and Bootstrap with minimal JavaScript for its interface. It
has been an awesome journey so far and I try to improve its looks and functionality from time to time, while updating
its content.

### Why not use a CMS like WordPress or a static site generator like Jekyll, Hugo, Gatsby or ...insert x, y, z Jamstack tool here...?

There is currently a very vibrant ecosystem of tools to generate a blogging site effortlessly and I fully support anyone
who will choose to use one of the above. There has never been an easier time to create your own blog with minimal effort
and with no cost.

I wanted to create this site from scratch, so I can learn by doing, evolve it over time, have complete control over its
content (maybe make some interactive posts in the future) and ...simply because it is fun to try!

Huge thanks to Antonio Melé and Packt publishing for creating an amazing book regarding Django development. If you are
interested in creating a website in Django I highly recommend you to
buy [Django 3 By Example - Third Edition](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952)
. Not affiliated in any way, just a happy customer.

## Prerequisites

* [Python 3.9.*](https://www.python.org/downloads/)
* [poetry](https://python-poetry.org/docs/#installation)
* [PostgreSQL](https://www.postgresql.org/download/)

### Ubuntu (using `apt`)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
```

### MacOS (using `brew`)

```bash
brew install python@3.9 poetry postgres
```

### Windows

Use the above links to download the appropriate executables and install them.

## Installation

### Install dependencies

```bash
poetry install
```

### Activate virtual environment shell

```bash
poetry shell
```

### Environment variables

```dotenv
DEBUG=True
EMAIL_USE_TLS=...
EMAIL_HOST=...
EMAIL_PORT=...
EMAIL_HOST_USER=...
EMAIL_HOST_PASSWORD=...
DB_HOST=...
DB_USER=...
DB_PASSWORD=...
REMOTE_HOST=...
SECRET_KEY=...
```

### Database migrations

Assuming you have a PostgreSQL database installed, and the above environment variables point to it, then you can perform the necessary
migrations with:

```bash
python manage.py migrate 
```

## Running

### Run application using development server

```bash
python manage.py 
```

## Running in production

As with any Django project, you should not use the provided development server but run the project using a production
server like Gunicorn (already included and installed from the defined dependencies).

### Collect all static files

```bash
python manage.py collectstatic
```

### Set environment variables

The `DEBUG` environment variable should be set to `False`:

```dotenv
DEBUG=False
```

### Run application using production server (Gunicorn)

```bash
gunicorn --bind 0.0.0.0:8000 mysite.wsgi
```
