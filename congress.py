import csv
from collections import namedtuple, defaultdict
from pprint import pprint
import glob
from typing import NamedTuple, DefaultDict, Tuple

#Senator = namedtuple("Senator", ["name", "party", "state"])
Senator = NamedTuple("Senator", [("name", str), ("party", str), ("state", str)])
VotingValue = int
VotingHistory = Tuple[VotingValue, ...]
# Load votes which were arranged by topic and accumlate vote by senator
vote_value = {"Yea" : 1, "Nay" : -1, "Not Voting": 0}                           # type: Dict[str, VotingValue]
accumelated_record = defaultdict(list)                                          # type: DefaulDict[Senator, List[VotingValue]]
for filename in glob.glob("./congress_data/*.csv"):
    with open(filename, encoding="utf") as file:
        reader = csv.reader(file)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in csv.reader(file):
            # person, state, district, vote, name, party
            senator = Senator(name, party, state)
            accumelated_record[senator].append(vote_value[vote])

# transform the record into a plain dict that maps to tuple of votes 
record = {senator: tuple(votes) for senator, votes in accumelated_record.items()}           # type: Dict[Senator, VotingHistory]


pprint(record, width=500)
