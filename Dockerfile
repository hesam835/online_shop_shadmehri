FROM python:latest

WORKDIR /code
COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install celery

COPY . /code/
EXPOSE 8000
CMD ["gunicorn", "shop.wsgi", ":8000"]

