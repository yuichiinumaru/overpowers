import * as THREE from "three";

export const Materials = {
  createStandard(params) {
    return new THREE.MeshStandardMaterial({
      roughness: 0.5,
      metalness: 0.5,
      ...params
    });
  },

  createPhysical(params) {
    return new THREE.MeshPhysicalMaterial({
      roughness: 0.5,
      metalness: 0.5,
      clearcoat: 1.0,
      clearcoatRoughness: 0.1,
      ...params
    });
  },

  createGlass(params) {
    return new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      metalness: 0,
      roughness: 0,
      transmission: 1,
      thickness: 0.5,
      ior: 1.5,
      ...params
    });
  },

  createToon(params) {
    return new THREE.MeshToonMaterial({
      ...params
    });
  }
};
