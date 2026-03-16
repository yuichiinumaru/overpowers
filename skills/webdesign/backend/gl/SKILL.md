---
name: bmap-jsapi-gl
description: "Baidu Maps JSAPI WebGL (BMapGL) Development Guide. This skill should be applied when writing, reviewing, or debugging code that uses the Baidu Maps API. It is suitable for tasks involving map initialization, overlay rendering, layer management, event handling, control interaction, or performance optimization. Automatically triggered when the user mentions BMapGL, Baidu Maps, jsapi-gl, or related map development needs."
metadata:
  openclaw:
    category: "api"
    tags: ['api', 'development', 'integration']
    version: "1.0.0"
---

# JSAPI GL Development Guide

Baidu Maps JSAPI WebGL version development guide. It includes API descriptions and code examples for core modules such as map initialization, overlays, events, and layers, aiming to help developers quickly integrate Baidu Maps and follow correct usage methods.

## When to Use

Refer to these guides in the following scenarios:

- Creating new map pages or components
- Adding markers, polylines, polygons, and other overlays on the map
- Handling map interaction events (click, drag, zoom, etc.)
- Configuring map styles or switching layers
- Debugging map rendering or performance issues

## Quick Reference

### 0. Basic Concepts

- `references/base-classes.md` - Base classes: Point, Bounds, Size, Pixel, Icon
- `references/constants.md` - Common constants: search status codes, POI types

### 1. Map

- `references/map-init.md` - Map initialization: resource import, instance creation, configuration options, interaction and view control

### 2. Map Overlays

- `references/overlay-common.md` - Common overlay operations: add/remove, show/hide, batch clear
- `references/marker.md` - Point marker: constructor parameters, position/icon/rotation/bringToTop/drag methods
- `references/polyline.md` - Polyline: constructor parameters, line styles, coordinate operations, editing mode
- `references/polygon.md` - Polygon: constructor parameters, border/fill styles, polygons with holes, editing mode
- `references/circle.md` - Circle: constructor parameters, center point/radius, style settings, editing mode
- `references/custom-overlay.md` - Custom overlay: DOM creation, attribute passing, event binding, rotation control
- `references/info-window.md` - Info window: constructor parameters, content/size settings, maximize, usage with Marker

### 3. Events

- `references/map-events.md` - Map events: binding methods, interaction events, view change events, lifecycle events
- `references/overlay-events.md` - Overlay events: common events, drag events, vector graphic events

### 4. Map Styles

- `references/map-style.md` - Personalized maps: customize map appearance (color, visibility), achieve dark themes, minimalist maps, etc.

### 5. Layer Services

- `references/xyz-layer.md` - Third-party layers: load XYZ/TMS/WMS/WMTS standard tiles
- `references/mvt-layer.md` - Vector tiles: load MVT/PBF format tiles, support style expressions, feature interaction, state management

### 6. Route Planning

- `references/route-common.md` - Common configuration: constructor parameters, rendering options, callback functions, data structures, status constants
  - `references/driving-route.md` - Driving: policy enumeration, waypoints, traffic conditions, tolls, dragging
  - `references/walking-route.md` - Walking: turn types, dragging
  - `references/riding-route.md` - Riding: cycling search
  - `references/transit-route.md` - Public transit: intra-city/inter-city policies, modes of transport, transfers

### 7. Other LBS Services

- `references/local-search.md` - Local search: general/bound/nearby search, result processing, pagination, POI data structure
- `references/geocoder.md` - Geocoding: forward geocoding (address → coordinates), reverse geocoding (coordinates → address)
- `references/convertor.md` - Coordinate conversion: GPS/Gaode/Google coordinates to Baidu coordinates

## How to Use

Please read each reference file for detailed instructions and code examples:

```
references/map-init.md
```

Each reference file contains:

- Brief functional description
- Complete code examples and explanations
- API parameter descriptions and notes
