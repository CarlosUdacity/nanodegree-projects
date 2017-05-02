from sqlalchemy import create_engine
import pandas as pd
import json
import time
import numpy as np
from multiprocessing import Pool as ThreadPool
import logging
import flow as f

logging.getLogger().setLevel(logging.DEBUG)

x = f.load_frontend_brazil_pages(recursive=True)

exit(0)

ta = time.time()
x = pd.read_sql_query("SELECT count(id) as count FROM frontend_brazil.pages",
                      con=f.engine_analytics)
print("Pages - Number of rows: %d - time: %3.1f" % (x['count'][0], time.time() - ta))

tb = time.time()
y = pd.read_sql_query("SELECT count(id) as count FROM frontend_brazil.pages "
                      "WHERE received_at <= '2017-03-01'",
                      con=f.engine_analytics)
print("Pages - Number of rows: %d - time: %3.1f" % (y['count'][0], time.time() - tb))

# *****

ta = time.time()
x = pd.read_sql_query("SELECT count(id) as count FROM frontend_brazil.identifies",
                      con=f.engine_analytics)
print("Identifies - Number of rows: %d - time: %3.1f" % (x['count'][0], time.time() - ta))

tb = time.time()
y = pd.read_sql_query("SELECT count(id) as count FROM frontend_brazil.identifies "
                      "WHERE received_at <= '2017-03-01'",
                      con=f.engine_analytics)
print("Identifies - Number of rows: %d - time: %3.1f" % (y['count'][0], time.time() - tb))

# *****

ta = time.time()
x = pd.read_sql_query("SELECT count(id) as count FROM frontend_brazil.tracks",
                      con=f.engine_analytics)
print("Tracks - Number of rows: %d - time: %3.1f" % (x['count'][0], time.time() - ta))

tb = time.time()
y = pd.read_sql_query("SELECT count(id) as count FROM frontend_brazil.tracks "
                      "WHERE received_at <= '2017-03-01'",
                      con=f.engine_analytics)
print("Tracks - Number of rows: %d - time: %3.1f" % (y['count'][0], time.time() - tb))

# *****

ta = time.time()
x = pd.read_sql_query("SELECT count(*) as count FROM analytics_tables.course_enrollments ",
                      con=f.engine_analytics)
print("Course Enrollments - Number of rows: %d - time: %3.1f" % (x['count'][0], time.time() - ta))

tb = time.time()
y = pd.read_sql_query("SELECT count(*) as count FROM analytics_tables.course_enrollments "
                      "WHERE join_time <= '2017-03-01'",
                      con=f.engine_analytics)
print("Course Enrollments - Number of rows: %d - time: %3.1f" % (y['count'][0], time.time() - tb))

# *****

ta = time.time()
x = pd.read_sql_query("SELECT count(id) as count FROM brazil_events.event_sign_up ",
                      con=f.engine_analytics)
print("Events - Number of rows: %d - time: %3.1f" % (x['count'][0], time.time() - ta))

tb = time.time()
y = pd.read_sql_query("SELECT count(id) as count FROM brazil_events.event_sign_up "
                      "WHERE received_at <= '2017-03-01'",
                      con=f.engine_analytics)
print("Events - Number of rows: %d - time: %3.1f" % (y['count'][0], time.time() - tb))


