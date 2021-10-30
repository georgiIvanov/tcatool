import os

def create_path(path):
  if path == None:
    return os.getcwd()
  else:
    return os.getcwd() + path
