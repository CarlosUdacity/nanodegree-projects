from sqlalchemy import create_engine
import pandas as pd
import json
import time
import numpy as np
from multiprocessing import Pool as ThreadPool
import logging
import flow as f

logging.getLogger().setLevel(logging.DEBUG)

ta = time.time()
df = pd.read_csv('data/pages.csv', nrows=500000)
print("data/pages.csv loaded in %f time" % (time.time() - ta))

print(df.head())

print(df.shape)

