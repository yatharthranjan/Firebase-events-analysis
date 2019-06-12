#!/usr/bin/env python3
from dask.distributed import Client, progress

def run_client():
    client = Client('10.131.135.81:8786', n_workers=2, threads_per_worker=2, memory_limit='4GB')
    client

if __name__ == '__main__':
    run_client()
