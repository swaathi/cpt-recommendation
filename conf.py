import os

DIRPATH = os.path.dirname(os.path.abspath(__file__))
HOMEPATH = DIRPATH + '/data'
# HOMEPATH = os.path.expanduser("~")

# Full dataset
RECSYS_PATH = HOMEPATH + '/recsys.csv'
# Extracted, mapped and cleaned(duplicate removal) recpt dataset
RECPT_PATH = HOMEPATH + '/recpt.csv'
# Extracted, mapped and cleaned(duplicate removal) recpt dataset
REICD_PATH = HOMEPATH + '/reicd.csv'
# Mapping dataset for mids
MIDS_KEY_PATH = HOMEPATH + '/mids_key.csv'
# Mapping dataset for cpts
CPTS_KEY_PATH = HOMEPATH + '/cpts_key.csv'
# Mapping dataset for icds
ICDS_KEY_PATH = HOMEPATH + '/icds_key.csv'

# from recpt import Recpt
# r = Recpt()

# d = r.mids_key[r.mids_key.mid == 659]
