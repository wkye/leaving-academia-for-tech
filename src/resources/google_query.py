import copy
import inspect
import os
import time

import pandas as pd
from loguru import logger
from serpapi import GoogleSearch
from src.resources.constants import SERP_API_KEY, ENGINE, START

class GoogleResource:
    def __init__(self, **kwargs):
        """
        Create a class to query Google Search
        :param kwargs:
        """
        self.serp_api_key = kwargs['serp_api_key']
        self.engine = kwargs['engine']
        self.start = kwargs['start']

    def to_pandas(self, results: list,results_keys: list) -> pd.DataFrame:
        """

        :param results: List form of job results in dictionaries
        :return: Pandas dataframe of job rsults
        """

        results_dict = {x: [] for x in results_keys}

        for result in results:
            for key in results_keys:
                results_dict[key].append(result[key])

        return pd.DataFrame(results_dict)

    def query(self, q, n_search ,**kwargs) -> pd.DataFrame:
        """
        """

        params = {
            "q": q,
            "engine": self.engine,
            "api_key": self.serp_api_key,
            "start": self.start
        }
        params.update(**kwargs)

        n = 0
        jobs = []
        results_keys = ['title','company_name','location','description']
        while n < n_search:
            tstart = time.time()
            results = GoogleSearch(params).get_dict()

            params["start"] += 10
            n += 10

            if "error" in results:
                tstop = time.time()
                print(results["error"])
                break

            for result in results["jobs_results"]:
                result_na = {key: result[key] if key in result.keys() else '' for key in results_keys}
                jobs.append(
                    {   "title": result_na["title"],
                        "company_name": result_na["company_name"],
                        "location": result_na["location"],
                        "description": result_na["description"]
                    }
                )
            tstop = time.time()
        df = self.to_pandas(jobs, results_keys)
        logger.info(
            f"Query data retrieved in {(tstop - tstart):0.1f} seconds.\n"
            f"Retrieved dataframe with {len(df)} rows, consuming {sum((df.memory_usage()) / 1e6):0.1f} MB."
        )
        return df

default_params = {
    'serp_api_key': SERP_API_KEY,
    'engine': ENGINE,
    'start': START
}

def resource(resource_id: str, **kwargs) -> object:
    """

    Resource utility to query different search engines. e.g. use resource_id = 'google' to query google.
    More resources to be added later.

    :param resource_id: name of search engine you are using. Each string represents a class.
    :param kwargs: default values; my personal serp_api key and google search are set as the defaults
    :return: desired resource type
    """
    if resource_id == 'google':
        resource = GoogleResource
    else:
        raise ValueError(f"{resource_id} has not been implemented yet or does not exist.\n"
            f"Allowable search engines: {list(RESOURCE_CLASSES.keys())}")

    default_params.update(**kwargs)

    return resource(**default_params)

google_jobs = resource('google')
df = google_jobs.query(q = 'data scientist',
                  location = 'New York, New York',
                  n_search = 100)
df.to_pickle('df.pkl')