FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt 

EXPOSE 80

CMD ["sh", "-c", "python3 manage.py collectstatic --noinput && python3 manage.py migrate && gunicorn fleddit.wsgi:application --bind 0.0.0.0:80"]