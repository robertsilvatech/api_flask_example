FROM alpine:3.8

EXPOSE 80

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
COPY run.py /
COPY ./app /app
RUN apk add --no-cache python3 && pip3 install -r /requirements.txt

CMD python3 /run.py