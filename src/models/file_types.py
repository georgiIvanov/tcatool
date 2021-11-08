from enum import Enum

class FileTypes(Enum):
  """Enum with possible file types tcatool can generate"""

  ACTION = "Action"
  STATE = "State"
  REDUCER = "Reducer"
  ENVIRONMENT = "Environment"
  VIEW = "View"
