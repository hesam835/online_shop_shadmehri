from python:latest

WORKDIR /ONLINE_SHOP_SHADMEHRI
COPY requirements.txt /ONLINE_SHOP_SHADMEHRI/

RUN pip install -U pip
RUN pip install -r /ONLINE_SHOP_SHADMEHRI/requirements.txt

COPY . /ONLINE_SHOP_SHADMEHRI/
EXPOSE 8000
CMD ["gunicorn", "shop.wsgi", ":8000"]

