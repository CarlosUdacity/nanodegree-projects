# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import pandas as pd
import json
import time
import logging

"""Ingestion Module

This module connects with external data sources to ingest data needed to the
capstone project. There are 2 connections: one to the Brazil database, and
other to Global database. Both connect using parameters provided in 
``db_connection.json`` file, at project root folder.

As it takes quite some time to retrieve some tables, after retrieving data this
module saves it in ``store.h5`` file, also at project root folder. Next time it
is used, first it tries to retrieve data from HDF5 file (which is much faster).

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
   
.. _Google Example:
   http://www.sphinx-doc.org/en/stable/ext/example_google.html

"""


def load_auth_user(sample=False):
    """Load Brazilian users data

    This function loads Brazilian users data.
    
    Args:
        sample (:obj:`bool`, optional): If `True`, returns only 10% of data

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    t = time.time()
    if not sample:
        x = pd.read_csv('data/ebdb_public_auth_user.csv')
    else:
        x = pd.read_csv('data/ebdb_public_auth_user.csv', nrows=7164)
    logging.info("auth_user loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_payment_app_product():
    """Load Brazilian products data

    This function loads Brazilian products data.
    
    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    t = time.time()
    x = pd.read_csv('data/ebdb_public_payment_app_product.csv')
    logging.info("payment_app_product loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_payment_app_subscription():
    """Load Brazilian subscription data

    This function loads Brazilian subscription data.
    
    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    t = time.time()
    x = pd.read_csv('data/ebdb_public_payment_app_historicalsubscription.csv',
                    low_memory=False)
    logging.info("payment_app_historicalsubscription loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_frontend_brazil_pages(sample=False):
    """Load data from all Brazilian website visits

    This function loads data from all Brazilian website visits.
    
    Args:
        sample (:obj:`bool`, optional): If `True`, returns only 10% of data

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    t = time.time()
    if not sample:
        x = pd.read_csv('data/analytics_frontend_brazil_pages.csv',
                        low_memory=False)
    else:
        x = pd.read_csv('data/analytics_frontend_brazil_pages.csv',
                        nrows=574799, low_memory=False)
    logging.info("frontend_brazil_pages loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_frontend_brazil_identifies(sample=False):
    t = time.time()
    if not sample:
        x = pd.read_csv('data/analytics_frontend_brazil_identifies.csv',
                        low_memory=False)
    else:
        x = pd.read_csv('data/analytics_frontend_brazil_identifies.csv',
                        nrows=14136, low_memory=False)
    logging.info("frontend_brazil_identifies loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_frontend_brazil_tracks(sample=False):
    t = time.time()
    if not sample:
        x = pd.read_csv('data/analytics_frontend_brazil_tracks.csv',
                        low_memory=False)
    else:
        x = pd.read_csv('data/analytics_frontend_brazil_tracks.csv',
                        nrows=134322, low_memory=False)
    logging.info("frontend_brazil_tracks loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_brazil_events_signup():
    t = time.time()
    x = pd.read_csv('data/analytics_brazil_events_event_sign_up.csv',
                    low_memory=False)
    logging.info("brazil_events_event_sign_up loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_analytics_tables_course_enrollments():
    t = time.time()
    x = pd.read_csv('data/analytics_analytics_tables_'
                    'course_enrollments_br.csv')
    logging.info("course_enrollments_br loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_zendesk_data(sample=False):
    return pd.DataFrame()
