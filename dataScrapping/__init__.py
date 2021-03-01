import sys
import os 
ABS_PATH = os.path.abspath('data_scrapping.py')
sys.path.append(ABS_PATH)

import data_scrapping

print(data_scrapping.INFO_FILE)

