import os

def create_path(path):
  if path == None:
    return os.getcwd()
  else:
    return os.getcwd() + path

def _create_swift_file(name, path, kind):
  filePath = os.path.join(path, (name + kind + ".swift"))
  return open(filePath, "w")

def create_file(name, path, type, content):
  f = _create_swift_file(name, path, type.value)
  f.write(content)