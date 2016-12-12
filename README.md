# eternal-stats-parser
Command line stats parser for Eternal

## Description
This is a very simple python script for parsing Eternal deck statistics that are stored in CSV files. The script takes the raw data and presents it in a useful manner, providing the following:
⋅⋅* What decks you faced, sorted in order of frequency
⋅⋅* The breakdown of your opponent's factions
⋅⋅* For each of your decks, the total winrate and individual matchup winrates

The script requires Python 2.7 or 3 to run. The script takes no arguments, you only need to run it with your python interpreter. The CSV files containing your deck statistics should be in .txt files in a "data" directory relative to where you run the script.

## Example run of the program:
```
python stats.py
Unearthly's stat parser 1.1

Total games played: 15
Opponent decks:

Elysian Midrange   13.3% (2)
FJS Midrange       13.3% (2)
Icaria Blue        13.3% (2)
Stonescar Jito     13.3% (2)
Aggressive Combrei  6.7% (1)
Big Combrei         6.7% (1)
FJS Armory          6.7% (1)
Haunting Scream     6.7% (1)
Rakano Warcry       6.7% (1)
Shimmerpack         6.7% (1)
Stonescar Midrange  6.7% (1)

Faction breakdown
Stonescar: 20.0% (3)
Rakano   : 20.0% (3)
Elysian  : 20.0% (3)
Combrei  : 13.3% (2)
Hooru    :  0.0% (0)
Argenport:  0.0% (0)
Praxis   :  0.0% (0)
Xenan    :  0.0% (0)
Feln     :  0.0% (0)
Skykrag  :  0.0% (0)
Other    : 26.7% (4)

Rakano Warcry
  Total winrate: 50.0% (3-3)
  Play winrate:  100.0% (2-0)
  Draw winrate:  25.0% (1-3)
Matchups:
  Elysian Midrange   100.0% - (1-0)
  Stonescar Midrange 100.0% - (1-0)
  FJS Midrange        50.0% - (1-1)
  Icaria Blue          0.0% - (0-1)
  Stonescar Jito       0.0% - (0-1)

Stonescar Burn
  Total winrate: 66.7% (6-3)
Matchups:
  Aggressive Combrei 100.0% - (1-0)
  Big Combrei        100.0% - (1-0)
  FJS Armory         100.0% - (1-0)
  Haunting Scream    100.0% - (1-0)
  Icaria Blue        100.0% - (1-0)
  Shimmerpack        100.0% - (1-0)
  Elysian Midrange     0.0% - (0-1)
  Rakano Warcry        0.0% - (0-1)
  Stonescar Jito       0.0% - (0-1)
```

## CSV Format
The format for the deck statistics is expected to be CSV format. The first line should be the name of your deck. Following lines should be P or D (Whether you were on the Play or Draw), followed by a comma, W or L (Win or Loss), followed be a comma, followed by the name of the opponent's deck. The opponent deck name is purely subjective, choose however you wish.
Example:
```
Rakano Warcry
P,W,Stonescar Burn
D,L,Combrei Midrange
```

There are more examples in src/data