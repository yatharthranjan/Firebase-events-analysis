#!/usr/bin/env python3
from dask.distributed import Client, progress

def run_client():
    client = Client('10.200.107.9:8786', n_workers=3, threads_per_worker=4, memory_limit='10GB')
    return client

if __name__ == '__main__':
    run_client()
