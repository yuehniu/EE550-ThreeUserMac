"""Implementation of slotted-aloha

Author: Yue Niu, Chaoyi Jiang
"""
import numpy as np


class SlotAloha():
    def __init__( self, p ):
        self.p = p

    def decide_send( self, MyHistory, Opp1History, Opp2History ):
        send = np.random.binomial( 1, self.p )

        return send
