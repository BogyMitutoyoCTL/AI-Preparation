import gym
import tensorflow
from rl.agents import DQNAgent
from rl.callbacks import ModelIntervalCheckpoint, FileLogger
from rl.core import Processor
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy

from tensorflow.python.keras import Input, Sequential
from tensorflow.python.keras.engine.training import Model
from tensorflow.python.keras.layers import *
from tensorflow.python.keras.optimizers import Adam

from DeepLearning.SnakeEnvConvolutionalMachineLearning import SnakeEnvConvolutionalMachineLearning

WINDOW_LENGTH = 1

# https://stackoverflow.com/questions/53429896/how-do-i-disable-tensorflows-eager-execution
tensorflow.compat.v1.disable_eager_execution()


class RemoveDimensionProcessor(Processor):
    def process_state_batch(self, batch):
        processed = batch[0]
        return processed


class DeepAgent:
    """
    This algorithm is trying to use a DQN agent that learns himself just given a gym.
    After quite some trouble with various error messages, this now at least runs and trains.
    It does not yet achieve good results.

    Best result: ???
    """

    def __init__(self, shape, initial_randomness: float, action_count: int):
        super().__init__()

        model = Sequential()
        model.add(Input(shape=shape))
        model.add(Conv2D(8, (3, 3), activation='relu', input_shape=shape))
        model.add(Conv2D(16, (3, 3), activation='relu', input_shape=shape))
        model.add(Conv2D(32, (3, 3), activation='relu', input_shape=shape))
        model.add(Flatten())
        model.add(Dense(64, activation='relu'))
        model.add(Dense(512, activation='relu'))
        model.add(Dense(action_count, activation='softmax'))

        print(model.summary())

        self.model = model

        self.callbacks = self.build_callbacks("msnake")

        self.processor = RemoveDimensionProcessor()

        self.memory = SequentialMemory(limit=50000,
                                       window_length=1)

        self.policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps',
                                           value_max=1.,
                                           value_min=.1,
                                           value_test=.05,
                                           nb_steps=1000)

        self.dqn = DQNAgent(model=self.model,
                            nb_actions=action_count,
                            memory=self.memory,
                            nb_steps_warmup=10,
                            target_model_update=1e-2,
                            policy=self.policy,
                            batch_size=1,
                            processor=self.processor)

        # https://github.com/keras-rl/keras-rl/issues/345
        Adam._name = "fix_bug"

        # Metrics: mae, mse, accuracy
        # LR: learning rate
        self.dqn.compile(Adam(lr=1e-3), metrics=['mse'])

        self.initial_randomness = initial_randomness

    def build_callbacks(self, env_name):
        callbacks = []

        checkpoint_weights_filename = 'dqn_' + env_name + '_weights_{step}.h5f'
        callbacks += [ModelIntervalCheckpoint(checkpoint_weights_filename, interval=5000)]

        log_filename = 'dqn_{}_log.json'.format(env_name)
        callbacks += [FileLogger(log_filename, interval=100)]
        return callbacks


def define_reward_system(env):
    # rewards
    env.reward_eat_food = 15.0
    env.additional_steps_function = lambda width, height, length: 200
    env.reward_closer_function = lambda distance: 2 if distance > 0 else 0
    env.reward_win = 1.0

    # penalties
    env.reward_impossible_move = -1
    env.reward_killed_by_wall = -2.0
    env.reward_killed_by_tail = -2.0
    env.reward_killed_by_starving_function = lambda steps, length: -0.1


if __name__ == "__main__":
    from gym.envs.registration import register
    register(id='mitusnakeml-v0', entry_point='SnakeEnvConvolutionalMachineLearning:SnakeEnvConvolutionalMachineLearning', )
    env: SnakeEnvConvolutionalMachineLearning = gym.make("mitusnakeml-v0")
    env.head_view_size = 7
    define_reward_system(env)

    agent = DeepAgent((env.head_view_size, env.head_view_size * 2, 1), 0.05, 4)
    # agent.dqn.load_weights("net.h5f")
    # agent.dqn.test(env, nb_episodes=2000, visualize=True)
    agent.dqn.fit(env, nb_steps=800000, visualize=True, verbose=2)
    # agent.dqn.save_weights("net.h5f", overwrite=True)
    # agent.dqn.test(env, nb_episodes=20, visualize=True)
    input("Done")