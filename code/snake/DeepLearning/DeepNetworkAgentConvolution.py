import gym
import tensorflow
from rl.agents import DQNAgent
from rl.callbacks import ModelIntervalCheckpoint, FileLogger
from rl.memory import SequentialMemory
from rl.policy import LinearAnnealedPolicy, EpsGreedyQPolicy
from tensorflow.keras import Input, Model
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

from DeepLearning.SnakeEnvConvolution import SnakeEnvConvolution

WINDOW_LENGTH = 1


class DeepAgentConvolution:
    """
    This algorithm is trying to use a DQN agent that learns himself just given a gym.
    At the moment, it cannot successfully work with convolution:
    Error when checking input: expected input_1 to have 4 dimensions, but got array with shape (1, 1, 20, 10, 3)

    Best result: ???
    """

    def __init__(self, shape, action_count: int):
        super().__init__()

        inp = Input(shape=shape)

        # Convolution part (image recognition / feature extraction)
        conv = Conv2D(16, kernel_size=2, padding="same")(inp)
        conv = Conv2D(8, kernel_size=2)(conv)

        # Classification (decision making)
        flat = Flatten()(conv)
        # Activation: relu, sigmoid, ...
        hidden = Dense(256, activation='relu')(flat)
        hidden = Dense(64, activation='relu')(hidden)
        hidden = Dense(16, activation='relu')(hidden)
        output = Dense(action_count, activation='softmax')(hidden)

        self.model = Model(inputs=inp, outputs=output)
        print(self.model.summary())

        self.memory = SequentialMemory(limit=50000, window_length=WINDOW_LENGTH)
        self.policy = LinearAnnealedPolicy(EpsGreedyQPolicy(), attr='eps', value_max=1., value_min=.1, value_test=.05,
                                           nb_steps=1000)
        self.callbacks = self.build_callbacks("msnake")
        self.dqn = DQNAgent(model=self.model, nb_actions=action_count, memory=self.memory,  nb_steps_warmup=20,
                            target_model_update=1e-2, policy=self.policy)

        Adam._name = "fix_bug"  # https://github.com/keras-rl/keras-rl/issues/345
        # Metrics: mae, mse, accuracy
        # LR: learning rate
        self.dqn.compile(Adam(lr=1e-5), metrics=['mse'])

    def build_callbacks(self, env_name):
        callbacks = []

        checkpoint_weights_filename = 'dqn_' + env_name + '_weights_{step}.h5f'
        callbacks += [ModelIntervalCheckpoint(checkpoint_weights_filename, interval=5000)]

        log_filename = 'dqn_{}_log.json'.format(env_name)
        callbacks += [FileLogger(log_filename, interval=100)]
        return callbacks


def define_reward_system(env):
    # rewards
    env.reward_eat_food = 3.0
    env.additional_steps_function = lambda width, height, length: 200
    env.reward_closer_function = lambda distance: 0.1 if distance > 0 else 0
    env.reward_win = 1.0
    # penalties
    env.reward_impossible_move = -0.1
    env.reward_killed_by_wall = -1.0
    env.reward_killed_by_tail = -1.0
    env.reward_killed_by_starving_function = lambda steps, length: -0.1


if __name__ == "__main__":
    from gym.envs.registration import register

    register(id='mitusnakeconv-v0', entry_point='SnakeEnvConvolution:SnakeEnvConvolution', )
    env: SnakeEnvConvolution = gym.make("mitusnakeconv-v0")

    define_reward_system(env)

    # https://stackoverflow.com/questions/53429896/how-do-i-disable-tensorflows-eager-execution
    tensorflow.compat.v1.disable_eager_execution()

    agent = DeepAgentConvolution(env.observation_space.shape, 4)
    agent.dqn.fit(env, nb_steps=5000, visualize=True, verbose=2)
    agent.dqn.save_weights("dqn_mitusnakeconv-v0_weights.h5f", overwrite=True)
    agent.dqn.test(env, nb_episodes=20, visualize=True)
    print(env.basegym.training_data)
