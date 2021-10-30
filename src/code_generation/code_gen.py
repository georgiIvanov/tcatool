import os
from models.file_types import FileTypes
from code_generation.generate_action import generate_action
from code_generation.generate_state import generate_state
from code_generation.generate_reducer import generate_reducer
from code_generation.generate_environment import generate_environment
from code_generation.generate_view import generate_view

def generate_code(name, path):
  generate_action(name, path)
  generate_state(name, path)
  generate_reducer(name, path)
  generate_environment(name, path)
  generate_view(name, path)
