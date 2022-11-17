# leaving-academia-for-tech


This repository contains the jupyter notebook and code that created my blog post [Getting Out of Academia and into Tech Without a Hard Sciences Degree](link.com).

## Installation

This project utilizes the [serpapi](https://github.com/serpapi/google-search-results-python) to query the google career search API. Register a google account to get your secret API key. Store secret key in `zshrc` as `SERP_API_KEY=<your secret key>`
```
# run in bash you create env variable for your serp api key
echo "export SERP_API_KEY=<your secret key>"

# clone repo and install dependencies of the repo
git clone git@github.com:wkye/leaving-academia-for-tech.git
poetry install
```

I wrote a wrapper on top of the [serp api python package](https://github.com/serpapi/google-search-results-python) to query and clean the json data comes from the package.

```
from src.resources import resource

# Right now, package only supports querying google
google_jobs = resource(resource_id = 'google'
                       # ,serp_api_key = <your secret key> # if you don't want to use secret variable to use key, you can enter here. Will default to environment variable in zshrc
                       # , engine = <engine you want to search> # engine you want to search. Will default to google_jobs
                       )
# returns data in a pandas dataframe form
df = google_jobs.query(q = 'data scientist', # Search term you want to query
                       n_search = 100 # Number of searches you want returned
                       # ,location = 'New York, New York', # location you'd like to query (optional)
                       # ,start = 0 # pagination
                  )              
```
