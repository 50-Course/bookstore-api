# pull from base image
# Set this image as the dev environment
FROM python:3.10-rc-slim-buster
# Set Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
# set the working dir
WORKDIR /usr/app
# copy requirements
COPY dev-requirements.txt /usr/app/
# install dependecies
RUN python install -r dev-requirements.txt
# Lauch up dev environment
COPY  . .