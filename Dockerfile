FROM python:3.12-slim

WORKDIR /code

ENV PYTHONUNBUFFERED=1

COPY pyproject.toml /code/
COPY poetry.lock /code/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]