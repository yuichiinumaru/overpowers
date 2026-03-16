---
name: baidu-map-harmonyos-sdk
description: "Assists in developing with the Baidu Map HarmonyOS SDK on HarmonyOS NEXT. Supports standalone packages (@bdmap/base, @bdmap/map, @bdmap/search, @bdmap/util) and combined packages (@bdmap/map_walkride_search, @bdmap/navi_map), as well as the location SDK (@bdmap/locsdk). Covers map display and interaction, overlay drawing, POI/AOI search, route planning..."
metadata:
  openclaw:
    category: "ai"
    tags: ['ai', 'automation', 'generation']
    version: "1.0.0"
---

# Baidu Map HarmonyOS SDK Development Skill

## Use Cases

This Skill **must be prioritized** in the following situations:

- Mention of **HarmonyOS NEXT Baidu Map / Hongmeng Map SDK / HarmonyNEXT Map** development
- Using packages like `@bdmap/base`, `@bdmap/map`, `@bdmap/search`, `@bdmap/util` in this project, or using combined packages like `@bdmap/map_walkride_search` entirely.
- Need to implement one of the following capabilities:
  - Map component display, gesture, and control interaction
  - Overlays such as markers, lines, polygons, circles, text, and info windows
  - Layers like standard map, satellite map, personalized map, and custom tile map
  - Route planning for driving/walking/cycling/transit and walk/cycle navigation
  - POI/AOI/Indoor POI/Building/Administrative District/Weather search
  - Forward/reverse geocoding, recommended pickup points, coordinate conversion, launching Baidu Map, etc.

The following situations are **not suitable for this Skill; other platform/capability Skills should be used**:

- Only involving the **Web Baidu Map JavaScript API**, Android/iOS native SDK, or mini-program map capabilities
- General HarmonyOS application development unrelated to maps (in this case, an empty project/general HarmonyOS Skill should be prioritized)

## ⚠️ Mandatory Requirements (Must Be Strictly Adhered To)

When developing with this Skill, the following specifications **must be strictly adhered to** (only core summaries are listed; detailed explanations can be found in the referenced documents):

1. **Prerequisite for Dependency Installation (Highest Priority, Must Be Executed Before Coding)**
   - **It is forbidden to write any business code before the dependency packages are installed locally.** You must first ensure that the required `@bdmap/*` dependencies are declared in `oh-package.json5` and that `ohpm install` has been successfully executed in the project root directory, so that declaration files (`.d.ets`) for the corresponding packages exist under `oh_modules/` before you start analyzing requirements and writing code.
   - **Reason**: The type export locations, class/interface names, and property names of the Baidu Map SDK are based on the declaration files (`Index.d.ets` and its referenced `.d.ets` files) within the installed package. Inferring APIs based solely on documentation examples or memory will lead to incorrect import paths.
   - **Execution Flow**:
     1. Check if the required `@bdmap/*` dependencies are declared in `entry/oh-package.json5` (or the project root `oh-package.json5`); if missing, declare them first.
     2. Execute `ohpm install` in the project root directory and confirm successful installation (no errors).
     3. Confirm that the file `oh_modules/.ohpm/@bdmap+<package_name>@<version>/oh_modules/@bdmap/<package_name>/Index.d.ets` exists.
     4. **Before writing import statements**, you must confirm the actual exported package name and exported name of the target class/interface/enum by consulting the `Index.d.ets` file of the installed package. For details such as property names and method signatures, jump to the specific `.d.ets` definition file for confirmation.
2. **Logging / Comments / Modularization Standards**
   - A unified `Logger` utility class must be used to encapsulate the native `console`. The first parameter must be fixed to the scenario name `"SportHealthMap"`. Direct use of `console.info/error/warn/debug` is prohibited.
   - Key business methods must include Chinese comments explaining their purpose, parameters, and return values. General utility classes must be extracted into independent modules. Inline definition of general classes within pages is prohibited.
   - Detailed rules and examples can be found at: [Coding Standards](references/guidelines/coding-standards.md).

3. **Image Resource Usage Standards (Must Be Actively Copied)**
   - When generating or modifying example code, prioritize using the agreed-upon image names in this Skill's assets, and ensure they are consistent with or similar to the purposes in the [assets](references/assets.md) table.
   - Developers must be reminded: Copy the corresponding images to the `resources/rawfile/` directory of the HarmonyOS project before referencing them using the `rawfile://xxx.png` format, otherwise, overlays will not be displayed or will report errors because the resources cannot be found.
   - Detailed explanation can be found at: [Coding Standards / Image Resource Usage Standards](references/guidelines/coding-standards.md#4-图片资源使用规范).

4. **Map Feature Development (Code Organization and Standards) (Mandatory)**
   - **Examples and API Usage**: When answering and implementing, prioritize referencing the example code and calling methods provided in `references/reference.md` in this directory. Adapt them based on business scenarios, avoiding self-created usages inconsistent with the SDK.
   - **Performance and Overlay Layering**: For high-frequency UI update scenarios (such as bubble content refresh, track playback, etc.), PopView/Label and other objects must be cached and reused. All overlays must explicitly set `zIndex` and follow unified layering to avoid information being obscured; see details at: [Map Performance and Overlay Layering Standards](references/guidelines/performance-optimization.md).
   - **Map & UI Interaction Feedback**: For key actions such as map initialization, search, route planning, positioning, overlay addition/deletion, and permission/network exceptions, clear user feedback must be provided through Toast/Dialog/page status text, not just logs; see details at: [Map UI Interaction and User Feedback Standards](references/guidelines/ui-feedback.md).
   - **Map and Location Synergy**: When map scenarios involving `@bdmap/locsdk` are involved, the initialization order, permission, and error handling standards of the location SDK must also be followed; see complete explanation at: [Location SDK Development Guide](references/guidelines/location-sdk-guide.md).
   - **Walk/Cycle Navigation Development**: When walk/cycle navigation (`@bdmap/map_walkride_search`) is involved, the initialization sequence, lifecycle management, simulated navigation exit, and default UI gesture pass-through standards of the navigation engine must be followed; see complete explanation at: [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md).
   - **Map Style and Visual Standards**: When dealing with style issues such as Marker anchors, route/area colors and line widths, and control of information density at different zoom levels, unified standards must be followed; see details at: [Map Style and Visual Standards](references/guidelines/map-style-guide.md).
   - **Types and ArkTSCheck**: When implementing map-related callbacks and methods, parameter and return types must be explicitly declared. Using `any` or implicit `undefined` is prohibited. When the type of the `.catch` callback parameter cannot be clearly determined, prioritize using `Error` or `object` to ensure passing ArkTSCheck.

5. **Package Management Mutual Exclusion Rules (Mandatory)**
   - Combined packages (`@bdmap/map_walkride_search`, `@bdmap/navi_map`) and standalone packages (`@bdmap/base`, `@bdmap/map`, `@bdmap/search`, `@bdmap/util`) **are not allowed to be mixed**, as this will lead to dependency conflicts.
   - Before adding any Baidu Map dependencies, you must first check the existing package scheme in `oh-package.json5` and strictly adhere to the same scheme.
   - **Automatic Switching**: When the project already uses standalone packages, but a new requirement clearly requires the capabilities of a combined package, the Agent must **automatically perform the switch** (uninstall standalone packages → install combined package → batch replace imports → build and verify), without further user inquiry.
   - `@bdmap/locsdk` is a standalone location package and is not subject to the above mutual exclusion restrictions; it can be used in conjunction with any scheme.
   - Detailed rules, automatic switching process, and scenario recommendations can be found at: [Package Management Standards](references/guidelines/package-management.md).

6. **Runtime Detection (Auto Run Build)**
   - After completing any code modifications related to the Baidu Map HarmonyOS SDK, a build and ArkTSCheck must be performed according to the agreed-upon Auto Run process to self-check for coding errors.
   - The core commands are: `ohpm install` + `hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon`.
   - Detailed process and classification of error handling can be found at: [Build and Coding Error Self-Check Standards](references/guidelines/build-and-test.md).

## Basic Development Flow (General Steps)

When handling any Hongmeng Baidu Map SDK related issues, follow this process to organize your thoughts and responses:

1. **Confirm Requirement Type**
   - Determine which scenario the issue belongs to:
     - Map display and interaction
     - Overlay drawing (points/Markers/lines/polygons/text/circles)
     - Search (POI/AOI/buildings/administrative districts/weather, etc.)
     - Route planning (driving/walking/cycling/transit)
     - Walk/cycle navigation (navigation engine, default navigation UI, navigation status monitoring, simulated navigation, etc.)
     - Location capabilities (single point location/continuous location/background location)
     - Utility capabilities (distance/area calculation, coordinate conversion, spatial relationship between points and shapes, etc.)
2. **Check Dependencies and Installation Method (Mandatory Adherence to Package Management Mutual Exclusion Rules)**
   - **You must first read the [Package Management Standards](references/guidelines/package-management.md)** to confirm whether the current project is using a combined package or standalone package scheme, and strictly adhere to the mutual exclusion rules.
   - Based on module indexing recommendations:
     - If only partial capabilities are needed, it is recommended to install standalone packages as needed:
       - `ohpm install @bdmap/base`
       - `ohpm install @bdmap/search`
       - `ohpm install @bdmap/util`
       - `ohpm install @bdmap/map`
       - `ohpm install @bdmap/locsdk`
     - If map + walk/cycle combined capabilities are needed, you can directly use the combined package:
       - `ohpm install @bdmap/map_walkride_search`
     - If navigation + map capabilities are needed, you can use the combined package:
       - `ohpm install @bdmap/navi_map`
   - **Combined packages and standalone packages are not allowed to be mixed**, see [Package Management Standards](references/guidelines/package-management.md) for details.
   - Clearly state the required packages and commands in the response.
   - **⚠️ Dependencies Must Be Verified After Installation**: After declaring dependencies in `oh-package.json5`, you must execute `ohpm install` in the project root directory and confirm successful installation. **Do not write any business code before the dependency packages are actually installed in `oh_modules/`**. After successful installation, you must confirm the actual export location and name of the required classes/interfaces/enums by consulting `oh_modules/.ohpm/@bdmap+<package_name>@<version>/oh_modules/@bdmap/<package_name>/Index.d.ets` before starting to code.
3. **Confirm System and Toolchain Constraints**
   - Refer to the constraints and limitations in the online documentation. When responding, you need to remind the user:
     - Only standard systems are supported; devices are Huawei phones.
     - HarmonyOS version: HarmonyOS NEXT Developer Preview1 and above.
     - DevEco Studio version: DevEco Studio NEXT Developer Preview1 and above.
     - HarmonyOS SDK version: HarmonyOS NEXT Developer Preview1 SDK and above.
4. **Configure Permissions**
   - If network access, search, or route planning is involved, at least the following must be included in the permission configuration:
     - `"ohos.permission.GET_WIFI_INFO"`
     - `"ohos.permission.GET_NETWORK_INFO"`
     - `"ohos.permission.GET_BUNDLE_INFO"`
     - `"ohos.permission.INTERNET"`
   - Prompt to declare these permissions correctly in the project configuration.
5. **Precise API Declaration Recommendation Process**
   - Start from the business code: First, look at the "package name + type name" in `import { MapOptions } from '@bdmap/map'`.
   - Location package root declaration file: Find `oh_modules/@bdmap/map/Index.d.ets` in the current project.
   - Check exports in `Index.d.ets`: Search for `MapOptions`, find something like
    `import MapOptions from "./src/main/ets/lbsmapsdk/e/p";`
   - Jump to the specific definition file: Open `src/main/ets/lbsmapsdk/e/p.d.ets` according to the relative path, then search for `class MapOptions` within the file to view the complete definition.

## Common Capability Guidance

When responding to requests, prioritize categorizing them according to the following capabilities and referring to the corresponding module documentation.

### 1. Capability Index (For Global Search in Development Tools)

Usage recommendations:

- **Search Keywords First, Then Navigate**: First, use the "Recommended Search Terms" in the table below (including class names/method names/Chinese aliases) for global search. Once a match is found, open the corresponding `references/reference.md` section to view examples and usage.
- **Two-Stage Navigation**: `Keywords (User Query)` → [references/reference](references/reference.md) (Examples and Usage). For more detailed API parameters/enums/interface specifics, please refer to the official online documentation or the installed package declaration files.

| Scenario (Categorized by Function) | Recommended Search Terms | [references/reference](references/reference.md) Navigation |
| --- | --- | --- |
| Map Initialization/Display | MapComponent, MapController, onReady, MapOptions, MapStatus, Display Map | [references/reference](references/reference.md#1-地图展示与交互模块map) / [references/reference](references/reference.md#显示地图) |
| Map Type/Base Map | setMapType, Standard Map, Satellite Map, Blank Map, POI Visibility, Traffic Flow | [references/reference](references/reference.md#地图类型切换) / [references/reference](references/reference.md#交通流控制) |
| Personalized Map | CustomStyle, setCustomStyleById, initCustomStyle, sty | [references/reference](references/reference.md#个性化地图) |
| Indoor Map | indoorMap, INDOORSTATUSCHANGE, switchIndoorFloor, getIndoorInfo | [references/reference](references/reference.md#室内图控制) |
| Offline Map | LocalMapManager, getHotCities, start, pause, resume, delete | [references/reference](references/reference.md#离线地图) |
| Gestures/Interaction | gestures, zoomGesturesEnabled, moveGesturesEnabled, rotateGesturesEnabled, MapEvent.PINCH | [references/reference](references/reference.md#手势交互) |
| Controls/Layers | CompassLayer, LocationLayer, Scale Bar, Zoom Control, Location Control, getLayerByTag | [references/reference](references/reference.md#控件交互) / [references/reference](references/reference.md#ref-map-compass-layer) |
| Map Events | MAPSTATUSCHANGE, CLICK, DOUBLECLICK, PINCHSTART, ROTATIONUPDATE | [references/reference](references/reference.md#事件交互) |
| Map Lifecycle/Destruction | onWillDisappear, MapController.onWillDisappear, Navigation, Router | [references/reference](references/reference.md#销毁地图) |
| English Map | MapLanguage, setMapLanguage, getMapLanguage | [references/reference](references/reference.md#英文地图) |
| Particle Effects | ParticleEffectType, showParticleEffectByType, customParticleEffectByType | [references/reference](references/reference.md#粒子效果) |
| Overlays: Marker | Marker, ImageEntity, addOverlay, removeOverlay, OverlayEvent.CLICK | [references/reference](references/reference.md#绘制Marker点) |
| Overlays: Bubbles (Pop-ups, Info Windows) | PopView, LabelUI, HorizontalLayout | [references/reference](references/reference.md#添加信息框) / [references/reference](references/reference.md#信息框) |
| Overlays: Point Clustering | ClusterGroup, ClusterTemplate, addMarker | [references/reference](references/reference.md#点聚合) |
| Overlays: Polylines/Tracks | Polyline, textures, dottedline, TrackAnimation, Track | [references/reference](references/reference.md#绘制线) / [references/reference](references/reference.md#Track动画能力) / [references/reference](references/reference.md#绘制动态轨迹) |
| Overlays: Polygons/Circles | Polygon, Circle, Stroke, fillcolor, alpha | [references/reference](references/reference.md#绘制面) / [references/reference](references/reference.md#绘制圆) |
| Overlays: 3D | Prism, Building, Bd_3DModel, GLTF, OBJ | [references/reference](references/reference.md#绘制棱柱) / [references/reference](references/reference.md#建筑物) / [references/reference](references/reference.md#绘制3D模型) |
| Layers: Tiles/Heatmaps | UrlTileProvider, ImageTileLayer, HeatMapBuilder, HexagonMapBuilder | [references/reference](references/reference.md#瓦片图层) / [references/reference](references/reference.md#ref-map-heatmap-3d) / [references/reference](references/reference.md#ref-map-heatmap-hexagon) / [references/reference](references/reference.md#2D蜂窝热力图) |
| Search: POI | PoiSearch, searchInCity, searchNearby, searchInBound, PoiDetail | [references/reference](references/reference.md#POI检索) |
| Search: Geocoding | GeoCoder, geocode, reverseGeoCode, GeoCodeOption | [references/reference](references/reference.md#地理编码) |
| Search: AOI | AoiSearch, requestAoi, polygon | [references/reference](references/reference.md#AOI检索) |
| Search: Sug | SuggestionSearch, requestSuggestion | [references/reference](references/reference.md#ref-search-suggestion) |
| Search: Bus Lines | BusLineSearch, searchBusLine, BUS_LINE, SUBWAY_LINE | [references/reference](references/reference.md#公交信息检索) |
| Search: Weather | WeatherSearch, WeatherResult, districtID | [references/reference](references/reference.md#天气服务) |
| Search: Recommended Pickup Points | requestRecommendStop, RecommendStopResult | [references/reference](references/reference.md#推荐上车点) |
| Search: Administrative Districts | DistrictSearch, searchDistrict, Boundary, polylines | [references/reference](references/reference.md#检索行政区边界数据) |
| Search: Buildings | BuildingSearch, requestBuilding, 3D Building Blocks | [references/reference](references/reference.md#地图建筑物检索) |
| Route: Driving | RoutePlanSearch, drivingSearch, DrivingRouteResult | [references/reference](references/reference.md#驾车路线规划) |
| Route: Walking | walkingSearch, WalkingRouteResult | [references/reference](references/reference.md#步行路线规划) |
| Route: Cycling | bikingSearch, BikingRouteResult | [references/reference](references/reference.md#骑行路线规划) |
| Route: Transit | transitSearch, masstransitSearch, TransitRouteResult | [references/reference](references/reference.md#公交路线规划) |
| Navigation: Walk/Cycle Engine | BDNaviService, NaviType, NaviMode, initializer, init, unInit | [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md#4-引擎初始化) |
| Navigation: Route Planning | RoutePlanOption, RouteNodeInfo, IRoutePlanListener, RoutePlanError, displayRoutePlanResult | [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md#6-路线规划) |
| Navigation: Navigation Control | start, stop, pause, resume, isStart, cancelRoutePlanDisplay, isMultiNaviCreated | [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md#7-导航控制) |
| Navigation: Status Monitoring | IGuideSubStatusListener, IGuideInfoListener, onRouteFarAway, onArriveDest, onFinalEnd | [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md#8-导航状态监听) |
| Navigation: Default UI | walkRideDefaultUIPage, walkRideUIPageOption, headerGuideShow, naviETAShow, hitTestBehavior | [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md#9-界面渲染) |
| Navigation: Simulated Navigation | MockLocationPlugin, setLocationPlugin, resetLocationPlugin, reloadTrack | [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md#7-导航控制) |
| Navigation: Voice Broadcast | ITTSPlugin, playTTSText, setTTsPlugin | [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md#4-引擎初始化) |
| Utility: Distance/Area | DistanceUtil, AreaUtil, calculateArea, getDistance | [references/reference](references/reference.md#距离和面积计算) |
| Utility: Spatial Relationships | SpatialRelationUtil, isPolygonContainsPoint, getNearestPointFromLine | [references/reference](references/reference.md#点和其他图形的位置关系) |
| Utility: Coordinate Conversion | NativeMethods, wgsll2bdll, gcjll2bdll, mc2ll | [references/reference](references/reference.md#坐标转换) |
| Other: Favorites/Sharing | FavoriteManager, ShareUrlSearch, requestRouteShareUrl | [references/reference](references/reference.md#地图收藏夹) / [references/reference](references/reference.md#位置短地址分享) |

### 2. Map Display and Interaction (Module: map)

- Guidance:
  - Find corresponding map component and controller examples and usage from [references/reference](references/reference.md).
  - Select appropriate map types: standard map, personalized map, satellite map, custom tile map.
  - Configure basic parameters: center point, zoom level, rotation, tilt, compass, scale bar, location button, and other controls.
- Responses should cover:
  - How to introduce `MapComponent` in a Hongmeng page.
  - How to obtain `MapController` in `onReady`.
  - Enabling/disabling gesture interaction (zoom, pan, rotate, tilt, etc.).
  - Key configuration points for control visibility and custom styling (e.g., specific field names if available in the documentation).

### 3. Overlay Drawing (Module: map)

- Focus on the following overlay types (prioritize finding specific interface names in [references/reference](references/reference.md)):
  - Marker points, point clustering, Marker animations.
  - Polylines, arcs.
  - Polygons/areas.
  - Circles.
  - Text annotations.
  - Ground overlays, prisms, 3D buildings/models.
  - Bubbles/pop-ups/info boxes/info windows.
- General pattern for responses:
  - Indicate that methods provided by `MapController` are used to add/update/delete corresponding overlays.
  - Explain necessary parameters (latitude/longitude, color, width, transparency, zIndex, etc.).
  - If complex styling is required (custom icons), guide the user to consult the corresponding section in the online documentation (Map Overlays section).

### 4. Search Capabilities (Module: search)

- Categorize by requirement:
  - POI Search: Standard place search, supporting keyword, city, and range search.
  - AOI Search: Area information.
  - Indoor POI Search: POIs within shopping malls, office buildings, etc.
  - Building Search: Building information.
  - Administrative District Search: Boundary data for provinces/cities/districts.
  - Weather Search: Real-time weather, forecasts, etc.
- Responses should:
  - Indicate the need to install `@bdmap/search` or a combined package.
  - Guide the user to check the corresponding interface descriptions in [references/reference](references/reference.md).
  - Explain synchronous/asynchronous calling modes (based on documentation) and how to handle callbacks/Promises.
  - Remind users to pay attention to quota limits, error code handling, and guide them to check the "Request Status Code Description" in the online documentation.

### 5. Route Planning (Module: @bdmap/map_walkride_search combined package)

- Supports:
  - Driving route planning.
  - Walking route planning.
  - Cycling route planning.
  - Transit route planning.
  - Cross-city transit route planning.
- Recommended response steps:
  - Clarify the required mode of transportation (driving/walking/cycling/transit).
  - Prompt to install `@bdmap/search` and necessary walk/cycle/transit related modules or combined packages, such as `@bdmap/map_walkride_search`.
  - Find corresponding APIs in [references/reference](references/reference.md):
    - Typical parameters: start/end coordinates / keywords, strategies (shortest time, shortest distance, avoid congestion, etc.), waypoints, etc.
  - Provide in the response:
    - How to construct the request parameter object.
    - How to initiate the route planning call.
    - How to parse routes, segments, and coordinates from the returned results and draw them on the map (in conjunction with map overlay capabilities).

> **Walk/Cycle Navigation Scenarios**: If the requirement involves not only route planning but also **real-time navigation guidance** (navigation start/stop, rerouting, default navigation UI, voice broadcast, simulated navigation, etc.), please refer directly to Section 8 "Walk/Cycle Navigation Capabilities" and the [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md).

### 6. Utility Capabilities and Others (Modules: util / map / search)

- Capability examples:
  - Distance and area calculation.
  - Determining the spatial relationship between points and other shapes (e.g., whether a point is inside a polygon).
  - Coordinate conversion (e.g., converting between different coordinate systems).
  - Launching Baidu Map client related capabilities (if explained in the online documentation).
  - Short address sharing for locations, map favorites, etc.
- Response method:
  - Based on the specific requirement, indicate the relevant sections in [references/reference](references/reference.md) or the online documentation such as "Utilities," "Launching Baidu Map Functionality," "Short Address Sharing for Locations," etc.
  - Briefly explain:
    - Meaning of input parameters.
    - Structure of return values.
    - Common errors and precautions (e.g., coordinate system requirements).

### 7. Location Capabilities (Module: locsdk / @bdmap/locsdk)
  This section only provides **key points**. For a complete development guide, please refer to: [Location SDK Development Guide](references/guidelines/location-sdk-guide.md).

  - **Applicable Scenarios**: Foreground continuous location, single-time location, background continuous location, obtaining latitude/longitude/address/POI, etc.
  - **Dependencies and Installation**: Use the project-agreed `@bdmap/locsdk` version uniformly. Configure online/offline dependencies according to the guide and execute `ohpm install` + build self-check.
  - **Privacy and Permissions (Mandatory)**: First obtain user privacy consent and runtime location permissions, then call `LocationClient.setAgreePrivacy(true)`, `LocationClient.checkAuthKey(...)`, and correctly declare location-related permissions and `backgroundModes` in `module.json5`.
  - **Initialization and Usage Order**: Follow the sequence of "Privacy Compliance → AK Authentication → Permission Request → Create `LocationClient` → Register Listener → Configure `LocationClientOption` → Start Location". When the page/business ends, stop location and unregister the listener.
  - **Modes and Capabilities**: Select continuous location, single-time location, or background location based on the business needs, and reasonably set parameters such as coordinate system, time/distance intervals, and whether to return address/location descriptions/POIs.
  - **Result Verification and Error Handling**: Before use, check `isLocSuccess`, ensure coordinates are not (0,0), and the accuracy radius is reasonable. Provide error reasons and suggested solutions through Logger + Toast/status text.
  - **Performance and Compliance**: Set reasonable frequencies and termination conditions for continuous/background location. Sensitive data must be transmitted via HTTPS and precise coordinates should not be output in logs.

### 8. Walk/Cycle Navigation Capabilities (Module: @bdmap/map_walkride_search combined package)
  This section only provides **key points**. For a complete development guide, please refer to: [Walk/Cycle Navigation SDK Development Guide](references/guidelines/walkride-sdk-guide.md).

  - **Applicable Scenarios**: Walk navigation, cycle navigation, display of route planning results, navigation status monitoring, default navigation UI rendering, simulated navigation debugging, etc.
  - **Dependencies and Installation**: Use the combined package `@bdmap/map_walkride_search` (which includes base + map + search + util). It cannot be mixed with standalone packages.
  - **Core Classes and Interfaces**:
    - `BDNaviService`: Main entry point for navigation services, created via `NaviType.WALK` / `NaviType.RIDE`.
    - `RoutePlanOption` + `IRoutePlanListener`: Route planning parameters and callbacks.
    - `IGuideSubStatusListener`: Navigation status monitoring (off-route, approaching/arriving destination, etc.).
    - `IGuideInfoListener`: Real-time data such as guidance information, remaining distance/time, speed, etc.
    - `ITTSPlugin`: Voice broadcast interface.
    - `walkRideDefaultUIPage`: Built-in navigation UI component.
    - `MockLocationPlugin`: Simulated location plugin (for debugging).
  - **Initialization Sequence**: `aboutToAppear` register TTS plugin → `MapComponent.onReady` get MapController → `service.initializer().init(context, mapController)`.
  - **Navigation Control**: Route planning successful → `cancelRoutePlanDisplay()` clear route display → `lifecycle().start()` start navigation → after reaching the destination, `lifecycle().stop()` stop → when the page is destroyed, `initializer().unInit()` release the engine.
  - **Default UI**: When using `walkRideDefaultUIPage` to render the navigation interface, `hitTestBehavior(HitTestMode.None)` must be set to prevent intercepting map gestures.
  - **Coordinate Conversion**: The SDK uses Baidu Coordinate System (BD09ll). External WGS84/GCJ-02 data must be converted via `CoordTrans.wgsToBaidu()` / `CoordTrans.gcjToBaidu()`.
  - **Error Handling**: `RoutePlanError` provides over 20 error codes. User-friendly error messages must be encapsulated; logs alone are insufficient.

## Response Style and Output Format Requirements

When responding to questions based on this Skill:

1. **Prioritize Chinese responses** unless explicitly requested otherwise.
2. **Document Retrieval and Tool Call Order (Mandatory)**:
   - ✅ When dealing with Baidu Map HarmonyOS SDK (e.g., `@bdmap/map` overlays, info boxes/PopViews, etc.), **local documentation must be read first**:
     - (Example) Use tools like `read_file` / `grep` to open and search:
       - [references/reference](references/reference.md)
   - ✅ Only when local documentation is insufficient, or significant version differences/omissions are found, should `web_search` be used to consult online documentation (e.g., `https://lbsyun.baidu.com/faq/api?title=harmonynextsdk`). The source of reference should be stated in the response.
   - ✅ When citing API names, parameters, enums, etc., in the response, they should be based on "local documentation + official online documentation". **It is forbidden to fabricate APIs based solely on memory or experience.**
   - ❌ **Before reading the local [references/reference](references/reference.md), it is forbidden to directly provide specific API implementations based on online search results** (e.g., constructor parameters for PopView, event enum names, etc.).
3. **Response structure should be as clear as possible, recommended to use the following order**:
   - **Scenario Description**: Briefly describe which module/capability this is (map display, search, route planning, etc.).
   - **Dependencies and Permissions**: List the ohpm packages to be installed and the required permissions.
   - **Key Steps**: Use 3-6 steps to describe the process from initialization to API calls.
   - **Example Code**: Provide concise examples (be careful not to conflict with the sample code in this Skill's description; refer to the actual project API naming).
   - **Further Reading**: Provide the local document files to be viewed (e.g., corresponding sections in [references/reference](references/reference.md)) and online documentation sections (e.g., "Map Overlays," "Route Planning," etc.).
4. **Build and Coding Error Self-Check (Mandatory)**:
   - After completing any code modifications related to the Baidu Map HarmonyOS SDK, perform `ohpm install` and `hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon` in the project root directory for a build and ArkTSCheck self-check.
   - If the build fails, trace back and fix the coding errors introduced in this modification based on the error messages. If it's an environment/toolchain issue, clearly distinguish it in the response and provide handling suggestions. See detailed process at: [Build and Coding Error Self-Check Standards](references/guidelines/build-and-test.md).

## Resource Files
- Image Resources: [assets.md](references/assets.md), use the provided image resources preferentially when generating code.

## Reference Documents

When using this Skill, **always combine local documents, installed package declaration files, and official online documentation**:

- Local Documents (This Project):
  - [references/reference](references/reference.md): HarmonyNEXT Map SDK Usage Documentation and Reference Code Summary
- Development Guides (This Project):
  - [references/guidelines/walkride-sdk-guide](references/guidelines/walkride-sdk-guide.md): Complete Walk/Cycle Navigation SDK Development Guide (Engine Initialization, Route Planning, Navigation Control, Status Monitoring, Default UI, Simulated Navigation, TTS, Resource Release)
  - [references/guidelines/location-sdk-guide](references/guidelines/location-sdk-guide.md): Location SDK Development Guide
  - [references/guidelines/package-management](references/guidelines/package-management.md): Package Management Mutual Exclusion Standards
  - [references/guidelines/coding-standards](references/guidelines/coding-standards.md): Coding Standards (Logging, Comments, Modularization, Image Resources)
  - [references/guidelines/performance-optimization](references/guidelines/performance-optimization.md): Performance and Overlay Layering Standards
  - [references/guidelines/ui-feedback](references/guidelines/ui-feedback.md): UI Interaction and User Feedback Standards
  - [references/guidelines/map-style-guide](references/guidelines/map-style-guide.md): Map Style and Visual Standards
  - [references/guidelines/build-and-test](references/guidelines/build-and-test.md): Build and Coding Error Self-Check Standards
- Installed Package Declaration Files:
  - Prerequisite: Check if the references in `entry/oh-package.json5` have been installed. If not, install them via `ohpm install` and record the package name and version number.
  - Check class/interface names in declaration files:
    Use grep (or IDE global search) to search for: "class MapOptions", limit the scope to `oh_modules/@bdmap/map/src/main/ets/`.
  - If the specific path is uncertain, uniformly recommend following the path `@bdmap/xxx/Index.d.ets` → target `.d.ets`, do not randomly search through a large number of obfuscated files:
    - First, search for the directory in the current project's `oh_modules/.ohpm/@bdmap+package_name@version_number`.
    - Then, continue to find the file `oh_modules/@bdmap/package_name/Index.d.ets`.
    - Finally, search for the type name within the `Index.d.ets` file to view the definition.
    - (Example) To find the definition of `MapController` from `{MapController} from '@bdmap/map'`, locate the file `oh_modules/.ohpm/@bdmap+map@2.0.3/oh_modules/@bdmap/map/Index.d.ets` in the current project. If `MapController` is found to have a relative path `./src/main/ets/lbsmapsdk/e/g` within `Index.d.ets`, then the definition of `MapController` can be found in the file `oh_modules/.ohpm/@bdmap+map@2.0.3/oh_modules/@bdmap/map/src/main/ets/lbsmapsdk/e/g.d.ets`.
- Official Online Documentation (Consult for more detailed API, enum, and parameter descriptions):
  - HarmonyNEXT Map SDK Overview and Development Guide: `https://lbsyun.baidu.com/faq/api?title=harmonynextsdk`

When there are discrepancies between local and online documentation, the **official online documentation** takes precedence, but the response should state which type of documentation was referenced.
