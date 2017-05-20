# -*- coding: utf-8 -*-
import pandas as pd
import time
import logging
import re
from datetime import datetime
from .ingestion import *
import os


script_dir = os.path.join(os.path.dirname(__file__), '../')


def get_features(email):
    t = time.time()
    result = pd.Series()

    # Retrieve basic account data
    account = auth_user.loc[lambda df: (df['email'] == email) &
                                       (df["is_superuser"] == False),
                            :].iloc[0].squeeze()
    result['email'] = account.email
    result['user_id'] = account.username

    # All data must be until became paying student, if that's the case
    anonymous_ids = frontend_brazil_pages.loc[lambda df: df.user_id == account.
                                              username, :]['anonymous_id']\
        .unique()
    visits = frontend_brazil_pages.loc[lambda df: df['anonymous_id'].isin(
                                       anonymous_ids)]\
        .sort_values('received_at')
    if visits.shape[0] > 0:
        first_visit = visits.iloc[0].squeeze()
    else:
        first_visit = None

    webinar_enrollments = brazil_events_signup.loc[lambda df: df.email == email
                                                   , :]
    course_enrollments = table_course_enrollments.loc[lambda df: df.user_id ==
                                                      account.username, :]

    # Days from 1st visit to signup
    if anonymous_ids.shape[0] == 0:  # No data
        result['days_from_first_visit_to_signup'] = None
    else:
        d0 = datetime.strptime(first_visit.received_at.split(".")[0], '%Y-%m-%d %H:%M:%S')
        d1 = datetime.strptime(account.date_joined.split(".")[0], '%Y-%m-%d %H:%M:%S')
        result['days_from_first_visit_to_signup'] = (d1 - d0).days

    # Referrer from first visit
    if anonymous_ids.shape[0] == 0:  # No data
        result['referrer_from_first_visit'] = None
    else:
        result['referrer_from_first_visit'] = first_visit.context_page_referrer

    # % of visits coming from Mobile vs. Desktop
    if anonymous_ids.shape[0] == 0:  # No data
        result['perc_of_visits_from_mobile'] = None
    else:
        grouped = visits.groupby('context_user_agent')
        counts = grouped.count()['id']
        total = 0
        for index, value in counts.iteritems():
            found = re.search('/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMo'
                              'bile|Opera Mini/', index)
            if found is not None:
                total += value

        result['perc_of_visits_from_mobile'] = total / counts.sum()

    # % of visits coming from Google, Facebook, email, etc

    # Number of webinar enrollments
    result['number_of_webinar_enrollments'] = webinar_enrollments.shape[0]

    # Number of free course enrollments
    result['number_of_free_course_enrollments'] = course_enrollments.shape[0]

    # Number of visits
    result['number_of_visits'] = visits.shape[0]

    # Number of weekday / weekend visits

    # Number of visits in morning / afternoon / night / madrugada

    # Number of visits in key pages
    # - NDOPs
    # - FCOPs
    # - Catalog
    # - Sign-in
    # - 50% back
    # - Checkout
    number_of_ndop_visits = 0
    number_of_catalog_visits = 0
    number_of_fcop_visits = 0
    number_of_signin_visits = 0
    number_of_50_back_visits = 0
    number_of_checkout_visits = 0
    for x in visits['context_page_path']:
        if "--nd" in x:
            number_of_ndop_visits += 1
        if "courses/all" in x:
            number_of_catalog_visits += 1
        if "--ud" in x:
            number_of_fcop_visits += 1
        if "signin" in x:
            number_of_signin_visits += 1
        if "50-back" in x:
            number_of_50_back_visits += 1
        if "checkout" in x:
            number_of_checkout_visits += 1

    result['number_of_ndop_visits'] = number_of_ndop_visits
    result['number_of_catalog_visits'] = number_of_catalog_visits
    result['number_of_fcop_visits'] = number_of_fcop_visits
    result['number_of_signin_visits'] = number_of_signin_visits
    result['number_of_50_back_visits'] = number_of_50_back_visits
    result['number_of_checkout_visits'] = number_of_checkout_visits


    # Number of inquires on Zendesk

    # Average time to solve on Zendesk

    # Email server (is_gmail, is_yahoo, etc, and is_from_company)

    # Gave first / last name

    # Name is in email

    # Is the student a paying student?
    subscriptions = table_payment_app_subscription.loc[lambda df:
                                                       df.user_id == account.
                                                       username, :]
    if subscriptions.shape[0] > 0:
        result['is_paying_student'] = 1
    else:
        result['is_paying_student'] = 0

    logging.info(result)
    logging.info("Time to generate features: %d" % (time.time() - t))
    return result


def create_features(save_to_csv=True, save_to_hdf5=False):
    abs_file_path = os.path.join(script_dir, 'features.csv')
    emails = auth_user['email']

    x = pd.DataFrame(columns=get_features('carlos@udacity.com').index.values)

    for index, email in enumerate(emails):
        # x.append(f.get_features(email), ignore_index=True)
        logging.info("INDEX: %d   -   USER: %s" % (index, email))
        x.loc[index] = get_features(email).values

    if save_to_csv:
        x.to_csv(abs_file_path)

    if save_to_hdf5:
        store = pd.HDFStore('store.h5')
        store['features'] = x

    return x
