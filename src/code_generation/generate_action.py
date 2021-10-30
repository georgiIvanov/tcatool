from utility import create_file
from models.file_types import FileTypes

def generate_action(name, path):
  str = f"""public enum {name}Action: Equatable {{

}}
"""
  create_file(name, path, FileTypes.ACTION, str)