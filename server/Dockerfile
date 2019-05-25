FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
      apt-utils \
      python3-pip \
      python3.6-dev \ 
      python3-dev \
      python3 \
      build-essential \
      libpq-dev
RUN pip3 install -U pipenv

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

COPY . code/

WORKDIR /code/server
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
