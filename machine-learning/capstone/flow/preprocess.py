# -*- coding: utf-8 -*-
import pandas as pd
import time
import logging
from datetime import datetime
from .ingestion import *


def get_features(email):
    result = pd.Series()

    # Retrieve basic account data
    account = auth_user.loc[lambda df: (df.email == email) &
                                       (df["is_superuser"] == False),
                            :].squeeze()
    logging.info(account)
    result['email'] = account.email
    result['user_id'] = account.username

    # All data must be until became paying student, if that's the case
    anonymous_ids = frontend_brazil_pages.loc[lambda df: df.user_id == account.
                                              username, :]['anonymous_id']\
        .unique()
    visits = frontend_brazil_pages.loc[lambda df: df['anonymous_id'].isin(
                                       anonymous_ids)]\
        .sort_values('received_at')
    first_visit = visits.iloc[0].squeeze()
    logging.info(first_visit)

    # Days from 1st visit to signup
    if anonymous_ids.shape[0] == 0:  # No data
        result['days_from_first_visit_to_signup'] = None
    else:
        d0 = datetime.strptime(first_visit.received_at, '%Y-%m-%d %H:%M:%S.%f')
        d1 = datetime.strptime(account.date_joined, '%Y-%m-%d %H:%M:%S.%f')
        result['days_from_first_visit_to_signup'] = (d1 - d0).days

    # Referrer from first visit
    if anonymous_ids.shape[0] == 0:  # No data
        result['referrer_from_first_visit'] = None
    else:
        x = first_visit.context_page_referrer
        logging.info(type(x))
        result['referrer_from_first_visit'] = first_visit.context_page_referrer

    # % of visits coming from Google, Facebook, email, etc

    # % of visits coming from Mobile vs. Desktop

    # Number of webinar enrollments

    # Number of free course enrollments

    # Number of visits

    # Number of weekday / weekend visits

    # Number of visits in morning / afternoon / night / madrugada

    # Number of visits in key pages
    # - NDOPs
    # - FCOPs
    # - Sign-in
    # - Catalog
    # - 50% back
    # - Checkout

    # Number of inquires on Zendesk

    # Average time to solve on Zendesk

    # Email server (is_gmail, is_yahoo, etc, and is_from_company)

    # Gave first / last name

    # Name is in email

    return result
