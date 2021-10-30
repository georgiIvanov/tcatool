import os
from models.file_types import FileTypes
from utility import create_path, create_file

def generate_code(name, path):
  path = create_path(path)
  if os.path.exists(path) == False:
    os.makedirs(path)
  generate_action(name, path)
  generate_state(name, path)
  generate_reducer(name, path)
  generate_environment(name, path)

def generate_action(name, path):
  str = f"""public enum {name}Action: Equatable {{

}}
"""
  create_file(name, path, FileTypes.ACTION, str)
  
def generate_state(name, path):
  str = f"""public struct {name}State: Equatable {{
    public init() {{

    }}
}}
"""
  create_file(name, path, FileTypes.STATE, str)

def generate_reducer(name, path):
  str = f"""import ComposableArchitecture

let {name.lower()}Reducer = Reducer<
    {name}State, {name}Action, {name}Environment
> {{ (state, action, env) in
    .none
}}
"""
  create_file(name, path, FileTypes.REDUCER, str)

def generate_environment(name, path):
  str = f"""public struct {name}Environment {{
    public init() {{
        
    }}
}}

#if DEBUG

public extension {name}Environment {{
    static var noop: {name}Environment {{
        .init()
    }}
}}

#endif
"""
  create_file(name, path, FileTypes.ENVIRONMENT, str)