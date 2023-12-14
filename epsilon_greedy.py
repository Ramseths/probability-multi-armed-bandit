from bandit import MultiArmedBandit
from config import EPISODES

if __name__ == '__main__':
    e_greedy = MultiArmedBandit()
    e_greedy.run(EPISODES)
    e_greedy.stats()