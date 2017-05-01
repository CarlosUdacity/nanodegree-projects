import pytest
from .context import flow


def test_load_auth_user():
    # Test loading from Postgres
    assert flow.load_auth_user(load_from_h5=False, store_to_h5=True,
                               log=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_auth_user(load_from_h5=True,
                               store_to_h5=True, log=True).shape[0] > 0


def test_load_payment_app_product():
    # Test loading from Postgres
    assert flow.load_payment_app_product(load_from_h5=False, store_to_h5=True,
                                         log=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_payment_app_product(load_from_h5=True, store_to_h5=True,
                                         log=True).shape[0] > 0


def test_load_payment_app_subscription():
    # Test loading from Postgres
    assert flow.load_payment_app_subscription(load_from_h5=False,
                                              store_to_h5=True,
                                              log=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_payment_app_subscription(load_from_h5=True,
                                              store_to_h5=True,
                                              log=True).shape[0] > 0


def test_load_frontend_brazil_pages():
    # Test loading data from HDF5/Postgres
    assert flow.load_frontend_brazil_pages(log=True).shape[0] > 0


def test_load_frontend_brazil_identifies():
    # Test loading data from HDF5/Postgres
    assert flow.load_frontend_brazil_identifies(log=True).shape[0] > 0


def test_load_frontend_brazil_tracks():
    # Test loading data from HDF5/Postgres
    assert flow.load_frontend_brazil_tracks(log=True).shape[0] > 0


def test_load_brazil_events_signup():
    # Test loading from Postgres
    assert flow.load_brazil_events_signup(load_from_h5=False,
                                          store_to_h5=True,
                                          log=True).shape[0] > 0
    # Test loading from HDF5
    assert flow.load_brazil_events_signup(load_from_h5=True,
                                          store_to_h5=True,
                                          log=True).shape[0] > 0


def test_load_analytics_tables_course_enrollments():
    # Test loading data from HDF5/Postgres
    assert flow.load_analytics_tables_course_enrollments(log=True).shape[0] > 0


def test_load_zendesk_data():
    # Test loading from CSV
    assert flow.load_zendesk_data(log=True).shape[0] > 0
