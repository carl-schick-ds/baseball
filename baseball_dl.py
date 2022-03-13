# Import needed libraries.  Unless noted, all libraries are available in the baseline conda environment.
import sqlite3
import pandas as pd
from IPython.display import display

class Baseball_Data_Loader:
    def __init__(self):
        self.database = 'data/mlb_data.sqlite'
        self.conn = sqlite3.connect(self.database)

    def get_players(self):
        query = "SELECT player_id, name_first ||' ' || name_last AS name, debut, weight, height, bats AS bat_hand, throws AS throw_hand FROM player"

        players_df = pd.read_sql_query(query, self.conn)
        players_df.set_index('player_id', inplace=True)
        players_df.index.name = 'player_id'

        display(players_df.head())
        return players_df

    def get_player_positions(self):
        query = 'SELECT player_id, ' \
        'SUM(g_c) AS catcher, ' \
        'SUM(g_1b) AS firstbaseman, ' \
        'SUM(g_2b) AS secondbaseman, ' \
        'SUM(g_3b) AS thirdbaseman, ' \
        'SUM(g_ss) AS shortstop, ' \
        'SUM(g_of) AS outfielder ' \
        'FROM appearances GROUP BY player_id'

        plyr_pos_df = pd.read_sql_query(query, self.conn)
        display(plyr_pos_df.head())
        return plyr_pos_df

    def get_player_performance(self):
        query = "SELECT player_id, year, stint, g AS games_yr, ab AS at_bats, h AS hits, hr, rbi FROM batting"
        performance_df = pd.read_sql_query(query, self.conn)

        display(performance_df.head())
        return performance_df