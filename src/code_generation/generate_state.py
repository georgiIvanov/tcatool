from utilities.path_builder import PathBuilder
from models.file_types import FileTypes

def generate_state(name, path):
  str = f"""public struct {name}State: Equatable {{
    public init() {{

    }}
}}
"""
  PathBuilder.create_file(name, path, FileTypes.STATE, str)