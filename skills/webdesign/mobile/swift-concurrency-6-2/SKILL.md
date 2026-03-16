---
name: dev-ios-swift-concurrency-6-2
description: "Swift 6.2 Approachable Concurrency patterns: default single-threaded, explicit offloading with @concurrent, and isolated conformance for MainActor types."
tags:
  - swift
  - ios
  - concurrency
  - xcode-26
version: 1.0.0
---

# Swift 6.2 Approachable Concurrency

Adopt the Swift 6.2 concurrency model where code runs on a single thread by default, and concurrency is explicitly introduced. Eliminate common data race bugs without sacrificing performance.

## When to Enable

* Migrating a Swift 5.x or 6.0/6.1 project to Swift 6.2
* Addressing data race safety compiler errors
* Designing an app architecture based on the MainActor
* Offloading CPU-intensive work to background threads
* Implementing protocol conformance on MainActor-isolated types
* Enabling the "Approachable Concurrency" build setting in Xcode 26

## Core Problem: Implicit Background Offloading

In Swift 6.1 and earlier, async functions could be implicitly offloaded to background threads, leading to data race bugs even in seemingly safe code:

```swift
// Swift 6.1: ERROR
@MainActor
final class StickerModel {
    let photoProcessor = PhotoProcessor()

    func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
        guard let data = try await item.loadTransferable(type: Data.self) else { return nil }

        // Error: Sending 'self.photoProcessor' risks causing data races
        return await photoProcessor.extractSticker(data: data, with: item.itemIdentifier)
    }
}
```

Swift 6.2 fixes this: async functions remain on the caller's actor by default.

```swift
// Swift 6.2: OK — async stays on MainActor, no data race
@MainActor
final class StickerModel {
    let photoProcessor = PhotoProcessor()

    func extractSticker(_ item: PhotosPickerItem) async throws -> Sticker? {
        guard let data = try await item.loadTransferable(type: Data.self) else { return nil }
        return await photoProcessor.extractSticker(data: data, with: item.itemIdentifier)
    }
}
```

## Core Pattern — Isolated Conformance

MainActor types can now safely conform to non-isolated protocols:

```swift
protocol Exportable {
    func export()
}

// Swift 6.1: ERROR — crosses into main actor-isolated code
// Swift 6.2: OK with isolated conformance
extension StickerModel: @MainActor Exportable {
    func export() {
        photoProcessor.exportAsPNG()
    }
}
```

The compiler ensures this conformance is only used on the main actor:

```swift
// OK — ImageExporter is also @MainActor
@MainActor
struct ImageExporter {
    var items: [any Exportable]

    mutating func add(_ item: StickerModel) {
        items.append(item)  // Safe: same actor isolation
    }
}

// ERROR — nonisolated context can't use MainActor conformance
nonisolated struct ImageExporter {
    var items: [any Exportable]

    mutating func add(_ item: StickerModel) {
        items.append(item)  // Error: Main actor-isolated conformance cannot be used here
    }
}
```

## Core Pattern — Global and Static Variables

Protect global/static state with the MainActor:

```swift
// Swift 6.1: ERROR — non-Sendable type may have shared mutable state
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // Error
}

// Fix: Annotate with @MainActor
@MainActor
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // OK
}
```

### MainActor Default Inference Pattern

Swift 6.2 introduces a pattern to infer MainActor by default — no manual annotation needed:

```swift
// With MainActor default inference enabled:
final class StickerLibrary {
    static let shared: StickerLibrary = .init()  // Implicitly @MainActor
}

final class StickerModel {
    let photoProcessor: PhotoProcessor
    var selection: [PhotosPickerItem]  // Implicitly @MainActor
}

extension StickerModel: Exportable {  // Implicitly @MainActor conformance
    func export() {
        photoProcessor.exportAsPNG()
    }
}
```

This pattern is opt-in and recommended for app, script, and other executable targets.

## Core Pattern — Background Work with @concurrent

When true parallelism is needed, explicitly offload with `@concurrent`:

> **Important:** This example requires the "Approachable Concurrency" build setting to be enabled — SE-0466 (MainActor Default Isolation) and SE-0461 (Default Non-Isolated Non-Sendable). With these settings enabled, `extractSticker` stays on the caller's actor, making access to mutable state safe. **Without these settings, this code has data races** — the compiler will flag it.

```swift
nonisolated final class PhotoProcessor {
    private var cachedStickers: [String: Sticker] = [:]

    func extractSticker(data: Data, with id: String) async -> Sticker {
        if let sticker = cachedStickers[id] {
            return sticker
        }

        let sticker = await Self.extractSubject(from: data)
        cachedStickers[id] = sticker
        return sticker
    }

    // Offload expensive work to concurrent thread pool
    @concurrent
    static func extractSubject(from data: Data) async -> Sticker { /* ... */ }
}

// Callers must await
let processor = PhotoProcessor()
processedPhotos[item.id] = await processor.extractSticker(data: data, with: item.id)
```

To use `@concurrent`:

1. Mark the containing type as `nonisolated`
2. Add `@concurrent` to the function
3. Add `async` if the function isn't already asynchronous
4. Add `await` at the call site

## Key Design Decisions

| Decision | Principle |
|----------|-----------|
| Default single-threaded | Most natural code is data-race free; concurrency is opt-in |
| Async functions stay on caller's actor | Eliminates implicit offloading that causes data race bugs |
| Isolated conformance | MainActor types can conform to protocols without unsafe workarounds |
| `@concurrent` explicitly opt-in | Background execution is an intentional performance choice, not an accident |
| MainActor default inference | Reduces boilerplate `@MainActor` annotations in app targets |
| Opt-in adoption | Non-disruptive migration path — enable features incrementally |

## Migration Steps

1. **Enable in Xcode**: Swift Compiler > Concurrency section in Build Settings
2. **Enable in SPM**: Use the `SwiftSettings` API in your Package.swift
3. **Use migration tools**: Automatic code changes via swift.org/migration
4. **Start with MainActor defaults**: Enable inference mode for app targets
5. **Add `@concurrent` where needed**: Profile performance first, then offload hot paths
6. **Test thoroughly**: Data race issues become compile-time errors

## Best Practices

* **Start with MainActor** — write single-threaded code first, optimize later
* **Use `@concurrent` only for CPU-intensive work** — image processing, compression, complex computations
* **Enable MainActor inference mode for primarily single-threaded app targets**
* **Profile before offloading** — use Instruments to find actual bottlenecks
* **Protect global variables with MainActor** — global/static mutable state needs actor isolation
* **Use isolated conformance**, not `nonisolated` workarounds or `@Sendable` wrappers
* **Migrate incrementally** — enable one feature at a time in build settings

## Anti-Patterns to Avoid

* Applying `@concurrent` to every async function (most don't need background execution)
* Using `nonisolated` to suppress compiler errors without understanding isolation
* Retaining legacy `DispatchQueue` patterns when actors provide the same safety
* Skipping `model.availability` checks in concurrency-related Foundation Models code
* Fighting the compiler — if it reports a data race, the code has a real concurrency issue
* Assuming all async code runs in the background (Swift 6.2 default: stays on caller's actor)

## When to Use

* All new Swift 6.2+ projects ("Approachable Concurrency" is the recommended default)
* Migrating existing apps from Swift 5.x or 6.0/6.1 concurrency
* Addressing data race safety compiler errors while adopting Xcode 26
* Building MainActor-centric app architectures (most UI apps)
* Performance optimization — offloading specific heavy computations to the background
