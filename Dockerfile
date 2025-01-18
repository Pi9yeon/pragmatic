FROM python:3.12.6

WORKDIR /home/

RUN git clone https://github.com/Pi9yeon/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-#t+()g^2j!9&u79gf17owc%_bsqwhq&xy$u9m-jm7-&%f#agm#" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]