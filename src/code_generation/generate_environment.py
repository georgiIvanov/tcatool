from path_builder import PathBuilder
from models.file_types import FileTypes

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
  PathBuilder.create_file(name, path, FileTypes.ENVIRONMENT, str)