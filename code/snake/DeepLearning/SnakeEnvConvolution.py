import gym
import pygame

import SnakeGym


class SnakeEnvConvolution(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.basegym: SnakeGym = SnakeGym.SnakeEnv()
        self.observation_space = self.basegym.observation_space
        self.action_space = gym.spaces.Discrete(4)

    def step(self, action) -> (list, float, bool, set):
        observation, reward, done, _ = self.basegym.step(action)
        return observation.field.field, reward, done, {}

    def reset(self):
        observation = self.basegym.reset()
        return observation.field.field

    def render(self, mode='human', close=False) -> None:
        self.basegym.render(mode, close)
        pygame.time.Clock().tick(1000)
