FROM --platform=linux/x86_64 python:3.10-slim

# Environment variables
ENV PYTHONUNBUFFERED=1

WORKDIR /app/

RUN apt-get update \
    # dependencies for building Python packages && cleaning up unused files
    && apt-get install -y build-essential \
    libcurl4-openssl-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*



# Python dependencies
RUN pip install --upgrade pip pipenv setuptools

COPY Pipfile Pipfile.lock ./
RUN pipenv sync --system --dev

# Copy project stuff
COPY ./ ./
