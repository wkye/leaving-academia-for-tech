# leaving-academia-for-tech


This repository contains the jupyter notebook and code that created my blog post [Getting Out of Academia and into Tech Without a Hard Sciences Degree](link.com).

## Installation

This project utilizes the [seripapi](https://github.com/serpapi/google-search-results-python) to query the google career search API. Register a google account to get your secret API then create a config.yaml file and set a variable for your secret api key.

```
echo "api_key: '[YOUR SECRET API KEY]'" >> config.yaml
```

Clone this repository and install [poetry](https://python-poetry.org/) on your machine. Then install this repo's Python packages and create a new virtual environment.

```
poetry install
poetry shell
```
