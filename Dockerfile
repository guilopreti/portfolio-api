FROM python:3.10

ENV PYTHONDONTWEIRTEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

WORKDIR /code

COPY . /code/

RUN python manage.py runserver 0.0.0.0:$PORT