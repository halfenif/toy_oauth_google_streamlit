FROM python:3.12-slim

RUN mkdir /app

COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 9050

CMD ["streamlit", "run", "app.py", "--server.port","9050"]