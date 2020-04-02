import gym
import numpy
import pygame

import SnakeGym


class SnakeEnvMachineLearning(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.basegym: SnakeGym = SnakeGym.SnakeEnv()
        self.observation_space = self.basegym.observation_space
        self.action_space = gym.spaces.Discrete(4)

    def step(self, action) -> (list, float, bool, set):
        obs, rew, done, _ = self.basegym.step(action)
        return self.head_view(obs), rew, done, {}
        # return self.reduce(obs.field.field), rew, done, {}

    def head_view(self, info) -> list:
        surrounding = []
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                surrounding.append( 0 if info.can_move_to(info.head_x + dx, info.head_y + dy) else 1)
        segment_count = 12
        foodsegment = int(((info.food_direction + 360) % 360) / (360 / segment_count))
        for i in range(segment_count):
            if i == foodsegment:
                surrounding.append(1.0)
            else:
                surrounding.append(0.0)
        return surrounding

    def reduce(self, field):
        a = numpy.array(field)
        a = -a[..., 0] + a[..., 1] + a[..., 2]
        return a
        # normalized = a / (numpy.max(a) - numpy.min(a))
        # return normalized

    def reset(self):
        obs = self.basegym.reset()
        # return self.reduce(obs.field.field)
        return self.head_view(obs)

    def render(self, mode='human', close=False) -> None:
        self.basegym.render(mode, close)
        pygame.time.Clock().tick(10)
