"""Simulate a 3-user MAC game

Author: Yue Niu, Chaoyi Jiang
"""
import numpy as np
import matplotlib.pyplot as plt
from SlottedAloha import SlotAloha
from FourState import FourState

"""Simulate parameter"""
n_runs = 100
N = 10000
idle_avg, collision_avg = 0, 0
succ_user1_avg, succ_user2_avg, succ_user3_avg = 0, 0, 0


"""Start simulation"""
for r in range( n_runs ):
    user1 = FourState( 1/2 )
    # user1 = SlotAloha( 1/2 )
    user2 = SlotAloha( 1/2 )
    user3 = SlotAloha( 1/2 )

    n_idle, n_collision = 0, 0
    succ_user1, succ_user2, succ_user3 = 0, 0, 0
    history_user1, history_user2, history_user3 = [], [], []

    for i in range( N ):
        user1_send = user1.decide_send( history_user1, history_user2, history_user3 )
        user2_send = user2.decide_send( history_user2, history_user1, history_user3 )
        user3_send = user3.decide_send( history_user3, history_user1, history_user2 )

        all_send = user1_send + user2_send + user3_send

        if all_send == 0:
            n_idle += 1

        elif all_send > 1:
            n_collision += 1

        else:
            if user1_send:
                succ_user1 += 1
            elif user2_send:
                succ_user2 += 1
            elif user3_send:
                succ_user3 += 1

        # record history
        history_user1.append( user1_send )
        history_user2.append( user2_send )
        history_user3.append( user3_send )

    idle_avg += n_idle
    collision_avg += n_collision
    succ_user1_avg += succ_user1
    succ_user2_avg += succ_user2
    succ_user3_avg += succ_user3


"""Print stats"""
print( "Total idle time: {:.1f}, \tTotal collisions: {:.1f}".format( idle_avg/n_runs, collision_avg/n_runs ) )
print( "User 1 succ: {:.1f}, \tUser 2 succ: {:.1f}, \tUser 3 succ: {:.1f}".format( succ_user1_avg/n_runs, succ_user2_avg/n_runs, succ_user3_avg/n_runs ) )