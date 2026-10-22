import test from 'node:test';import assert from 'node:assert/strict';
import {createField,maskAt,compositeOpaque} from '../skills/teaching-video-studio/assets/transitions/masks.mjs';
for(const kind of ['directional-wipe','dry-brush','ink-spread']){
 test(kind+': endpoints, monotonicity, repeatable seek and local feather',()=>{
  const f=createField(96,54,{kind,seed:8});assert.ok(maskAt(f,0).every(x=>x===0));assert.ok(maskAt(f,1).every(x=>x===1));
  let prior=maskAt(f,0);
  for(let p=.05;p<1;p+=.05){const m=maskAt(f,p);assert.ok(m.every((v,i)=>v>=prior[i]&&v>=0&&v<=1));prior=m;}
  const m=maskAt(f,.5);maskAt(f,.2);assert.deepEqual(maskAt(f,.5),m);
  assert.ok(m.filter(v=>v>0&&v<1).length/m.length<.12,'Only a narrow boundary may blend');
  assert.deepEqual(createField(96,54,{kind,seed:8}),f);
 });
}
test('compositor has exact endpoint pixels and no transparency',()=>{
 const a=new Uint8ClampedArray([255,0,0,255,255,0,0,255]),b=new Uint8ClampedArray([0,0,255,255,0,0,255,255]);
 assert.deepEqual(compositeOpaque(a,b,[0,0]),a);assert.deepEqual(compositeOpaque(a,b,[1,1]),b);
 assert.deepEqual([...compositeOpaque(a,b,[0,1])],[255,0,0,255,0,0,255,255]);
 b[3]=0;assert.throws(()=>compositeOpaque(a,b,[.5,.5]));
});
test('invalid parameters rejected',()=>{assert.throws(()=>createField(0,5));assert.throws(()=>createField(5,5,{kind:'unknown'}));assert.throws(()=>maskAt(createField(5,5),NaN));});
