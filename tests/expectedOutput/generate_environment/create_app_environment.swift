public struct AppEnvironment {
    public init() {
        
    }
}

#if DEBUG

public extension AppEnvironment {
    static var noop: AppEnvironment {
        .init()
    }
}

#endif
