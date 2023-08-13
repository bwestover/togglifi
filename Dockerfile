FROM python:3.11-slim

ADD ./src /wifi-toggle

RUN pip install -r /wifi-toggle/requirements.txt

WORKDIR /wifi-toggle

CMD ["./docker-entrypoint.sh"]
