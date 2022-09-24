# getting base image
FROM python:3.10.6

# specifying from which folder we will execute instructions
WORKDIR /usr/src/app

# installing pip dependencies
COPY ./requirements.txt ./
RUN pip3 install -U pip
RUN pip install --no-cache-dir -r requirements.txt

# copying application code
COPY ./app .

# specifying env vars
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=True

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0"]