import * as THREE from "three";

export class InteractionHandler {
  constructor(camera, scene, renderer) {
    this.camera = camera;
    this.scene = scene;
    this.renderer = renderer;
    this.raycaster = new THREE.Raycaster();
    this.mouse = new THREE.Vector2();
    this.clickables = [];
    
    this.setupListeners();
  }

  setupListeners() {
    window.addEventListener('click', (event) => this.onMouseClick(event));
    window.addEventListener('mousemove', (event) => this.onMouseMove(event));
  }

  updateMouse(event) {
    this.mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
    this.mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
  }

  addClickable(object, callback) {
    this.clickables.push(object);
    object.userData.onClick = callback;
  }

  onMouseClick(event) {
    this.updateMouse(event);
    this.raycaster.setFromCamera(this.mouse, this.camera);
    const intersects = this.raycaster.intersectObjects(this.clickables, true);

    if (intersects.length > 0) {
      const object = intersects[0].object;
      if (object.userData.onClick) {
        object.userData.onClick(intersects[0]);
      }
    }
  }

  onMouseMove(event) {
    this.updateMouse(event);
    // Add hover logic here if needed
  }
}
