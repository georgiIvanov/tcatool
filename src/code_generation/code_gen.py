from code_generation.generate_action import generate_action
from code_generation.generate_state import generate_state
from code_generation.generate_reducer import generate_reducer
from code_generation.generate_environment import generate_environment
from code_generation.generate_view import generate_view
from models.gen_config import GenConfig

def generate_code(config: GenConfig):
  generate_action(config)
  generate_state(config)
  generate_reducer(config)
  generate_environment(config)
  generate_view(config)
