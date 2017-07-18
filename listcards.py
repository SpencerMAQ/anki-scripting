import sys, os
from pprint import pprint

from anki.storage import Collection

# NOTE: This project is not yet set-up to use the VIRTUALENV

# Load Anki library
# https://www.youtube.com/watch?v=vR_6mkQ23sM
# what this does is it adds ~/anki (folder) to where python searches for modules,
# thus we don't have to do somehting like from anbki.anki.storage import Collection
sys.path.append("anki")  # [1] We need to add the Anki project in our path

# Define the path to the Anki SQLite collection
# PROFILE_HOME = os.path.expanduser('~/Documents/Anki/User 1')  # [2]
PROFILE_HOME = r'D:\TeMP\1_!_!_!_TEMP\1_ANKITEMPS\ankiscripting\Anki\User 1'
cpath = os.path.join(PROFILE_HOME, 'collection.anki2')

# Load the Collection
col = Collection(cpath, log=True)   # Entry point to the API

# print(os.path.exists(cpath))
# print(os.path.isfile(cpath))

# Use the available methods to list the notes
# for cid in col.findNotes('tag:Basic-Grammar Tae-Kim-Grammar-Guide comprehension'):   # [3] filter cards
#     note = col.getNote(cid)
#     # 'Front' is the first field of these cards
#     front = note.fields[1]
#     print(front)

name_of_deck = r'A_Misc::MyNotes'


# did = mw.col.decks.byName("name")["id"] gets the ID only since
# did = mw.col.decks.byName("name") would return a dictionary
# you only need the ID which you would use for selection
did = col.decks.byName(name_of_deck)['id']

name_of_deck = col.decks.name(did)
pprint(col.decks.byName(name_of_deck))

# mid = col.decks.byName(name_of_deck)['mid']     # get model ID
# print(mid)

# notes = col.findNotes('mid:' + str(mid))
# print(len(notes))
# print(col.decks.name(did))

# ============== NOTE ==============
# This was a mistake, you can't find notes based on did
# you can find them using an mid though
# notes = col.findNotes('did:' + str(did))
# ============== NOTE ==============

# print(notes)
# deck = col.decks.get(did)
# print(deck.items())
# pprint(dir(deck))

# These are the methods for deck
# ['clear',
# 'copy',
# 'fromkeys',
# 'get',
# 'items',      # dict items (key-value pair)
# 'keys',       # dict key
# 'pop',
# 'popitem',
# 'setdefault',
# 'update',
# 'values']     # dict value

