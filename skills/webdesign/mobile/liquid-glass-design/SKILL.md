---
name: design-ux-liquid-glass-design
description: iOS 26 Liquid Glass Design System — Dynamic glass materials for SwiftUI, UIKit, and WidgetKit, with blur, reflection, and interactive deformation effects.
tags: [design, ux, ios, swiftui, liquid-glass]
version: 1.0.0
---

# Liquid Glass Design System (iOS 26)

Guidelines for implementing Apple's Liquid Glass pattern—a dynamic material that blurs content behind it, reflects the colors and light of surrounding content, and reacts to touch and pointer interactions. Covers SwiftUI, UIKit, and WidgetKit integration.

## When to Enable

* When building or updating an app for iOS 26+ that adopts the new design language
* When implementing glass-styled buttons, cards, toolbars, or containers
* When creating morphing transitions between glass elements
* When applying Liquid Glass effects to widgets
* When migrating existing blur/material effects to the new Liquid Glass API

## Core Patterns — SwiftUI

### Basic Glass Effect

The simplest way to add Liquid Glass to any view:

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()  // Default: regular variant, capsule shape
```

### Custom Shapes and Tints

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect(.regular.tint(.orange).interactive(), in: .rect(cornerRadius: 16.0))
```

Key customization options:

* `.regular` — Standard glass effect
* `.tint(Color)` — Adds a color tint to enhance prominence
* `.interactive()` — Reacts to touch and pointer interactions
* Shapes: `.capsule` (default), `.rect(cornerRadius:)`, `.circle`

### Glass Button Styles

```swift
Button("Click Me") { /* action */ }
    .buttonStyle(.glass)

Button("Important") { /* action */ }
    .buttonStyle(.glassProminent)
```

### GlassEffectContainer for Multiple Elements

For performance and morphing considerations, always wrap multiple glass views in a container:

```swift
GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()

        Image(systemName: "eraser.fill")
            .frame(width: 80.0, height: 80.0)
            .font(.system(size: 36))
            .glassEffect()
    }
}
```

The `spacing` parameter controls the merge distance—elements closer together will blend their glass shapes.

### Unified Glass Effect

Combine multiple views into a single glass shape using `glassEffectUnion`:

```swift
@Namespace private var namespace

GlassEffectContainer(spacing: 20.0) {
    HStack(spacing: 20.0) {
        ForEach(symbolSet.indices, id: \.self) { item in
            Image(systemName: symbolSet[item])
                .frame(width: 80.0, height: 80.0)
                .glassEffect()
                .glassEffectUnion(id: item < 2 ? "group1" : "group2", namespace: namespace)
        }
    }
}
```

### Morphing Transitions

Create smooth morphing effects as glass elements appear/disappear:

```swift
@State private var isExpanded = false
@Namespace private var namespace

GlassEffectContainer(spacing: 40.0) {
    HStack(spacing: 40.0) {
        Image(systemName: "scribble.variable")
            .frame(width: 80.0, height: 80.0)
            .glassEffect()
            .glassEffectID("pencil", in: namespace)

        if isExpanded {
            Image(systemName: "eraser.fill")
                .frame(width: 80.0, height: 80.0)
                .glassEffect()
                .glassEffectID("eraser", in: namespace)
        }
    }
}

Button("Toggle") {
    withAnimation { isExpanded.toggle() }
}
.buttonStyle(.glass)
```

### Extending Horizontal Scrolling Under Sidebars

To allow horizontal scrolling content to extend under sidebars or inspectors, ensure the `ScrollView` content reaches the leading/trailing edges of its container. The system automatically handles scrolling behavior under sidebars when the layout extends to the edge—no additional modifiers are needed.

## Core Patterns — UIKit

### Basic UIGlassEffect

```swift
let glassEffect = UIGlassEffect()
glassEffect.tintColor = UIColor.systemBlue.withAlphaComponent(0.3)
glassEffect.isInteractive = true

let visualEffectView = UIVisualEffectView(effect: glassEffect)
visualEffectView.translatesAutoresizingMaskIntoConstraints = false
visualEffectView.layer.cornerRadius = 20
visualEffectView.clipsToBounds = true

view.addSubview(visualEffectView)
NSLayoutConstraint.activate([
    visualEffectView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
    visualEffectView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
    visualEffectView.widthAnchor.constraint(equalToConstant: 200),
    visualEffectView.heightAnchor.constraint(equalToConstant: 120)
])

// Add content to contentView
let label = UILabel()
label.text = "Liquid Glass"
label.translatesAutoresizingMaskIntoConstraints = false
visualEffectView.contentView.addSubview(label)
NSLayoutConstraint.activate([
    label.centerXAnchor.constraint(equalTo: visualEffectView.contentView.centerXAnchor),
    label.centerYAnchor.constraint(equalTo: visualEffectView.contentView.centerYAnchor)
])
```

### UIGlassContainerEffect for Multiple Elements

```swift
let containerEffect = UIGlassContainerEffect()
containerEffect.spacing = 40.0

let containerView = UIVisualEffectView(effect: containerEffect)

let firstGlass = UIVisualEffectView(effect: UIGlassEffect())
let secondGlass = UIVisualEffectView(effect: UIGlassEffect())

containerView.contentView.addSubview(firstGlass)
containerView.contentView.addSubview(secondGlass)
```

### Scroll Edge Effects

```swift
scrollView.topEdgeEffect.style = .automatic
scrollView.bottomEdgeEffect.style = .hard
scrollView.leftEdgeEffect.isHidden = true
```

### Toolbar Glass Integration

```swift
let favoriteButton = UIBarButtonItem(image: UIImage(systemName: "heart"), style: .plain, target: self, action: #selector(favoriteAction))
favoriteButton.hidesSharedBackground = true  // Opt out of shared glass background
```

## Core Patterns — WidgetKit

### Rendering Mode Detection

```swift
struct MyWidgetView: View {
    @Environment(\.widgetRenderingMode) var renderingMode

    var body: some View {
        if renderingMode == .accented {
            // Tinted mode: white-tinted, themed glass background
        } else {
            // Full color mode: standard appearance
        }
    }
}
```

### Accentable Groups for Visual Hierarchy

```swift
HStack {
    VStack(alignment: .leading) {
        Text("Title")
            .widgetAccentable()  // Accent group
        Text("Subtitle")
            // Primary group (default)
    }
    Image(systemName: "star.fill")
        .widgetAccentable()  // Accent group
}
```

### Image Rendering in Accent Mode

```swift
Image("myImage")
    .widgetAccentedRenderingMode(.monochrome)
```

### Container Background

```swift
VStack { /* content */ }
    .containerBackground(for: .widget) {
        Color.blue.opacity(0.2)
    }
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Wrap with GlassEffectContainer | Performance optimization, enables morphing between glass elements |
| `spacing` parameter | Controls merge distance—how close elements need to be to blend |
| `@Namespace` + `glassEffectID` | Enables smooth morphing transitions when view hierarchy changes |
| `interactive()` modifier | Explicit opt-in for touch/pointer reactions—not all glass should respond |
| UIGlassContainerEffect in UIKit | Consistent container pattern with SwiftUI |
| Accentable rendering mode in widgets | System applies tinted glass when user opts into a tinted Home Screen |

## Best Practices

* **Always use GlassEffectContainer** for applying glass effects to multiple sibling views—it supports morphing and improves rendering performance
* **Apply `.glassEffect()` after other appearance modifiers** (frame, font, padding)
* **Use `.interactive()` only on elements that respond to user interaction** (buttons, toggles)
* **Choose spacing within containers carefully** to control when glass effects merge
* **Use `withAnimation`** when changing view hierarchy to enable smooth morphing transitions
* **Test across various appearance modes**—Light, Dark, and Accent/Tinted modes
* **Ensure accessibility contrast**—text on glass must remain readable

## Anti-Patterns to Avoid

* Using multiple independent `.glassEffect()` views without a GlassEffectContainer
* Nesting glass effects too deeply—reduces performance and visual clarity
* Applying glass effects to every view—reserve for interactive elements, toolbars, and cards
* Forgetting `clipsToBounds = true` when using corner radius in UIKit
* Ignoring accentable rendering mode in widgets—breaks tinted Home Screen appearance
* Using opaque backgrounds behind glass effects—defeats the translucent effect

## Use Cases

* Navigation bars, toolbars, and tab bars adopting the new iOS 26 design
* Floating action buttons and card-based containers
* Interactive controls requiring visual depth and touch feedback
* Widgets that should integrate with the system Liquid Glass appearance
* Morphing transitions between related UI states
