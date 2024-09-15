FROM python:3.11-slim

ADD ./src/requirements.txt /wifi-toggle/requirements.txt

RUN pip install -r /wifi-toggle/requirements.txt

ADD ./src /wifi-toggle

WORKDIR /wifi-toggle

CMD ["./docker-entrypoint.sh"]
