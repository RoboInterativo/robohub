FROM python:3.6.8
EXPOSE 5000
ENV HOME=/opt/app
WORKDIR /opt/app

COPY requirements.txt /tmp/requirements.txt
COPY . .
COPY service.sh /opt/service.sh

RUN pip install virtualenv  &&\
    python -m virtualenv /opt/venv &&\
    chown 1001:1001 /opt/ -R

USER 1001

RUN . /opt/venv/bin/activate &&\
    pip install pip --upgrade &&\
    pip install -r  /tmp/requirements.txt &&\
    cd /opt/app/back && ls -li
RUN    chmod +x /opt/service.sh &&  python setup.py install

CMD . /opt/service.sh
