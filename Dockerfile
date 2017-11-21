FROM ubuntu:16.04
MAINTAINER marquirj

RUN apt-get update
RUN apt-get install -y python-setuptools
RUN apt-get install -y python-dev
RUN apt-get install -y build-essential
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade
RUN apt-get install net-tools

RUN apt-get install -y git
RUN git clone https://github.com/marquirj/ProyectoSkull.git
RUN pip install -r ProyectoSkull/requirements.txt
EXPOSE 8000
CMD  cd bot && python app.py
