from sqlalchemy import create_engine
import pandas as pd
import json
import time
import numpy as np
from multiprocessing import Pool as ThreadPool
import logging
import flow as f
import os


script_dir = os.path.dirname(__file__)
features_file = os.path.join(script_dir, 'features.csv')

x = f.create_features(save_to_csv=True, save_to_hdf5=True)
print(x.shape)


#t0 = time.time()
#x = pd.read_csv(features_file)
#print(x.shape)
#print("Time to load: %d" % (time.time() - t0))
