from utilities.path_builder import PathBuilder
from models.file_types import FileTypes
from models.gen_config import GenConfig

def generate_state(config: GenConfig):
  str = f"""public struct {config.name}State: Equatable {{
    public init() {{

    }}
}}
"""
  PathBuilder.create_file(config.name, config.path, FileTypes.STATE, str)