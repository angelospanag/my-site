FROM python:3.9.1

WORKDIR /mysite

COPY pyproject.toml poetry.lock /mysite/
RUN pip3 install poetry && poetry config virtualenvs.create false && poetry install --no-dev
COPY docker-entrypoint.sh .env blog mysite static manage.py poetry.lock pyproject.toml /mysite/
RUN chmod +x docker-entrypoint.sh
