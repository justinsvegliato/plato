#!/usr/bin/env python
import time

import numpy as np

import grid_world as domain
from mdp import MDP
from utils import key


def simulate(policy):
    steps = 0
    current_state = domain.get_start_state()

    while not np.array_equal(current_state, domain.get_goal_state()):
        current_state = domain.get_next_state(current_state, policy[key(current_state)])

        steps += 1

        if steps > 1000:
            return False

    return steps


def execute_vi_example(mdp):
    start = time.clock()
    policy = mdp.solve(solver='vi')
    end = time.clock()
    print('The MDP was solved using VI in %d seconds.' % (end - start))

    steps = simulate(policy)
    print('The agent reached the goal in %s steps.' % steps)


def execute_pi_example(mdp):
    start = time.clock()
    policy = mdp.solve(solver='pi')
    end = time.clock()
    print('The MDP was solved using PI in %d seconds.' % (end - start))

    steps = simulate(policy)
    print('The agent reached the goal in %s steps.' % steps)


def execute_mc_example(mdp):
    start = time.clock()
    policy = mdp.solve(solver='mc')
    end = time.clock()
    print('The MDP was solved using MC in %d seconds.' % (end - start))

    steps = simulate(policy)
    print('The agent reached the goal in %s steps.' % steps)


def main():
    mdp = MDP(
        domain.get_states(),
        domain.get_actions(),
        domain.get_transition_probability,
        domain.get_reward
    )

    print('Value Iteration:')
    execute_vi_example(mdp)
    print()

    print('Policy Iteration:')
    execute_pi_example(mdp)
    print()

    print('Monte Carlo:')
    execute_mc_example(mdp)


if __name__ == '__main__':
    main()
