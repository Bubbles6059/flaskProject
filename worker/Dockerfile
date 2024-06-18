FROM --platform=linux/amd64 python:3-alpine3.15
LABEL authors="rohansuresh"
RUN mkdir /worker
WORKDIR /worker
COPY . /worker
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 6379
COPY . .
ENTRYPOINT celery -A worker.tasks worker --loglevel=info
