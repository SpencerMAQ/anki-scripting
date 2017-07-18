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

# Use the available methods to list the notes
# for cid in col.findNotes('tag:Basic-Grammar Tae-Kim-Grammar-Guide comprehension'):   # [3] filter cards
#     note = col.getNote(cid)
#     # 'Front' is the first field of these cards
#     front = note.fields[1]
#     print(front)

name_of_deck = '全集Deck::JpcorePLUS'    # did:1406297528924(JPCoreplus)
name_of_model = 'Japanese-1b811 example_sentences'      # Note Type
field_to_match = 'Expression_Original_Unedited'

# did = mw.col.decks.byName("name")["id"] gets the ID only since
# did = mw.col.decks.byName("name") would return a dictionary
# you only need the ID which you would use for selection
did = col.decks.byName(name_of_deck)['id']
# print(col.decks.byName(name_of_deck))
updated_name = col.decks.name(did)
print(updated_name)

mid = col.models.byName(name_of_model)['id']        # get model ID

nids = col.findNotes('mid:' + str(mid))
# print(len(nids))
first_note_id = nids[1]
first_note = col.getNote(first_note_id)
# pprint(first_note.keys())

fields_to_match = []
def reschedule():
    for note_id in nids:
        note = col.getNote(note_id)
        # print(note[field_to_match])
        fields_to_match.append(note[field_to_match])
        # cid = col.getCards('nid:' + str(note_id))

        # There is no 'findCard' feature when going from notes
        # Because we are not always sure that for every note would be
        # One card

        # That is why findCards returns a list
        # Simply pick the first element of that list, simple
        cid = col.findCards('nid:' + str(note_id))
        first_card_id = cid[0]

        card = col.getCard(first_card_id)
        card.due = 0
        print(card.due)
        # print(cid)
        # print(type(cid))
        # col.sched.newDue()
        break

reschedule()

list_of_mined_words = []
def match_txt_cards():
    for line in list_of_mined_words:
        if line in fields_to_match:
            pass
            # set the due value of that note to ZERO

    # print(note_id)
# for cid in col.findCards(nid)

# ============== NOTE ==============
# This was a mistake, you can't find notes based on did
# you can find them using an mid though
# notes = col.findNotes('did:' + str(did))
# ============== NOTE ==============


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

