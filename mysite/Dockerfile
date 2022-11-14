FROM python:3.11-rc-bullseye



ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY mysite/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations mysite/mysite
RUN python3 manage.py migrate mysite
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
