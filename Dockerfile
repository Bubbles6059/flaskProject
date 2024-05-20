FROM python:3-alpine3.15
LABEL authors="rohansuresh"
WORKDIR /flaskProject
ADD . /flaskProject
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]