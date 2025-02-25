import numpy as np

class Hand:
    def __init__(self, hand, open_sequences, winning_tile):
        self.hand = hand
        self.open_sequences = open_sequences
        self.winning_tile = winning_tile

        # TODO: winning_tile should be a pair of (tile, tsumo/ron)


        self.menzenchin = true
        if open_sequences:
            # TODO: Deal with concealed Quads
            self.menzenchin = false
