FROM --platform=linux/amd64 python:3-alpine3.15
LABEL authors="rohansuresh"
RUN mkdir /flask_app
WORKDIR /flask_app
COPY . /flask_app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
ENV PYTHONPATH /flask_app
COPY . .
CMD ["python", "flask_app/app.py"]
