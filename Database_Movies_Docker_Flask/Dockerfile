FROM python:3.6
RUN apt-get update
RUN apt-get -y install libmariadbclient-dev
WORKDIR /movies
COPY requirements.txt /movies
RUN pip install -r requirements.txt
COPY . /movies
CMD ["python", "-u", "code.py"]