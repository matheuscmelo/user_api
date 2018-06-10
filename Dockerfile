FROM python:3

COPY ./api/ /var/app/api/

WORKDIR /var/app/api/

RUN pip install -r requirements.txt
