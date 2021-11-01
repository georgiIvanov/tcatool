from utilities.path_builder import PathBuilder
from models.file_types import FileTypes

def generate_action(name, path):
  str = f"""public enum {name}Action: Equatable {{

}}
"""
  PathBuilder.create_file(name, path, FileTypes.ACTION, str)