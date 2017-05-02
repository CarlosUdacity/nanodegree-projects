import pytest
import logging
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
import random
from .context import flow

logging.getLogger().setLevel(logging.DEBUG)


def test_load_auth_user():
    # Test loading from Postgres
    assert flow.load_auth_user(load_from_h5=False,
                               store_to_h5=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_auth_user(load_from_h5=True,
                               store_to_h5=True).shape[0] > 0


def test_load_payment_app_product():
    # Test loading from Postgres
    assert flow.load_payment_app_product(load_from_h5=False,
                                         store_to_h5=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_payment_app_product(load_from_h5=True,
                                         store_to_h5=True).shape[0] > 0


def test_load_payment_app_subscription():
    # Test loading from Postgres
    assert flow.load_payment_app_subscription(load_from_h5=False,
                                              store_to_h5=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_payment_app_subscription(load_from_h5=True,
                                              store_to_h5=True).shape[0] > 0


def test_load_frontend_brazil_pages():
    # Test loading data from HDF5/Postgres
    assert flow.load_frontend_brazil_pages().shape[0] > 0

    # Sample data from HDF5 file and compare to Postgres data
    if 'frontend_brazil_pages' in flow.store:
        offset = random.randint(0,
                                flow.store['frontend_brazil_pages'].shape[0])
        limit = random.randint(0, flow.store['frontend_brazil_pages'].shape[0]
                               - offset)
        sample_hdf5 = flow.store['frontend_brazil_pages'][offset:(limit +
                                                                  offset)]
        sample_postgres = pd.read_sql_query(
            "SELECT * FROM frontend_brazil.pages "
            "WHERE received_at <= '%s' "
            "ORDER BY received_at ASC "
            "LIMIT %d OFFSET %d" % ('2017-03-01', limit, offset),
            con=flow.engine_analytics)
        sample_postgres.set_index(np.arange(offset, limit + offset),
                                  inplace=True)

        assert_frame_equal(sample_hdf5, sample_postgres)


def test_load_frontend_brazil_identifies():
    # Test loading data from HDF5/Postgres
    assert flow.load_frontend_brazil_identifies().shape[0] > 0


def test_load_frontend_brazil_tracks():
    # Test loading data from HDF5/Postgres
    assert flow.load_frontend_brazil_tracks().shape[0] > 0


def test_load_brazil_events_signup():
    # Test loading from Postgres
    assert flow.load_brazil_events_signup(load_from_h5=False,
                                          store_to_h5=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_brazil_events_signup(load_from_h5=True,
                                          store_to_h5=True).shape[0] > 0


def test_load_analytics_tables_course_enrollments():
    # Test loading data from HDF5/Postgres
    assert flow.load_analytics_tables_course_enrollments().shape[0] > 0


def test_load_zendesk_data():
    # Test loading from CSV
    assert flow.load_zendesk_data().shape[0] > 0
