#!/usr/bin/env python3

import dask.dataframe as df
import dask_client as dc

def read_json_as_dataframe(path):
    return df.read_json(path, blocksize=2**28)


dc.run_client()
json_data = read_json_as_dataframe('data/json/bq-results-20190611.json')

json_data
