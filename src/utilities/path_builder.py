import os
from unittest.mock import patch

class PathBuilder:
  """Use this class to create files. 

  It gets a base path and then appends directories to it.
  """

  def __init__(self, baseDir):
    """Inits PathBuilder with baseDir function"""
    self.baseDir = baseDir

  def _assemble_path(self, path):
    if path == None or path == "/" or path == ".":
      return self.baseDir
    else:
      return self.baseDir + path

  def create_path(self, path: str = None) -> str:
    if path != None and path[-1] == "/":
      path = "/" + path[:-1]

    fullPath = self._assemble_path(path)
    if os.path.exists(fullPath) == False:
      os.makedirs(fullPath)
    return fullPath

  @staticmethod
  def create_file(name, path, type, content):
    filePath = os.path.join(path, (name + type.value + ".swift"))
    with open(filePath, "w") as f:
      f.write(content)