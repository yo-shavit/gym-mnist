import gym
from gym import error, spaces, utils
from gym.utils import seeding

class MNISTEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    ...
  def _step(self, action):
    ...
  def _reset(self):
    ...
  def _render(self, mode='human', close=False):
    ...

class MNISTMultiactionEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    ...
  def _step(self, action):
    ...
  def _reset(self):
    ...
  def _render(self, mode='human', close=False):
    ...


