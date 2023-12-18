FROM python:3.10.6-buster

# Necessary, so Docker doesn't buffer the output and that you can see the output 
ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN python -m pipenv install --system --deploy --ignore-pipfile

COPY . .

RUN ["touch", "db.sqlite3"]
RUN python manage.py migrate

CMD python manage.py runserver 0.0.0.0:8000