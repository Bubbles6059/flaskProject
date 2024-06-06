FROM --platform=linux/amd64 python:3-alpine3.15
LABEL authors="rohansuresh"
RUN mkdir /worker
COPY ./requirements.txt /worker/requirements.txt
WORKDIR /worker
RUN pip install -r requirements.txt
COPY . /worker
ENTRYPOINT celery -A tasks worker --loglevel=info
