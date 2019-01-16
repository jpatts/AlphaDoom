
import argparse
import tensorflow as tf

# ----------------------------------------
# Global variables
arg_lists = []
parser = argparse.ArgumentParser()

# Possible actions
shoot = [1, 0, 0]
left = [0, 1, 0]
right = [0, 0, 1]

# ----------------------------------------
# Macro for arparse
def add_argument_group(name):
    arg = parser.add_argument_group(name)
    arg_lists.append(arg)
    return arg

# ----------------------------------------
# Arguments for training
train_arg = add_argument_group("Training")

train_arg.add_argument("--learning_rate", type=float,
                       default=1e-4,
                       help="Learning rate (gradient step size)")

train_arg.add_argument("--batch_size", type=int,
                       default=8,
                       help="Positions in queue to be evaluated at a time")

train_arg.add_argument("--episodes", type=int,
                       default=1000,
                       help="Number of episodes to train on")

train_arg.add_argument("--Cpuct", type=float,
                       default=0.99,
                       help="Constant for determing exploration rate")

train_arg.add_argument("--T", type=int,
                       default=0.99,
                       help="Temperature for exploration")

train_arg.add_argument("--log_dir", type=str,
                       default="./logs/",
                       help="Directory to save logs")

train_arg.add_argument("--log_freq", type=int,
                       default=100,
                       help="Number of steps before logging weights")

train_arg.add_argument("--save_dir", type=str,
                       default="./saves/",
                       help="Directory to save current model")

train_arg.add_argument("--save_freq", type=int,
                       default=100,
                       help="Number of episodes before saving model")

train_arg.add_argument("-f", "--extension", type=str,
                       default=None,
                       help="Specific name to save training session or restore from")

# ----------------------------------------
# Arguments for testing
test_arg = add_argument_group("Testing")

test_arg.add_argument("--test_episodes", type=int,
                       default=100,
                       help="Number of episodes to test on")

# ----------------------------------------
# Arguments for model
model_arg = add_argument_group("Model")

model_arg.add_argument("--model", type=str,
                       default="atari",
                       choices=["atari", "alexnet", "zfnet", "vggnet", "googlenet"],
                       help="CNN architecture to use")

model_arg.add_argument("--activ", type=str,
                       default="relu",
                       choices=["relu", "elu", "selu", "tanh", "sigmoid"],
                       help="Activation function to use")

model_arg.add_argument("--init", type=str,
                       default="glorot_normal",
                       choices=["glorot_normal", "glorot_uniform", "random_normal", "random_uniform", "truncated_normal"],
                       help="Initialization function to use")

model_arg.add_argument("--actions", type=int,
                       default=[shoot, left, right],
                       help="Possible actions to take")

model_arg.add_argument("--skiprate", type=int,
                       default=3,
                       help="Number of frames to skip during each action. Current action will be repeated for duration of skip")

model_arg.add_argument("--num_frames", type=int,
                       default=4,
                       help="Number of stacked frames to send to CNN, depicting history")

# ----------------------------------------
# Function to be called externally
def get_config():
    config, unparsed = parser.parse_known_args()

    # If there are unparsed arguments, print usage and exit
    if len(unparsed) > 0:
        parser.print_usage()
        exit(1)

    return config
