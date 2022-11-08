# leaving-academia-for-tech


This repository contains the jupyter notebook and code that created my blog post [Getting Out of Academia and into Tech Without a Hard Sciences Degree](link.com).

## Installation

This project utilizes the [seripapi](https://github.com/serpapi/google-search-results-python) to query the google career search API. Register a google account to get your secret API create a `SERIPAPI_KEY` env variable in you `.zprofile` or `bash_src`

```
echo SERIPAPI_KEY=[YOUR SECRET API KEY]'" >> ~/.zprofile
source ~/.zprofile
```

Clone this repository and install [poetry](https://python-poetry.org/) on your machine. Then install this repo's Python packages and create a new virtual environment.

```
poetry install
poetry shell
```
