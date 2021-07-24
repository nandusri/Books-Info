# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip3 install --upgrade pip 
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

# copy project
COPY . /app

# EXPOSE 8000