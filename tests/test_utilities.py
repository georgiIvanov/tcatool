import os
from unittest.mock import MagicMock
from models.gen_config import GenConfig

def build_output_path():
  return os.getcwd() + "/tests/actualOutput"

def build_expected_path(path):
  return os.getcwd() + "/tests/expectedOutput" + path

def get_last_part_of_path(path):
  head_tail = os.path.split(path)
  return head_tail[1]

def get_config_args(mocked_function: MagicMock) -> GenConfig:
  config, _ = mocked_function.call_args
  return config[0]
