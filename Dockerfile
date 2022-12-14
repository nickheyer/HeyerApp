FROM python:3.10-alpine

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./HeyerAppDjango /app 
WORKDIR /app

COPY ./entry.sh /
ENTRYPOINT [ "sh", "/entry.sh" ]