import os

class PathBuilder:
  """Use this class to create files.
  It gets a base path and then appends directories to it.
  """

  def __init__(self, base_dir):
    """Inits PathBuilder with baseDir function"""
    self.base_dir = base_dir

  def _assemble_path(self, path):
    if path is None or path == "/" or path == ".":
      return self.base_dir
    return self.base_dir + path

  def create_path(self, path: str = None) -> str:
    if path is not None and path[-1] == "/":
      path = "/" + path[:-1]

    full_path = self._assemble_path(path)
    if os.path.exists(full_path) is False:
      os.makedirs(full_path)
    return full_path

  @staticmethod
  def create_file(name, path, file_type, content):
    file_path = os.path.join(path, (name + file_type.value + ".swift"))
    with open(file_path, "w", encoding="ascii") as file:
      file.write(content)
    