from utility import create_file
from models.file_types import FileTypes

def generate_reducer(name, path):
  str = f"""import ComposableArchitecture

let {name.lower()}Reducer = Reducer<
    {name}State, {name}Action, {name}Environment
> {{ (state, action, env) in
    .none
}}
"""
  create_file(name, path, FileTypes.REDUCER, str)