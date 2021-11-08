import os
from unittest.mock import MagicMock
from models.gen_config import GenConfig

def build_output_path():
  return os.getcwd() + "/tests/actualOutput" 

def build_expected_path(dir):
  return os.getcwd() + "/tests/expectedOutput" + dir

def get_last_part_of_path(path):
  head_tail = os.path.split(path)
  return head_tail[1]

def get_config_args(mockedFunction: MagicMock) -> GenConfig:
  config, kwargs = mockedFunction.call_args
  return config[0]
