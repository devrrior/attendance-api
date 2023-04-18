FROM python:3.7.3-alpine3.9

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache libffi-dev gcc musl-dev mariadb-connector-c-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

# fastAPI on railway
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "$PORT"]