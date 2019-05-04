FROM python:3.7.1-slim-stretch

WORKDIR /usr/app/
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT flask run -h 0.0.0.0 -p 5000

#MOUNT_POINTS
VOLUME .:/usr/app/

#EXPOSE PORTS 
EXPOSE 5000:5000
