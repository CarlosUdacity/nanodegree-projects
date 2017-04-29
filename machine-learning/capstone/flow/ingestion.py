from sqlalchemy import create_engine
import pandas as pd
import json
import time
from multiprocessing import Pool as ThreadPool


def load_df(sql_statement):
    return pd.read_sql_query(sql=sql_statement, con=conn_str)


with open('db_connection.json') as data_file:
    p = json.load(data_file)

conn_str = "postgresql://" + p["user"] + ":" + p["password"] + \
           "@" + p["netloc"] + ":" + str(p["port"]) + "/" + p["dbname"]
engine = create_engine(conn_str)


def load_auth_user(log=False):
    user_length = pd.read_sql_query("SELECT COUNT(id) AS count FROM auth_user", con=engine)['count'][0]

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
    pool.close()
    pool.join()

    if log:
        print("\nauth_user loaded: %d lines in %f seconds" % (c.shape[0], time.time() - tc))

    return c


def load_payment_app_product(log=False):
    x = pd.read_sql_query("SELECT * FROM payment_app_product", con=engine)
    tc = time.time()
    if log:
        print("\npayment_app_product loaded: %d lines in %f seconds" % (
            x.shape[0], time.time() - tc))
    return x


def load_payment_app_subscription(log=False):
    x = pd.read_sql_query("SELECT * FROM payment_app_subscription", con=engine)
    tc = time.time()
    if log:
        print("\npayment_app_subscription loaded: %d lines in %f seconds" % (
            x.shape[0], time.time() - tc))
    return x


def load_frontend_brazil_pages(log=False):
    return pd.DataFrame()


def load_frontend_brazil_identifies(log=False):
    return pd.DataFrame()


def load_frontend_brazil_tracks(log=False):
    return pd.DataFrame()


def load_brazil_events_signup(log=False):
    return pd.DataFrame()


def load_analytics_tables_course_enrollments(log=False):
    return pd.DataFrame()


def load_zendesk_data(log=False):
    return pd.DataFrame()
