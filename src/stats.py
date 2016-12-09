# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This script parses all files that end in the extension ".txt" in the "data"
# directory and then prints various information including:
#   - What decks you faced, sorted in order of frequency
#   - The breakdown of your opponent's factions
#   - For each of your decks, the total winrate and individual matchup winrates
#
# The format for the deck statistics is expected to be CSV format.
# The first line should be the name of your deck. Following lines should be W
# or L, followed be a comma, followed by the name of the opponent's deck.
# The opponent deck name is purely subjective, choose however you wish.
# Example:
#Rakano Warcry
#W,Stonescar Burn
#L,Combrei Midrange

from __future__ import absolute_import, division, print_function, unicode_literals
import glob
import math
import operator
import sys

factions = ['Rakano','Combrei','Elysian','Feln','Stonescar',
                'Xenan','Hooru','Argenport','Praxis','Skykrag']
faction_keywords = dict()
faction_keywords['Queen'] = 'Stonescar'
faction_keywords['Jito'] = 'Stonescar'
faction_keywords['Icaria'] = 'Rakano'
faction_keywords['Shimmerpack'] = 'Elysian'
faction_keywords['Reanimator'] = 'Feln'

min_meta_count = 1
include_mirror = True

meta = dict()
sorted_meta = None
records = dict()
sorted_records = None
total_games = 0.0
max_deck_length = 0
faction_counts = dict()
sorted_factions = None

class Record:
    """Class that holds a deck's win/loss record.'"""
    def __init__( self, deck ):
        self.deck = deck
        self.wins = 0
        self.losses = 0

    @property
    def percentage( self ):
        return float( self.wins )*100 / ( self.wins + self.losses )

    @property
    def count( self ):
        return self.wins+self.losses

def parse_stats_file( stat_file ):
    """Parses a file containing a single deck's match statistics."""
    global meta
    global records
    global total_games
    global max_deck_length

    first = True
    with open( stat_file ) as stat_handle:
        stat_data = stat_handle.read()
        for line in stat_data.split( '\n' ):
            if first:
                deck = line
                first = False
                continue
            original_line = line
            # Ignore empty lines.
            if original_line == '':
                continue
            line = original_line.split( ',' )
            # The line must have exactly two entries, the W/L and the deck name.
            if len( line ) != 2:
                raise ValueError( 'Found invalid line in file "'+stat_file+'": '+original_line )
            result = line[0]
            opponent_deck = line[1]
            if not opponent_deck in meta:
                meta[opponent_deck] = Record( opponent_deck )
            if not deck in records:
                records[deck] = dict()
            if not opponent_deck in records[deck]:
                records[deck][opponent_deck] = Record( opponent_deck )
            if result == 'W':
                records[deck][opponent_deck].wins += 1
                meta[opponent_deck].losses += 1
            elif result == 'L':
                records[deck][opponent_deck].losses += 1
                meta[opponent_deck].wins += 1
            added = False
            for faction in factions:
                if added:
                    break
                if faction in opponent_deck:
                    faction_counts[faction] += 1
                    added = True
                else:
                    for keyword in faction_keywords:
                        if keyword in opponent_deck:
                            faction_counts[faction_keywords[keyword]] += 1
                            added = True
                            break

def parse_all_stats():
    """Parse all stats files and store the results."""
    global meta
    global sorted_meta
    global records
    global sorted_records
    global total_games
    global max_deck_length
    global faction_counts
    global sorted_factions
    
    for faction in factions:
        faction_counts[faction] = 0

    for stats_file in glob.glob( "data/*.txt" ):
        parse_stats_file( stats_file )
    
    sorted_factions = sorted( faction_counts.items(), key=operator.itemgetter(1), reverse=True )

    total_games = 0.0
    max_deck_length = 0
    for deck in meta:
        deck_games = meta[deck].count
        if deck_games < min_meta_count:
            continue
        total_games += deck_games
        max_deck_length = max( max_deck_length, len(deck) )

    sorted_meta = sorted( meta.items(), key=operator.itemgetter(0) )
    sorted_meta = sorted( sorted_meta, key=lambda r: r[1].count, reverse=True )
    for deck, record in sorted_meta:
        record.representation = record.count / total_games * 100

    sorted_records = sorted( records.items(), key=operator.itemgetter(0) )

def main( args ):
    global meta
    global sorted_meta
    global records
    global sorted_records
    global total_games
    global max_deck_length
    global faction_counts
    global sorted_factions

    print( "Unearthly's stat parser 1.0\n" )

    try:
        parse_all_stats()
    except Exception as e:
        print( 'Encountered error:' )
        print( '  '+str(e) )
        return 1

    print( 'Total games played: %.0f' % total_games )
    print( 'Opponent decks:\n' )
    count_justify = -1
    for deck, record in sorted_meta:
        if record.count < min_meta_count:
            continue
        if count_justify == -1:
            count_justify = int(math.log10(record.count))+3
        justify = max_deck_length
        representation = '%.1f%%' % ( record.representation )
        count = '(%d)' % ( record.count )
        print( "%s %s %s" % (
            deck.ljust(justify),
            representation.rjust(5),
            count.rjust(count_justify)
        ) )
    
    max_faction_length = 0
    count_justify = 0
    for faction,count in sorted_factions:
        max_faction_length = max( max_faction_length, len(faction) )

    print( '\nFaction breakdown' )
    remaining = total_games
    count_justify = -1
    for faction,count in sorted_factions:
        if count_justify == -1:
            count_justify = int(math.log10(count))+3
        remaining -= count
        percentage = '%.1f%%' % (count / total_games * 100)
        count = '(%d)' % ( count )
        print( "%s: %s %s" % (
            faction.ljust(max_faction_length),
            percentage.rjust(5),
            count.rjust(count_justify) ) )
    percentage = '%.1f%%' % (remaining / total_games * 100)
    count = '(%d)' % ( remaining )
    print( "%s: %s %s" % (
            'Other'.ljust(max_faction_length),
            percentage.rjust(5),
            count.rjust(count_justify) ) )

    for deck, results in sorted_records:
        records_array = []
        total_wins = 0
        total_games = 0
        for opponent_deck in records[deck]:
            if deck == opponent_deck and not include_mirror:
                continue
            deck_games = records[deck][opponent_deck].wins+records[deck][opponent_deck].losses
            if deck_games < min_meta_count:
                continue
            total_wins += records[deck][opponent_deck].wins
            total_games += deck_games
            records_array.append( records[deck][opponent_deck] )
        if total_games == 0:
            continue
        total_losses = total_games-total_wins
        print()
        print( "%s Matchups: %.1f%% (%d-%d)" % ( deck, total_wins*100/float(total_games), total_wins, total_losses ) )
        records_array.sort( key=lambda x: x.deck )
        records_array.sort( key=lambda x: x.wins, reverse=True )
        records_array.sort( key=lambda x: x.percentage, reverse=True )
        for record in records_array:
            percentage = '%.1f%%' % ( record.percentage )
            print( "%s %s - (%d-%d)" % (
                record.deck.ljust(max_deck_length),
                percentage.rjust(6),
                record.wins,
                record.losses ) )

if __name__ == '__main__':
    sys.exit( main( sys.argv ) or 0 )