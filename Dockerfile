FROM python:3.10-alpine
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
CMD python -m flask run --host=0.0.0.0