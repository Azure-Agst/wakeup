FROM python:3-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt && pip install waitress

RUN mkdir /app/config
COPY wakeup/ wakeup/

CMD ["waitress-serve", "--listen=0.0.0.0:8080", "--call", "wakeup:create_app"]