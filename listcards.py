import sys, os
import anki.anki as anki
from anki.storage import Collection

# Load Anki library
sys.path.append("anki")

# Define the path to the Anki SQLite collection
PROFILE_HOME = os.path.expanduser('~/Documents/Anki/User 1')
cpath = os.path.join(PROFILE_HOME)