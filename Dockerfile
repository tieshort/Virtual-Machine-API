FROM python:3.11-slim

# Using Poetry
# RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /virtual-machine-api/backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Using Poetry 
# COPY pyproject.toml poetry.lock ./
# RUN pip install poetry
# RUN poetry config virtualenvs.create false && \
#     poetry install --no-interaction --no-ansi

COPY src/ .
COPY postgres.env .
COPY email.env .

ENTRYPOINT [ "fastapi", "run", "main.py" ]