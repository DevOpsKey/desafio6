FROM python:3

MAINTAINER Cristiano Costa

ENV FLASK_APP=app.py

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

COPY entrypoint.sh /usr/bin/entrypoint.sh

RUN chmod +x /usr/bin/entrypoint.sh

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
