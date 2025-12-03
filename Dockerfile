FROM python:3.11-slim
LABEL authors="elenayanushevskaya"

WORKDIR /app
ENV APP_NAME=DOCKER_DEMO

RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

COPY simple_script.py .

CMD ["python", "simple_script.py"]