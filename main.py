"""
python3 main.py --gin_file config.gin --gin_param "TrainArgument.output_dir='my_output_dir2'"
"""

import gin
import gin_template
from absl import app
from external import TrainArgument
# mimic: from transformers import TrainingArguments

gin.external_configurable(TrainArgument)


@gin.configurable
def train(train_args: TrainArgument):
    print(train_args.output_dir)
    return


def main(_):
    gin_template.parse_and_log_config()
    train()


if __name__ == "__main__":
    app.run(main)
