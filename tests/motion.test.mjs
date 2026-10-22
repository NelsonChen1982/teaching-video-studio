import test from 'node:test';
import assert from 'node:assert/strict';
import {stateAt,DURATION} from '../skills/teaching-video-studio/assets/three-starter/motion.mjs';
test('arbitrary seek is repeatable',()=>{const a=stateAt(8);stateAt(2);assert.deepEqual(stateAt(8),a);});
test('frames finite and bounded',()=>{for(let t=0;t<=DURATION;t+=1/30){const s=stateAt(t);assert.ok([...s.camera,...s.target,s.packetX,s.packetY].every(Number.isFinite));assert.ok(s.packetX>=-4&&s.packetX<=4);}assert.deepEqual(stateAt(-10),stateAt(0));assert.deepEqual(stateAt(100),stateAt(DURATION));});
test('camera continuous',()=>{for(const t of [4,8,12]){const a=stateAt(t-.0001),b=stateAt(t+.0001);assert.ok(Math.hypot(...a.camera.map((x,i)=>x-b.camera[i]))<.01);}});
test('invalid time rejected',()=>assert.throws(()=>stateAt(NaN)));
