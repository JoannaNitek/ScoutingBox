FROM python:3.6-stretch

RUN apt-get -y update
RUN apt-get install -y python3-pip
ADD requirements.txt ./
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./ ./

# instalacja postgres

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]