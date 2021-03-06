# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import time
import logging
import os
import sys

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

script_dir = os.path.join(os.path.dirname(__file__), '../')


def load_auth_user(sample=False):
    """Load Brazilian users data

    This function loads Brazilian users data.
    
    Args:
        sample (:obj:`bool`, optional): If `True`, returns only 10% of data

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/ebdb_public_auth_user.csv')
    t = time.time()
    if not sample:
        x = pd.read_csv(abs_file_path)
    else:
        x = pd.read_csv(abs_file_path, nrows=7164)
    logging.info("auth_user loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_payment_app_product():
    """Load Brazilian products data

    This function loads Brazilian products data.
    
    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/ebdb_public_payment_app_'
                                             'product.csv')

    t = time.time()
    x = pd.read_csv(abs_file_path)
    logging.info("payment_app_product loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_payment_app_subscription():
    """Load Brazilian subscription data

    This function loads Brazilian subscription data.
    
    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/ebdb_public_payment_app_'
                                             'historicalsubscription.csv')
    t = time.time()
    x = pd.read_csv(abs_file_path,
                    dtype={
                        'user_id': str
                    }) #low_memory=False)
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
    abs_file_path = os.path.join(script_dir, 'data/analytics_frontend_brazil_'
                                             'pages.csv')
    t = time.time()
    if not sample:
        x = pd.read_csv(abs_file_path,
                        dtype={'context_page_path': str,
                               'context_page_referrer': str,
                               'context_campaign_medium': str,
                               'context_campaign_name': str,
                               'context_campaign_source': str,
                               'context_campaign_expid': str,
                               'context_campaign_content': str,
                               'context_campaign_term': str,
                               'context_campaign_campaingn': str,
                               'context_campaign_utm_campaign': str,
                               'context_campaign_utm_content': str,
                               'context_campaign_utm_medium': str,
                               'context_campaign_utm_term': str,
                               'context_campaign_referrer': str,
                               'context_traits_email': str,
                               'context_traits_first_name': str,
                               'context_traits_last_name': str,
                               'context_campaign_campilaign': str,
                               'context_campaign_aprempaign': str,
                               'context_campaign_cammapaign': str,
                               'context_campaign_sgloource': str,
                               'context_campaign_sjurce': str,
                               'context_campaign_contentutm_medium': str,
                               'context_campaign_xmedium': str,
                               'context_campaign_ca5uu_c3_b9mparign': str,
                               'context_campaign_camparign': str,
                               'context_campaign_mediuuy87ym': str,
                               'context_campaign_20term': str})
    else:
        x = pd.read_csv(abs_file_path, nrows=574799,
                        dtype={'context_page_path': str,
                               'context_page_referrer': str,
                               'context_campaign_medium': str,
                               'context_campaign_name': str,
                               'context_campaign_source': str,
                               'context_campaign_expid': str,
                               'context_campaign_content': str,
                               'context_campaign_term': str,
                               'context_campaign_campaingn': str,
                               'context_campaign_utm_campaign': str,
                               'context_campaign_utm_content': str,
                               'context_campaign_utm_medium': str,
                               'context_campaign_utm_term': str,
                               'context_campaign_referrer': str,
                               'context_traits_email': str,
                               'context_traits_first_name': str,
                               'context_traits_last_name': str,
                               'context_campaign_campilaign': str,
                               'context_campaign_aprempaign': str,
                               'context_campaign_cammapaign': str,
                               'context_campaign_sgloource': str,
                               'context_campaign_sjurce': str,
                               'context_campaign_contentutm_medium': str,
                               'context_campaign_xmedium': str,
                               'context_campaign_ca5uu_c3_b9mparign': str,
                               'context_campaign_camparign': str,
                               'context_campaign_mediuuy87ym': str,
                               'context_campaign_20term': str})
    logging.info("frontend_brazil_pages loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_frontend_brazil_identifies(sample=False):
    """DEPRECATED - Load data from all Brazilian anonymous visitors

    This function loads data from all Brazilian anonymous visitors.
    THIS FUNCTION IS DEPRECATED AS IT DOES NOT CONTAIN ALL DATA.
    DO NOT USE THIS FUNCTION
    
    Args:
        sample (:obj:`bool`, optional): If `True`, returns only 10% of data

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/analytics_frontend_brazil'
                                             '_identifies.csv')
    t = time.time()
    if not sample:
        x = pd.read_csv(abs_file_path, low_memory=False)
    else:
        x = pd.read_csv(abs_file_path, nrows=14136, low_memory=False)
    logging.info("frontend_brazil_identifies loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_frontend_brazil_tracks(sample=False):
    """Load all data from Segment

    This function loads all data from Segment.
    
    Args:
        sample (:obj:`bool`, optional): If `True`, returns only 10% of data

    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/analytics_frontend_brazi'
                                             'l_tracks.csv')
    t = time.time()
    if not sample:
        x = pd.read_csv(abs_file_path, low_memory=False)
    else:
        x = pd.read_csv(abs_file_path, nrows=134322, low_memory=False)
    logging.info("frontend_brazil_tracks loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_brazil_events_signup():
    """Load data from all Brazilian webinars

    This function loads data from all Brazilian webinars.
    
    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/analytics_brazil_events_'
                                             'event_sign_up.csv')
    t = time.time()
    x = pd.read_csv(abs_file_path, low_memory=False)
    logging.info("brazil_events_event_sign_up loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_analytics_tables_course_enrollments():
    """Load data from all Brazilian free course enrollments

    This function loads data from all Brazilian free course enrollments.
    
    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/analytics_analytics_tables_'
                                             'course_enrollments_br.csv')
    t = time.time()
    x = pd.read_csv(abs_file_path)
    logging.info("course_enrollments_br loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


def load_zendesk_data():
    """Load data from Zendesk

    This function loads data from Zendesk.
    
    Returns:
        pandas.core.frame.DataFrame: Dataframe containing all data

    """
    abs_file_path = os.path.join(script_dir, 'data/zendesk_export.csv')
    t = time.time()
    x = pd.read_csv(abs_file_path)
    logging.info("zendesk_export loaded: %d lines in %f "
                 "seconds" % (x.shape[0], time.time() - t))
    return x


logging.getLogger().setLevel(logging.DEBUG)

auth_user = load_auth_user(sample=False)
frontend_brazil_pages = load_frontend_brazil_pages(sample=False)\
    .replace(np.nan, '', regex=True)
brazil_events_signup = load_brazil_events_signup()
table_course_enrollments = load_analytics_tables_course_enrollments()
table_payment_app_subscription = load_payment_app_subscription()
