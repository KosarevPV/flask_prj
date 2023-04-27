FROM python:3.9.1-buster

RUN pip install "poetry==1.4.2"

WORKDIR /app
COPY poetry.lock pyproject.toml /blog/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000
CMD ["python", "wsgi.py"]