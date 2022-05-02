FROM python:3.7.10
RUN apt-get update -y
RUN apt-get install wget -y
RUN apt-get install vim -y
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

