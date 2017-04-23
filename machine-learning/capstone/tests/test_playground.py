import pytest

from sqlalchemy import create_engine
import pandas as pd
import json
import time
from multiprocessing import Pool as ThreadPool
from functools import partial


def load_df(sql_statement):
    return pd.read_sql_query(sql=sql_statement, con=conn_str)


with open('db_connection.json') as data_file:
    p = json.load(data_file)

conn_str = "postgresql://" + p["user"] + ":" + p["password"] + \
           "@" + p["netloc"] + ":" + str(p["port"]) + "/" + p["dbname"]
engine = create_engine(conn_str)
user_length = pd.read_sql_query("SELECT COUNT(id) AS count FROM auth_user", con=engine)['count'][0]

run_a = True
run_b = True
run_c = True

if run_c:
    # Load data in multiple threads
    tc = time.time()
    chunk_size = 10000
    offset = 0
    sqls = []
    while True:
        sql = "SELECT * FROM auth_user LIMIT %d OFFSET %d" % (chunk_size, offset)
        sqls.append(sql)
        offset += chunk_size
        if user_length < offset:
            break

    pool = ThreadPool(12)
    results = pool.map(load_df, sqls)
    c = pd.concat(results)
    tcf = time.time()
    pool.close()
    pool.join()

if run_a:
    # Load data in a single thread
    ta = time.time()
    a = pd.read_sql_query("SELECT * FROM auth_user", con=engine)
    taf = time.time()

if run_b:
    # Load data in a single thread, but in chunks
    tb = time.time()
    chunk_size = 10000
    offset = 0
    dfs = []
    while True:
        sql = "SELECT * FROM auth_user LIMIT %d OFFSET %d" % (chunk_size, offset)
        dfs.append(pd.read_sql_query(sql=sql, con=conn_str))
        offset += chunk_size
        if len(dfs[-1]) < chunk_size:
            break
    b = pd.concat(dfs)
    tbf = time.time()


def test_single_vs_multithread():
    print("\nExperiment A done: %d lines in %f seconds" % (a.shape[0], taf - ta))
    print("Experiment B done: %d lines in %f seconds" % (b.shape[0], tbf - tb))
    print("Experiment C done: %d lines in %f seconds" % (c.shape[0], tcf - tc))
    assert (tcf - tc) < (taf - ta)
