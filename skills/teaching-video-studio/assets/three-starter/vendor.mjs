import {copyFile, mkdir} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
const base = fileURLToPath(new URL('.', import.meta.url));
await mkdir(`${base}vendor`, {recursive: true});
for (const name of ['three.module.js', 'three.core.js']) {
  await copyFile(`${base}node_modules/three/build/${name}`, `${base}vendor/${name}`);
}
await copyFile(`${base}node_modules/three/LICENSE`, `${base}vendor/THREE-LICENSE.txt`);
console.log('Local Three.js modules and license prepared.');
