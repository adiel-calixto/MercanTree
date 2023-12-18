# First stage (static files)
FROM python:3.10.6-buster as static

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN python -m pipenv install --system --deploy --ignore-pipfile

COPY . .
RUN python manage.py collectstatic


# Second stage (frontend)
FROM node:16-alpine as frontend

WORKDIR /app

COPY mercantree-fe/package.json mercantree-fe/yarn.lock ./
RUN yarn install

COPY mercantree-fe/ .
RUN yarn build

# Final stage
FROM httpd:2.4

COPY --from=frontend /app/dist /usr/local/apache2/htdocs/
COPY --from=static /app/staticfiles /usr/local/apache2/htdocs/assets/