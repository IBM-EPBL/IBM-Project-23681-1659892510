FROM python:3.8

WORKDIR /app
COPY . /app

ENV LISTEN_PORT=5000
EXPOSE 5000

RUN pip install -r requirements.txt

CMD ["python","./app.py"]