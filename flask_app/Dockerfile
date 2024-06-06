FROM --platform=linux/amd64 python:3-alpine3.15
LABEL authors="rohansuresh"
RUN mkdir /flask_app
COPY ./requirements.txt /flask_app/requirements.txt
WORKDIR /flask_app
RUN pip install -r requirements.txt
COPY . /flask_app
EXPOSE 5000
CMD ["python", "app.py"]
