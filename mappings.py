import csv
import pandas as pd

# local imports
from conf import *

ds = pd.read_csv(RECSYS_PATH)
mids = ds.MID.unique()
cpts = ds.CPT.unique()
icds = ds.ICD.unique()

mids_key = { k: v for v, k in enumerate(mids) }
cpts_key = { k: v for v, k in enumerate(cpts) }
icds_key = { k: v for v, k in enumerate(icds) }

with open(MIDS_KEY_PATH, 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["key", "mid"])
    for v, k in enumerate(mids):
       writer.writerow([v, k])

with open(CPTS_KEY_PATH, 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["key", "cpt"])
    for v, k in enumerate(cpts):
       writer.writerow([v, k])

with open(ICDS_KEY_PATH, 'wb') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["key", "cpt"])
    for v, k in enumerate(icds):
       writer.writerow([v, k])
