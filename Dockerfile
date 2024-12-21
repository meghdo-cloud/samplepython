FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ .

# Use Gunicorn instead of Flask development server
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:app"]