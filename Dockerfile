FROM python:3.11

COPY . /

WORKDIR /

RUN pip install -r requirements.txt

CMD uvicorn --host=0.0.0.0 --port 8000 app:app
