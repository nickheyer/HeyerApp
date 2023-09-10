FROM python:3.10-alpine

RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev libjpeg-turbo-dev zlib-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./HeyerAppDjango /app
WORKDIR /app

# Create the staticfiles directory
RUN mkdir -p /app/staticfiles && chmod -R 755 /app/staticfiles

COPY ./entry.sh /
ENTRYPOINT [ "sh", "/entry.sh" ]