from utilities.path_builder import PathBuilder
from models.file_types import FileTypes
from models.gen_config import GenConfig

def generate_view(config: GenConfig):
  if config.no_view():
    return

  output = f"""import SwiftUI
import ComposableArchitecture

public struct {config.name}View: View {{
    let store: Store<{config.name}State, {config.name}Action>
    @ObservedObject var viewStore: ViewStore<{config.name}State, {config.name}Action>

    public init(_ store: Store<{config.name}State, {config.name}Action>) {{
        self.store = store
        self.viewStore = ViewStore(store)
    }}

    public var body: some View {{

    }}
}}

#if DEBUG

struct {config.name}View_Previews: PreviewProvider {{
    static var previews: some View {{
        return {config.name}View(
            .init(
                initialState: .init(),
                reducer: {config.name.lower()}Reducer,
                environment: .noop
            )
        )
            
    }}
}}

#endif
"""
  PathBuilder.create_file(config.name, config.path, FileTypes.VIEW, output)
