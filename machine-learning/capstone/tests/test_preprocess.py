import logging
import pandas as pd
import numpy as np
from pandas.util.testing import assert_frame_equal
import random
from .context import flow

logging.getLogger().setLevel(logging.DEBUG)


def test_feature_engineering():
    x = flow.get_features('carlos@udacity.com')

    assert isinstance(x, pd.Series)
    assert x.size > 0
    assert 'days_from_first_visit_to_signup' in x.index.values
    assert 'referrer_from_first_visit' in x.index.values
    assert 'perc_of_visits_from_organic' in x.index.values
    assert 'perc_of_visits_from_email' in x.index.values
    assert 'perc_of_visits_from_google' in x.index.values
    assert 'perc_of_visits_from_facebook' in x.index.values
    assert 'perc_of_visits_from_others' in x.index.values
    assert 'perc_of_visits_from_mobile' in x.index.values
    assert 'number_of_webinar_enrollments' in x.index.values
    assert 'number_of_free_course_enrollments' in x.index.values
    assert 'number_of_visits' in x.index.values
    assert 'number_of_weekday_visits' in x.index.values
    assert 'number_of_weekend_visits' in x.index.values
    assert 'number_of_morning_visits' in x.index.values
    assert 'number_of_noon_visits' in x.index.values
    assert 'number_of_afternoon_visits' in x.index.values
    assert 'number_of_nighttime_visits' in x.index.values
    assert 'number_of_midnight_visits' in x.index.values
    assert 'number_of_ndop_visits' in x.index.values
    assert 'number_of_fcop_visits' in x.index.values
    assert 'number_of_signin_visits' in x.index.values
    assert 'number_of_catalog_visits' in x.index.values
    assert 'number_of_50-back_visits' in x.index.values
    assert 'number_of_checkout_visits' in x.index.values
    assert 'number_of_checkout_step_1_visits' in x.index.values
    assert 'number_of_checkout_step_2_visits' in x.index.values
    assert 'number_of_inquires_on_zendesk' in x.index.values
    assert 'average_time_to_ticket_solved' in x.index.values
    assert 'is_email_from_google' in x.index.values
    assert 'is_email_from_yahoo' in x.index.values
    assert 'is_email_from_etc //get main email servers' in x.index.values
    assert 'is_email_from_company' in x.index.values
    assert 'gave_first_name' in x.index.values
    assert 'gave_last_name' in x.index.values
    assert 'levendish_distance_first_name_from_email' in x.index.values
    assert 'levendish_distance_last_name_from_email' in x.index.values
