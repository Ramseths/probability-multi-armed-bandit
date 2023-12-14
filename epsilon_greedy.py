from random import randint
from numpy.random import random

# Exploration Exploitation Trade Off
EPSILON = 0.1

# Iterations
EPISODES = 10000

# N# of Bandits
BANDITS = 3

class Bandit:

    def __init__(self, probability):
        # Q values
        self.q = 0

        # Actions was chosen in the past
        self.k = 0

        # Prob. Distribution
        self.probability = probability

    def get_reward(self):
        # 1 WIN, 0 LOSE
        if random() < self.probability:
            return 1
        else:
            return 0
    
class MultiArmedBandit:
    def __init__(self):
        self.bandits = []
        # Exploration 50%
        self.bandits.append(Bandit(0.5))
        # Exploration 60%
        self.bandits.append(Bandit(0.6))
        # Exploration 40%
        self.bandits.append(Bandit(0.4))

    def run(self):
        for i in range(EPISODES):
            bandit = self.bandits[self.select_bandit()]
            reward = bandit.get_reward()
            self.update(bandit, reward)

            print(f'Episode {i}, bandit {bandit.probability}: Q-value {bandit.q}')

    



