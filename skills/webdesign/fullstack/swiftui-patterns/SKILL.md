---
name: dev-ios-swiftui-patterns
description: "Modern SwiftUI architecture patterns including @Observable state management, view composition, type-safe navigation, and performance optimization."
tags:
  - swiftui
  - ios
  - architecture
  - macos
version: 1.0.0
---

# SwiftUI Patterns

Modern SwiftUI patterns for Apple platforms, for building declarative, high-performance user interfaces. Covers the Observation framework, view composition, type-safe navigation, and performance optimizations.

## When to Activate

* When building SwiftUI views and managing state (`@State`, `@Observable`, `@Binding`)
* When designing navigation flows with `NavigationStack`
* When building ViewModels and data flow
* When optimizing rendering performance for lists and complex layouts
* When using environment values and dependency injection in SwiftUI

## State Management

### Property Wrapper Selection

Choose the simplest wrapper that fits best:

| Wrapper | Use Case |
|---------|----------|
| `@State` | View-local value types (toggles, form fields, sheet presentation) |
| `@Binding` | Bidirectional reference to a parent view's `@State` |
| `@Observable` class + `@State` | Owned model with multiple properties |
| `@Observable` class (no wrapper) | Read-only reference passed from a parent view |
| `@Bindable` | Bidirectional binding to an `@Observable` property |
| `@Environment` | Shared dependency injected via `.environment()` |

### @Observable ViewModel

Use `@Observable` (instead of `ObservableObject`)—it tracks changes at the property level, so SwiftUI only re-renders views that read the changed property:

```swift
@Observable
final class ItemListViewModel {
    private(set) var items: [Item] = []
    private(set) var isLoading = false
    var searchText = ""

    private let repository: any ItemRepository

    init(repository: any ItemRepository = DefaultItemRepository()) {
        self.repository = repository
    }

    func load() async {
        isLoading = true
        defer { isLoading = false }
        items = (try? await repository.fetchAll()) ?? []
    }
}
```

### View Consuming ViewModel

```swift
struct ItemListView: View {
    @State private var viewModel: ItemListViewModel

    init(viewModel: ItemListViewModel = ItemListViewModel()) {
        _viewModel = State(initialValue: viewModel)
    }

    var body: some View {
        List(viewModel.items) { item in
            ItemRow(item: item)
        }
        .searchable(text: $viewModel.searchText)
        .overlay { if viewModel.isLoading { ProgressView() } }
        .task { await viewModel.load() }
    }
}
```

### Environment Injection

Replace `@EnvironmentObject` with `@Environment`:

```swift
// Inject
ContentView()
    .environment(authManager)

// Consume
struct ProfileView: View {
    @Environment(AuthManager.self) private var auth

    var body: some View {
        Text(auth.currentUser?.name ?? "Guest")
    }
}
```

## View Composition

### Extract Subviews to Limit Invalidation

Break views into small, focused structs. When state changes, only the child views that read that state re-render:

```swift
struct OrderView: View {
    @State private var viewModel = OrderViewModel()

    var body: some View {
        VStack {
            OrderHeader(title: viewModel.title)
            OrderItemList(items: viewModel.items)
            OrderTotal(total: viewModel.total)
        }
    }
}
```

### ViewModifier for Reusable Styles

```swift
struct CardModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding()
            .background(.regularMaterial)
            .clipShape(RoundedRectangle(cornerRadius: 12))
    }
}

extension View {
    func cardStyle() -> some View {
        modifier(CardModifier())
    }
}
```

## Navigation

### Type-Safe NavigationStack

Use `NavigationStack` with `NavigationPath` for programmatic, type-safe routing:

```swift
@Observable
final class Router {
    var path = NavigationPath()

    func navigate(to destination: Destination) {
        path.append(destination)
    }

    func popToRoot() {
        path = NavigationPath()
    }
}

enum Destination: Hashable {
    case detail(Item.ID)
    case settings
    case profile(User.ID)
}

struct RootView: View {
    @State private var router = Router()

    var body: some View {
        NavigationStack(path: $router.path) {
            HomeView()
                .navigationDestination(for: Destination.self) { dest in
                    switch dest {
                    case .detail(let id): ItemDetailView(itemID: id)
                    case .settings: SettingsView()
                    case .profile(let id): ProfileView(userID: id)
                    }
                }
        }
        .environment(router)
    }
}
```

## Performance

### Use Lazy Containers for Large Collections

`LazyVStack` and `LazyHStack` only create their views when they are visible:

```swift
ScrollView {
    LazyVStack(spacing: 8) {
        ForEach(items) { item in
            ItemRow(item: item)
        }
    }
}
```

### Stable Identifiers

Always use stable, unique IDs in `ForEach`—avoid array indices:

```swift
// Use Identifiable conformance or explicit id
ForEach(items, id: \.stableID) { item in
    ItemRow(item: item)
}
```

### Avoid Expensive Operations in `body`

* Never perform I/O, network calls, or heavy computations inside `body`
* Use `.task {}` for asynchronous work—it cancels automatically when the view disappears
* Use `.sensoryFeedback()` and `.geometryGroup()` judiciously within scroll views
* Minimize `.shadow()`, `.blur()`, and `.mask()` in lists—they trigger offscreen rendering

### Conform to Equatable

For views with expensive body calculations, conform to `Equatable` to skip unnecessary re-renders:

```swift
struct ExpensiveChartView: View, Equatable {
    let dataPoints: [DataPoint] // DataPoint must conform to Equatable

    static func == (lhs: Self, rhs: Self) -> Bool {
        lhs.dataPoints == rhs.dataPoints
    }

    var body: some View {
        // Complex chart rendering
    }
}
```

## Previews

Use the `#Preview` macro with inline mock data for rapid iteration:

```swift
#Preview("Empty state") {
    ItemListView(viewModel: ItemListViewModel(repository: EmptyMockRepository()))
}

#Preview("Loaded") {
    ItemListView(viewModel: ItemListViewModel(repository: PopulatedMockRepository()))
}
```

## Anti-Patterns to Avoid

* Using `ObservableObject` / `@Published` / `@StateObject` / `@EnvironmentObject` in new code—migrate to `@Observable`
* Placing asynchronous work directly in `body` or `init`—use `.task {}` or explicit loading methods
* Creating ViewModels with `@State` in child views that don't own the data—pass them from the parent instead
* Using `AnyView` for type erasure—prefer `@ViewBuilder` or `Group` for conditional views
* Ignoring `Sendable` requirements when passing data to or receiving data from Actors

## References

Check out `swift-actor-persistence` for Actor-based persistence patterns.
Check out `swift-protocol-di-testing` for Protocol-based DI and testing with Swift Testing.
