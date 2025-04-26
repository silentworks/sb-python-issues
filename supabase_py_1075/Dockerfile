FROM python:3.11.9-bookworm AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen


FROM python:3.11.9-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV VIRTUAL_ENV=/app/.venv

# WORKDIR /app

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}
COPY . /app

ARG SUPABASE_URL
ARG SUPABASE_KEY
ENV SUPABASE_URL=$SUPABASE_URL
ENV SUPABASE_KEY=$SUPABASE_KEY

CMD ["uv", "run", "uvicorn", "app.main:app", "--workers", "2", "--host", "::", "--port", "8080"]
