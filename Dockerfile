FROM python:3.11

RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip \
    chromium \
    chromium-driver

RUN python3 -m pip install --upgrade pip


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