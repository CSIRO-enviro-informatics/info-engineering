FROM python:3.7

RUN apt-get update && apt-get install -y libpq-dev python3-dev

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/RDFLib/pyLDAPI.git
EXPOSE 3000
CMD python ./app.py
