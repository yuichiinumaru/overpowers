---
name: amap-jsapi-skill
description: "Gaode Maps JSAPI v2.0 (WebGL) development skill. Covers map lifecycle management, forced security configuration, 3D view control, overlay drawing, and LBS service integration."
metadata:
  openclaw:
    category: "api"
    tags: ['api', 'development', 'integration']
    version: "1.0.0"
---

# Gaode Maps JSAPI v2.0 Development Skills
This guide contains API descriptions and code examples for core modules such as map initialization, overlays, events, and layers, aiming to help developers quickly integrate Gaode Maps and follow correct usage practices.
## Quick Start
### 1. Load the Loader
Use a script tag to load loader.js:
```bash
<script src="https://webapi.amap.com/loader.js"></script>
```
### 2. Security Key Configuration (Mandatory)
**Important**: Starting from v2.0, you must configure a security key before loading the map, otherwise, authentication will fail. For details and backend proxy examples, please refer to [Security Policy](references/security.md).
```javascript
// Execute before calling AMapLoader.load
window._AMapSecurityConfig = {
  securityJsCode: 'Your Security Key', // Development environment: set in plain text
  // serviceHost: 'https://your-proxy-domain/_AMapService', // Production environment: proxy forwarding is recommended
};
```
### 3. Initialize the Map
```javascript
import AMapLoader from '@amap/amap-jsapi-loader';
AMapLoader.load({
    key: 'Your Web Developer Key', // Required
    version: '2.0',           // Specify version
    plugins: ['AMap.Scale', 'AMap.ToolBar'] // Preload plugins
}).then((AMap) => {
    const map = new AMap.Map('container', {
        viewMode: '3D',       // Enable 3D view
        zoom: 11,             // Initial zoom level
        center: [116.39, 39.90] // Initial center point
    });
    map.addControl(new AMap.Scale());
}).catch(e => console.error(e));
```
## Scenario Examples
### Map Control
- **Lifecycle** : `references/map-init.md` - Master the `load`, `Map` instance creation, and `destroy` process.
- **View Interaction** : `references/view-control.md` - Control `zoom`, `center` (pan), `pitch`, and `rotation`.
### Overlay Drawing
- **Markers** : `references/marker.md` - Use `Marker` (basic) and `LabelMarker` (mass avoidance) to mark locations.
- **Vector Graphics** : `references/vector-graphics.md` - Draw `Polyline` (paths, lines), `Polygon` (areas, polygons), and `Circle` (ranges, circles).
- **Information Display** : `references/info-window.md` - Display detailed information via `InfoWindow`.
- **Context Menu** : `references/context-menu.md` - Customize right-click interactions for the map or overlays.
### Layer Management
- **Base Layers** : `references/layers.md` - Standard, satellite, road network, and 3D building layers.
- **Custom Data** : `references/custom-layers.md` - Integrate `Canvas`, `WMS/WMTS`, and `GLCustomLayer` to overlay Canvas, WMS layers, and Three.js layers on the map.
### Services and Plugins
- **LBS Services** :
    - `references/geocoder.md` - Geocoding/Reverse Geocoding (address/coordinate conversion).
    - `references/routing.md` - Route planning (driving/walking/transit).
    - `references/search.md` - POI search and input suggestions.
- **Event System** : `references/events.md` - Respond to interaction events such as clicks, drags, and zooms.
## Best Practices
1. **Safety First**: In production environments, always use a proxy server to forward `serviceHost` to avoid `securityJsCode` leakage.
2. **Load on Demand**: Declare only the necessary plugins in `plugins` to reduce the initial load size.
3. **Resource Release**: Always call `map.destroy()` when a component is unmounted to prevent WebGL context memory leaks.

## API Reference

JSAPI documentation is divided into the following categories:

### [Foundation Classes](references/api/foundation.md)
LngLat / Bounds / Pixel / Size

### [Information Window](references/api/info-window.md)
InfoWindow

### [Events](references/api/events.md)
Event

### [Map](references/api/map.md)
Map / MapsEvent

### [Official Layers](references/api/layers-official.md)
TileLayer / Traffic / Satellite / RoadNet / Buildings / DistrictLayer / IndoorMap

### [Standard Layers](references/api/layers-standard.md)
WMS / WMTS / MapboxVectorTileLayer

### [Custom Layers](references/api/layers-custom.md)
HeatMap / VectorLayer / LabelsLayer / CustomLayer / Flexible / ImageLayer / CanvasLayer / GLCustomLayer

### [Markers](references/api/marker.md)
Marker / Text / Icon / LabelMarker / ElasticMarker / MarkerCluster / MassMarks / MoveAnimation / AnimationCallback / EasingCallback

### [Context Menu](references/api/context-menu.md)
ContextMenu

### [Vector Graphics](references/api/vector-graphics.md)
Polygon / Polyline / BezierCurve / Circle / CircleMarker / Ellipse / Rectangle / GeoJSON

### [Overlay Groups](references/api/overlay-group.md)
LayerGroup / OverlayGroup

### [Controls](references/api/controls.md)
Control / Scale / ToolBar / ControlBar / MapType / HawkEye

### [Tools](references/api/tools.md)
RangingTool / MouseTool / PolygonEditor / PolylineEditor / CircleEditor / BezierCurveEditor / EllipseEditor / RectangleEditor

### [Services](references/api/services.md)
WebService / WebServiceCallback

### [Search](references/api/search.md)
AutoComplete / AutoCompleteSearchCallback / PlaceSearch / searchCallback / CloudDataSearch / CloudDataSearchCallback

### [Geocoder](references/api/geocoder.md)
Geocoder / GeocoderCallback / ReGeocoderCallback / convertFrom

### [Routing](references/api/routing.md)
Driving / DrivingCallback / DrivingResult / DriveStepBasic / DriveStepDetail / TruckDriving / Walking / WalkingCallback / WalkingResult / Transfer / TransferCallback / TransferResult / Riding / RidingCallback / RidingResult / DragRoute / DragRouteTruck / GraspRoad / GraspRoadCallback

### [Other Services](references/api/services-other.md)
DistrictSearch / Weather / WeatherLiveResult / WeatherForecastResult / StationSearch / LineSearch

### [Geolocation](references/api/geolocation.md)
Geolocation / GeolocationCallBack / GeolocationResult / CitySearch

### [Common Library](references/api/common.md)
GeometryUtil / DomUtil / Browser / Util

## Iron Rules to Follow When Using Skills
1. **Validate Generated Code Availability**: After generating code, you must self-validate to ensure the code is syntactically correct, logically complete, and can run properly. Outputting unverified code is prohibited.
2. **Local File Placement Specification**: All generated project files must be placed in the `amap-jsapi/` folder within the openclaw workspace directory. File names must consistently use kebab-case (e.g., `map-init.html`, `layers-official.html`).
## How to Use
1. If there are similar "Scenario Examples," read them first, then read the API documentation for the classes involved in those examples. Finally, complete the task by combining the description, scenario examples, and APIs.
2. Before finalizing the task, check if the API usage conforms to the documentation.
