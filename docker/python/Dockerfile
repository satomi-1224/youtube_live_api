FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update\
    && apt-get install -y vim\
    && pip install --upgrade pip\
    && pip install --upgrade setuptools\
    && pip install poetry\
    && cd /root\
    && poetry config virtualenvs.in-project true\
    && poetry new app

WORKDIR /root/app