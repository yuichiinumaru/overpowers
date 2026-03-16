import sys

geometries = {
    "BoxGeometry": "width, height, depth, widthSegments, heightSegments, depthSegments",
    "SphereGeometry": "radius, widthSegments, heightSegments, phiStart, phiLength, thetaStart, thetaLength",
    "PlaneGeometry": "width, height, widthSegments, heightSegments",
    "CircleGeometry": "radius, segments, thetaStart, thetaLength",
    "CylinderGeometry": "radiusTop, radiusBottom, height, radialSegments, heightSegments, openEnded",
    "ConeGeometry": "radius, height, radialSegments, heightSegments, openEnded",
    "TorusGeometry": "radius, tube, radialSegments, tubularSegments, arc",
    "CapsuleGeometry": "radius, length, capSegments, radialSegments"
}

def list_geometries():
    print(f"{'Geometry Type':<20} | {'Parameters'}")
    print("-" * 60)
    for geo, params in geometries.items():
        print(f"{geo:<20} | {params}")

if __name__ == "__main__":
    list_geometries()
