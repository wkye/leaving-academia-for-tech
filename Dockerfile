From jupyter/scipy-notebook

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

# System deps:
RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /leaving-academia-for-tech
COPY . .

# Project initialization:
RUN POETRY_VIRTUALENVS_CREATE=false && poetry install

# Creating folders, and files for a project:
COPY . /code
