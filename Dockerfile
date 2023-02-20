FROM python:3.10

WORKDIR /code

COPY Pipfile* /code/
RUN pip install -U pipenv
RUN pipenv install --deploy --ignore-pipfile --system

COPY ./src /code/
