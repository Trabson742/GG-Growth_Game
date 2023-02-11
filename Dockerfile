
FROM python:3.8

ADD . ./app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip uninstall jinja2

COPY requirements.txt requirements.txt
RUN pip install -U -r requirements.txt
RUN pip3 install jinja2==3.0.3 --force-reinstall
RUN pip3 install SQLAlchemy==1.3.23 --force-reinstall

RUN pip3 install flask --upgrade

RUN pip list

CMD [ "python", "-m" , "flask", "run"]