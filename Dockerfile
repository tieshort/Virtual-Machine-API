FROM python:3.11-slim

RUN apt-get update
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /virtual-machine-api/backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .

EXPOSE 8080

ENTRYPOINT [ "python", "main.py" ]