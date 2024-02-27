FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD uvicorn --app-dir=src main:api --host 0.0.0.0 --port 8000 --proxy-headers