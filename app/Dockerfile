FROM python:3 as production_image

ENV SERVER_IP="0.0.0.0"
ENV SERVER_PORT="8080"

EXPOSE 8080

WORKDIR /usr/src/sample-app

COPY ./sample-app/ ./
COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy --ignore-pipfile

ENTRYPOINT ["gunicorn", "server:app"]