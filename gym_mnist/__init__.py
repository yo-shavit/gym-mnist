from gym.envs.registration import register

register(
    id='mnist-v0',
    entry_point='gym_mnist.envs:MNISTEnv',
)
register(
    id='mnist-full-v0',
    entry_point='gym_mnist.envs:MNISTEnv',
    kwargs={'full_mnist':True},
)
register(
    id='mnist-multiaction-v0',
    entry_point='gym_mnist.envs:MNISTMultiactionEnv',
)
register(
    id='blockwalker-v0',
    entry_point='gym_mnist.envs:BlockWalkerEnv',
)
register(
    id='blockwalker-multicolored-v0',
    entry_point='gym_mnist.envs:MulticoloredBlockWalkerEnv',
)
register(
    id='blockwalker-random-v0',
    entry_point='gym_mnist.envs:MulticoloredRandomBlockWalkerEnv',
)
