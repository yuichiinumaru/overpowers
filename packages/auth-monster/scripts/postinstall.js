const fs = require('fs');
const path = require('path');
const { xdgConfig } = require('xdg-basedir');

function postinstall() {
  const configDir = path.join(xdgConfig || '', 'opencode');
  if (!fs.existsSync(configDir)) {
    console.log(`Creating config directory at ${configDir}`);
    fs.mkdirSync(configDir, { recursive: true });
  } else {
    console.log(`Config directory already exists at ${configDir}`);
  }
}

try {
  postinstall();
} catch (error) {
  console.error('Postinstall script failed:', error);
  // Don't exit with 1 to avoid breaking npm install if this fails
}
