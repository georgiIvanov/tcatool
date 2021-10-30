import os
from models.file_types import FileTypes
from code_generation.generate_action import generate_action
from code_generation.generate_state import generate_state
from code_generation.generate_reducer import generate_reducer
from code_generation.generate_environment import generate_environment
from code_generation.generate_view import generate_view
from utility import create_path

def generate_code(name, path):
  path = create_path(path)
  if os.path.exists(path) == False:
    os.makedirs(path)
  generate_action(name, path)
  generate_state(name, path)
  generate_reducer(name, path)
  generate_environment(name, path)
  generate_view(name, path)
