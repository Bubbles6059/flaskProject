FROM --platform=linux/amd64 python:3-alpine3.15
LABEL authors="rohansuresh"
RUN mkdir /flaskProject
WORKDIR /flaskProject
COPY . /flaskProject
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]