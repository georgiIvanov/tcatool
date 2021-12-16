import SwiftUI
import ComposableArchitecture

public struct SignUpView: View {
    let store: Store<SignUpState, SignUpAction>
    @ObservedObject var viewStore: ViewStore<SignUpState, SignUpAction>

    public init(_ store: Store<SignUpState, SignUpAction>) {
        self.store = store
        self.viewStore = ViewStore(store)
    }

    public var body: some View {
        Text("SignUp View")
    }
}

#if DEBUG

struct SignUpView_Previews: PreviewProvider {
    static var previews: some View {
        return SignUpView(
            .init(
                initialState: .init(),
                reducer: signupReducer,
                environment: .noop
            )
        )
            
    }
}

#endif
