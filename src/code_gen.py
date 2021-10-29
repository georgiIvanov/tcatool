import os

from utility import create_path

def generate_code(path):
  path = create_path(path)
  if os.path.exists(path) == False:
    os.makedirs(path)
