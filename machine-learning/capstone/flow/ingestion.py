# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import pandas as pd
import json
import time

"""Ingestion Module

This module connects with external data sources to ingest data needed to the
capstone project. There are 2 connections: one to the Brazil database, and
other to Global database. Both connect using parameters provided in 
``db_connection.json`` file, at project root folder.

As it takes quite some time to retrieve some tables, after retrieving data this
module saves it in ``store.h5`` file, also at project root folder. Next time it
is used, first it tries to retrieve data from HDF5 file (which is much faster).

Attributes:
    conn_st1 (str): Postgres string URI used to ingest data from Brazil
        database. Sources parameters from ``db_connection.json`` file, located
        in project' root folder.
        
    conn_st2 (str): Postgres string URI used to ingest data from Global
        database. Sources parameters from ``db_connection.json`` file, located
        in project' root folder.
        
    engine_ebdb (sqlalchemy.engine.base.Engine): SQLAlchemy connectable 
        (engine/connection) used to ingest data from Brazil database.
    
    engine_analytics (sqlalchemy.engine.base.Engine): SQLAlchemy connectable 
        (engine/connection) used to ingest data from Global database.
    
    store (pandas.io.pytables.HDFStore): Object that reads and writes pandas 
        using the high performance HDF5 format. Used to improve performance.

Todo:
    * Create a ``load_frontend_brazil_pages`` function, that ingest data in
      chunks from Global database and stores it in HDF5 file. It should be 
      smart to only query if needed, and only do it for the difference.
    * Create ``load_frontend_brazil_identifies``, 
      ``load_frontend_brazil_tracks``, ``load_brazil_events_signup`` and
      ``load_analytics_tables_course_enrollments`` functions reusing logic 
      created in ``load_frontend_brazil_pages``.
    * Finish creating ``load_zendesk_data``, to ingest data from Zendesk
      imported data.
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
   
.. _Google Example:
   http://www.sphinx-doc.org/en/stable/ext/example_google.html

"""

with open('db_connection.json') as data_file:
    p = json.load(data_file)

conn_st1 = "postgresql://" + p["ebdb"]["user"] + ":" + p["ebdb"]["password"] + \
           "@" + p["ebdb"]["netloc"] + ":" + str(p["ebdb"]["port"]) + "/" + \
           p["ebdb"]["dbname"]
engine_ebdb = create_engine(conn_st1)

conn_st2 = "postgresql://" + p["analytics"]["user"] + ":" + p["analytics"][
    "password"] + "@" + p["analytics"]["netloc"] + ":" + str(
    p["analytics"]["port"]) + "/" + p["analytics"]["dbname"]
engine_analytics = create_engine(conn_st2)

store = pd.HDFStore('store.h5')


def load_auth_user(load_from_h5=True, store_to_h5=True, log=False):
    """Load Brazilian users data

    This function tries to load Brazilian users data from ``store.h5`` file. If
    it doesn't find dataframe stored in this file, then it connects with 
    Postgres database, retrieves data and then save it in the file. As this
    table size is small, this function is not optimized to only query missing
    data from HDF5 file: it either retrieves all data from Postgres or none.

    Args:
        load_from_h5 (:obj:`bool`, optional): If `False`, force function to 
            source data from Postgres database.
        store_to_h5 (:obj:`bool`, optional): If `False`, doesn't store data
            into HDF5 file.
        log (:obj:`bool`, optional): If `True`, print how many rows were loaded
            and how many time it was taken.

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all users registered
        in Brazil database

    """
    tc = time.time()
    if load_from_h5:
        if 'auth_user' in store:
            print("\nauth_user loaded from store.h5: %d lines in %f "
                  "seconds" % (store['auth_user'].shape[0], time.time() - tc))
            return store['auth_user']
        else:
            print("\nauth_user not found in store.h5. "
                  "Loading from Postgres...")

    x = pd.read_sql_query("SELECT * FROM auth_user", con=engine_ebdb)
    if log:
        print("\nauth_user loaded from Postgres: %d lines in %f "
              "seconds" % (x.shape[0], time.time() - tc))

    if store_to_h5:
        store['auth_user'] = x

    return x


def load_payment_app_product(load_from_h5=True, store_to_h5=True, log=False):
    """Load Brazilian products data

    This function tries to load Brazilian products data from ``store.h5`` file.
    If it doesn't find dataframe stored in this file, then it connects with 
    Postgres database, retrieves data and then save it in the file. As this
    table size is small, this function is not optimized to only query missing
    data from HDF5 file: it either retrieves all data from Postgres or none.

    Args:
        load_from_h5 (:obj:`bool`, optional): If `False`, force function to 
            source data from Postgres database.
        store_to_h5 (:obj:`bool`, optional): If `False`, doesn't store data
            into HDF5 file.
        log (:obj:`bool`, optional): If `True`, print how many rows were loaded
            and how many time it was taken.

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all users registered
        in Brazil database

    """
    tc = time.time()
    if load_from_h5:
        if 'payment_app_product' in store:
            print("\npayment_app_product loaded from store.h5: %d lines in "
                  "%f seconds" % (store['payment_app_product'].shape[0],
                                  time.time() - tc))
            return store['payment_app_product']
        else:
            print("\npayment_app_product not found in store.h5. "
                  "Loading from Postgres...")

    x = pd.read_sql_query("SELECT * FROM payment_app_product", con=engine_ebdb)
    if log:
        print("\npayment_app_product loaded: %d lines in %f seconds" % (
            x.shape[0], time.time() - tc))
    if store_to_h5:
        store['payment_app_product'] = x
    return x


def load_payment_app_subscription(load_from_h5=True, store_to_h5=True,
                                  log=False):
    """Load Brazilian subscriptions data

    This function tries to load Brazilian subscription data from ``store.h5`` 
    file. If it doesn't find dataframe stored in this file, then it connects 
    with Postgres database, retrieves data and then save it in the file. As 
    this table size is small, this function is not optimized to only query 
    missing data from HDF5 file: it either retrieves all data from Postgres or 
    none.

    Args:
        load_from_h5 (:obj:`bool`, optional): If `False`, force function to 
            source data from Postgres database.
        store_to_h5 (:obj:`bool`, optional): If `False`, doesn't store data
            into HDF5 file.
        log (:obj:`bool`, optional): If `True`, print how many rows were loaded
            and how many time it was taken.

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all users registered
        in Brazil database

    """
    tc = time.time()
    if load_from_h5:
        if 'payment_app_subscription' in store:
            print("\npayment_app_subscription loaded from store.h5: %d lines "
                  "in %f seconds" % (store['payment_app_product'].shape[0],
                                     time.time() - tc))
            return store['payment_app_subscription']
        else:
            print("\npayment_app_subscription not found in store.h5. "
                  "Loading from Postgres...")

    x = pd.read_sql_query("SELECT * FROM payment_app_subscription",
                          con=engine_ebdb)
    if log:
        print("\npayment_app_subscription loaded: %d lines in %f seconds" % (
            x.shape[0], time.time() - tc))

    if store_to_h5:
        store['payment_app_subscription'] = x

    return x


def load_frontend_brazil_pages(log=False, maximum_batch=100000,
                               date_cutoff='2017-03-01'):
    """Load data from all Brazilian website visits

    This function tries to load data from all Brazilian website visits from
    ``store.h5`` file. As this is a very large table, whenever length of
    DataFrame in HDF5 file is different than Postgres, the function will query
    additional data from the Postgres database, to the limit set on the minimum
    batch parameter. Finally, the date cutoff parameter controls the limit
    of data to source.

    Args:
        log (:obj:`bool`, optional): If `True`, print how many rows were loaded
            and how many time it was taken.
        maximum_batch(:obj:`int`, optional): This parameter limits the data 
            queried from Postgres database, to address performance.
        date_cutoff(:obj:`str`, optional): This parameter determines date limit
            to query from Postgres database.

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing data from all 
        Brazilian website visits

    """

    return pd.DataFrame()


def load_frontend_brazil_identifies_user_data(log=False, maximum_batch=100000,
                                              date_cutoff='2017-03-01'):
    return pd.DataFrame()


def load_frontend_brazil_tracks(log=False, maximum_batch=100000,
                                date_cutoff='2017-03-01'):
    return pd.DataFrame()


def load_brazil_events_signup(load_from_h5=True, store_to_h5=True, log=False):
    return pd.DataFrame()


def load_analytics_tables_course_enrollments(log=False, maximum_batch=100000,
                                             date_cutoff='2017-03-01'):
    return pd.DataFrame()


def load_zendesk_data(log=False):
    return pd.DataFrame()
