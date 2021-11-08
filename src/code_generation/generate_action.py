from utilities.path_builder import PathBuilder
from models.file_types import FileTypes
from models.gen_config import GenConfig

def generate_action(config: GenConfig):
  if config.noAction():
    return
  
  str = f"""public enum {config.name}Action: Equatable {{

}}
"""
  PathBuilder.create_file(config.name, config.path, FileTypes.ACTION, str)