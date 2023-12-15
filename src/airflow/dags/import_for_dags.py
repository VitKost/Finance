import sys
import os

sys.path.insert(0,os.path.abspath(sys.path[0] + "/../../"))
print(sys.path)

INCOMING_MESSAGES_PATH = os.path.abspath(__file__ + '/../../../../messages/incoming/*_CSV_LOAD_*.csv')