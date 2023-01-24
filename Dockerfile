FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY entrypoint.sh /code/
RUN pip install -r requirements.txt
COPY ./django_test /code/
RUN cd django_test
RUN python manage.py makemigrations
RUN python manage.py migrate
# COPY . /code/

