from utilities.path_builder import PathBuilder
from models.file_types import FileTypes
from models.gen_config import GenConfig

def generate_reducer(config: GenConfig):
  str = f"""import ComposableArchitecture

let {config.name.lower()}Reducer = Reducer<
    {config.name}State, {config.name}Action, {config.name}Environment
> {{ (state, action, env) in
    .none
}}
"""
  PathBuilder.create_file(config.name, config.path, FileTypes.REDUCER, str)