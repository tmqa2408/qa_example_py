FROM python:3.9.0-alpine

WORKDIR /app

COPY . .

#RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip install selenium==4.4.3

RUN pip3 install -r requirements.txt

CMD ["pytest"]

#FROM python:3.10
#
#WORKDIR /app
#
#COPY requirements.txt ./app
#
#COPY . .
#
#RUN pip install --trusted-host=pypi.org --trusted-host=files.pythonhosted.org jinja2
#RUN pip install -r requirements.txt
#
#RUN apt-get update && apt-get install -y wget unzip && \
#    wget http://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
#    apt-get install -y ./google-chrome-stable_current_amd64.deb &&\
#    rm google-chrome-stable_current_amd64.deb && \
#    apt-get --fix-broken install && \
#    apt-get clean
#
#CMD ["pytest"]