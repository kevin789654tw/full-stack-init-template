FROM python:3.10-slim

WORKDIR /app

RUN pip install --upgrade pip && pip install poetry

COPY pyproject.toml ./
RUN poetry install --no-root

COPY . .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
