/**
 * Choreographer Helper script
 */
function generateCameraPath(keyframes, duration) {
  return {
    path_type: "spline",
    keyframes: keyframes,
    duration: duration,
    smoothing: true
  };
}
module.exports = { generateCameraPath };
