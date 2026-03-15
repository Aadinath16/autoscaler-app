FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY backend/ backend/
COPY frontend/ frontend/

CMD ["gunicorn", "-b", "0.0.0.0:5000", "backend.app:app"]