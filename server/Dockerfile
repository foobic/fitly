FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3.6-dev python3-dev python3 build-essential libpq-dev
RUN pip3 install -U pipenv
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
COPY . code/
WORKDIR /code/server
RUN bash .env  
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE $FLASK_RUN_PORT
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
