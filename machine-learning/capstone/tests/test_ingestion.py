import pytest
from .context import flow


def test_load_auth_user():
    assert flow.load_auth_user(log=True).shape[0] > 0


def test_load_payment_app_product():
    assert flow.load_payment_app_product(log=True).shape[0] > 0


def test_load_payment_app_subscription():
    assert flow.load_payment_app_subscription(log=True).shape[0] > 0


def test_load_frontend_brazil_pages():
    assert flow.load_frontend_brazil_pages(log=True).shape[0] > 0


def test_load_frontend_brazil_identifies():
    assert flow.load_frontend_brazil_identifies(log=True).shape[0] > 0


def test_load_frontend_brazil_tracks():
    assert flow.load_frontend_brazil_tracks(log=True).shape[0] > 0


def test_load_brazil_events_signup():
    assert flow.load_brazil_events_signup(log=True).shape[0] > 0


def test_load_analytics_tables_course_enrollments():
    assert flow.load_analytics_tables_course_enrollments(log=True).shape[0] > 0


def test_load_zendesk_data():
    assert flow.load_zendesk_data(log=True).shape[0] > 0
