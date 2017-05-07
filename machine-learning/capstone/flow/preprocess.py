# -*- coding: utf-8 -*-
import pandas as pd
import time
import logging
from .ingestion import *


def get_features(email):
    x = auth_user.loc[lambda df: (df.email == email) & (df["is_superuser"] ==
                                                        False), :].squeeze()

    # All data must be until became paying student, if that's the case

    # Days from 1st visit to signup

    # Referrer from first visit

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



    return x
