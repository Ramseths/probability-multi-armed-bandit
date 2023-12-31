from random import randint
from numpy.random import random
from config import EPSILON, BANDITS

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
        # Exploration 80%
        self.bandits.append(Bandit(0.8))
        # Exploration 60%
        self.bandits.append(Bandit(0.6))
        # Exploration 40%
        self.bandits.append(Bandit(0.4))

    def run(self, episodes):
        for i in range(episodes):
            bandit = self.bandits[self.get_bandit()]
            reward = bandit.get_reward()
            self.update(bandit, reward)

            print(f'Episode {i}, bandit {bandit.probability}: Q-value {bandit.q}')

    def get_bandit(self):
        # Epsilon Greedy Strategy

        if random() < EPSILON:
            # Exploration
            bandit_index = randint(0, BANDITS - 1)
        else:
            # Exploitation
            bandit_index = self.max_q_bandit()

        return bandit_index
    
    def stats(self):
        # Shows how many times the Bandit has been selected
        for i in range(BANDITS):
            print(f'Bandit {i} with k {self.bandits[i].k}')
    
    def update(self, bandit, reward):
        bandit.k = bandit.k + 1
        bandit.q = bandit.q + (1 / (1 + bandit.k)) * (reward - bandit.q)

    def max_q_bandit(self):
        # Bandit with max Q(a) value (Exploitation)
        bandit_index = 0
        max_q = self.bandits[bandit_index].q

        for i in range(1, BANDITS):
            if self.bandits[i].q > max_q:
                max_q = self.bandits[i].q
                bandit_index = i

        return bandit_index