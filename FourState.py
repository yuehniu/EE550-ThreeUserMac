"""Implementation of 4-stage transmission protocal

Author: Yue Niu, Chaoyi Jiang
"""
import numpy as np

class FourState():
    def __init__(self, p ):
        self.p = p
        self.MyCurState = None
        self.MyNextState = None

    def decide_send( self, MyHistory, Opp1History, Opp2History ):
        if self.MyCurState is None:
            self.MyNextState = 'State1'

        elif self.MyCurState == 'State1':
            if MyHistory[ -1 ] == 1 and Opp1History[ -1 ] == 0 and Opp2History[ -1 ] == 0:
                self.MyNextState = 'State2'
            elif MyHistory[ -1 ] == 0 and Opp1History[ -1 ] == 1 and Opp2History[ -1 ] == 0:
                self.MyNextState = 'State3'
            elif MyHistory[ -1 ] == 0 and Opp1History[ -1 ] == 0 and Opp2History[ -1 ] == 1:
                self.MyNextState = 'State3'
            else:
                self.MyNextState = 'State1'

        elif self.MyCurState == 'State2':
            if Opp1History[ -1 ] == 1 or Opp2History[ -1 ] == 1:
                self.MyNextState = 'State3'
            else:
                self.MyNextState = 'State4'

        elif self.MyCurState == 'State3':
            if MyHistory[ -1 ] == 1 and Opp1History[ -1 ] == 0 and Opp2History[ -1 ] == 0:
                self.MyNextState = 'State2'
            else:
                self.MyNextState = 'State3'

        elif self.MyCurState == 'State4':
            if MyHistory[ -1 ] + Opp1History[ -1 ] + Opp2History[ -1 ] > 1:
                self.MyNextState = 'State1'
            else:
                self.MyNextState = 'State4'

        # decide whether to send
        if self.MyNextState == 'State1':
            send = np.random.binomial( 1, 1/3 )
        elif self.MyNextState == 'State2':
            send = 0
        elif self.MyNextState == 'State3':
            send = np.random.binomial( 1, self.p )
        elif self.MyNextState == 'State4':
            send = 1

        self.MyCurState = self.MyNextState

        return send