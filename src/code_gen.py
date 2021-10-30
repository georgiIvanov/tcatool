import os
from file_types import FileTypes

from utility import create_path
from file_types import FileTypes

def generate_code(name, path):
  path = create_path(path)
  if os.path.exists(path) == False:
    os.makedirs(path)
  generate_action(name, path)

def generate_action(name, path):
  f = create_swift_file(name, path, FileTypes.ACTION.value)
  str = f"""public enum {name}Action: Equatable {{

}}
"""
  f.write(str)
  

def create_swift_file(name, path, kind):
  filePath = os.path.join(path, (name + kind + ".swift"))
  return open(filePath, "w")