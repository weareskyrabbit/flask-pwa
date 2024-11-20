FROM python:3.8

WORKDIR /usr/src

COPY /requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /usr/src/apps