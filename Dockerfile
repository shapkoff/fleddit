FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

RUN python3 .\manage.py migrate

EXPOSE 80

CMD ["python3", ".\manage.py", "runserver"]
