from utilities.path_builder import PathBuilder
from models.file_types import FileTypes
from models.gen_config import GenConfig

def generate_environment(config: GenConfig):
  if config.no_environment():
    return

  output = f"""public struct {config.name}Environment {{
    public init() {{
        
    }}
}}

#if DEBUG

public extension {config.name}Environment {{
    static var noop: {config.name}Environment {{
        .init()
    }}
}}

#endif
"""
  PathBuilder.create_file(config.name, config.path, FileTypes.ENVIRONMENT, output)
