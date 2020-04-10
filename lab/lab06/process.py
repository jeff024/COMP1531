import pickle
from unpickle import most_common
import json

DATA = pickle.load(open("shapecolour.p", "rb"))
common = most_common(DATA)

D = {
    "moct_common": {
        "colour": common['colour'],
        "Shape": common['shape']
    },
    "rawDATA": DATA
}

with open('processed.json', 'w') as FILE:
    print(json.dumps(D))
    json.dump(D, FILE)
