from enum import Enum

class FileTypes(Enum):
  ACTION = "Action"
  STATE = "State"
  REDUCER = "Reducer"
  ENVIRONMENT = "Environment"
  VIEW = "View"