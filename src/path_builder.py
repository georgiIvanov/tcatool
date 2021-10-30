import os

class PathBuilder:
  """Use this class to create files. 

  It gets a base path and then appends directories to it.
  """

  def __init__(self, baseDir):
    """Inits PathBuilder with baseDir function"""
    self.baseDir = baseDir

  def _assemble_path(self, path):
    if path == None:
      return self.baseDir
    else:
      return self.baseDir + path

  def create_path(self, path):
    fullPath = self._assemble_path(path)
    if os.path.exists(fullPath) == False:
      os.makedirs(fullPath)
    return fullPath

  @staticmethod
  def create_file(name, path, type, content):
    filePath = os.path.join(path, (name + type.value + ".swift"))
    f = open(filePath, "w")
    f.write(content)