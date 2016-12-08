# eternal-stats-parser
Command line stats parser for Eternal

## Description
This is a very simple python script for parsing Eternal deck statistics that are stored in CSV files. The script takes the raw data and presents it in a useful manner, providing the following:
⋅⋅* What decks you faced, sorted in order of frequency
⋅⋅* The breakdown of your opponent's factions
⋅⋅* For each of your decks, the total winrate and individual matchup winrates

The script requires Python 3 to run. The script takes no arguments, you only need to run it with your python interpreter. The CSV files containing your deck statistics should be in .txt files in a "data" directory relative to where you run the script.

## Example run of the program:
```
python stats.py
Unearthly's stat parser 1.0

Total games played: 18
Opponent decks:

Stonescar Burn     16.7% (3)
Aggressive Combrei 11.1% (2)
Feln Control       11.1% (2)
Rakano Warcry      11.1% (2)
Stonescar Jito     11.1% (2)
Big Combrei         5.6% (1)
Combrei Midrange    5.6% (1)
Elysian Midrange    5.6% (1)
FJS Armory          5.6% (1)
Haunting Scream     5.6% (1)
Icaria Blue         5.6% (1)
Shimmerpack         5.6% (1)

Faction breakdown
Stonescar: 27.8% (5)
Combrei  : 22.2% (4)
Rakano   : 16.7% (3)
Elysian  : 11.1% (2)
Feln     : 11.1% (2)
Argenport:  0.0% (0)
Hooru    :  0.0% (0)
Xenan    :  0.0% (0)
Skykrag  :  0.0% (0)
Praxis   :  0.0% (0)
Other    : 11.1% (2)

Shimmerpack Matchups: 55.6% (5-4)
Stonescar Burn     100.0% - (3-0)
Aggressive Combrei 100.0% - (1-0)
Rakano Warcry      100.0% - (1-0)
Combrei Midrange     0.0% - (0-1)
Feln Control         0.0% - (0-2)
Stonescar Jito       0.0% - (0-1)

Stonescar Burn Matchups: 66.7% (6-3)
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
The format for the deck statistics is expected to be CSV format. The first line should be the name of your deck. Following lines should be W or L, followed be a comma, followed by the name of the opponent's deck. The opponent deck name is purely subjective, choose however you wish.
Example:
```
Rakano Warcry
W,Stonescar Burn
L,Combrei Midrange
```

There are more examples in src/data