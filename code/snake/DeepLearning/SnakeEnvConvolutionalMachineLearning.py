import math

import gym
import pygame

import SnakeGym


class SnakeEnvConvolutionalMachineLearning(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.basegym: SnakeGym = SnakeGym.SnakeEnv()
        self.observation_space = self.basegym.observation_space
        self.action_space = gym.spaces.Discrete(4)
        self.head_view_size = 3

    def step(self, action) -> (list, float, bool, set):
        obs, rew, done, _ = self.basegym.step(action)
        data = self.head_view(obs)
        return data, rew, done, {}

    def head_view(self, info) -> list:
        surrounding = []
        for dy in range(self.head_view_size):
            line = self.head_view_size * [[0]]
            for dx in range(self.head_view_size):
                x = info.head_x + dx - int(self.head_view_size / 2)
                y = info.head_y + dy - int(self.head_view_size / 2)

                line.append([1 if info.can_move_to(x, y) else 0])

            surrounding.append(line)

        food_x = round(math.sin(
            math.radians(info.food_direction + 360)) * min(info.air_line_distance, self.head_view_size/2)
                       + int(self.head_view_size / 2))

        food_y = round(math.cos(
            math.radians(info.food_direction + 360)) * min(info.air_line_distance, self.head_view_size/2)
                       + int(self.head_view_size / 2))

        surrounding[food_x][food_y][0] = 1

        return surrounding

    def reset(self):
        obs = self.basegym.reset()
        return self.head_view(obs)

    def render(self, mode='human', close=False) -> None:
        self.basegym.render(mode, close)
        pygame.time.Clock().tick(1000)
