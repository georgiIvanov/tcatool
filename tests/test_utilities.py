import os

def build_output_path():
  return os.getcwd() + "/tests/actualOutput" 

def build_expected_path(dir):
  return os.getcwd() + "/tests/expectedOutput" + dir