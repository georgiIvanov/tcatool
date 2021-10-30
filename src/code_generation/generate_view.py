from src.path_builder import PathBuilder
from src.models.file_types import FileTypes

def generate_view(name, path):
  str = f"""import SwiftUI
import ComposableArchitecture

public struct {name}View: View {{
    let store: Store<{name}State, {name}Action>
    @ObservedObject var viewStore: ViewStore<{name}State, {name}Action>

    public init(_ store: Store<{name}State, {name}Action>) {{
        self.store = store
        self.viewStore = ViewStore(store)
    }}

    public var body: some View {{

    }}
}}

#if DEBUG

struct {name}View_Previews: PreviewProvider {{
    static var previews: some View {{
        return {name}View(
            .init(
                initialState: .init(),
                reducer: {name.lower()}Reducer,
                environment: .noop
            )
        )
            
    }}
}}

#endif
"""
  PathBuilder.create_file(name, path, FileTypes.VIEW, str)