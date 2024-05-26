FROM python:3.11

COPY ./ /opt/

WORKDIR /opt/

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
