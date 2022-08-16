 FROM python:3.10
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements/*.txt /code/
 RUN pip install -r development.txt
 ADD src/ /code/
