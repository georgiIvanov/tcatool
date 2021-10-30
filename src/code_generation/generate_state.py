from utility import create_file
from models.file_types import FileTypes

def generate_state(name, path):
  str = f"""public struct {name}State: Equatable {{
    public init() {{

    }}
}}
"""
  create_file(name, path, FileTypes.STATE, str)