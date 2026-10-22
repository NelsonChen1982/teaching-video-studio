// Original Teaching Video Studio helpers. No external dependencies.
// A field stores when each pixel is revealed, not an accumulating simulation.
const clamp=(x,a=0,b=1)=>Math.max(a,Math.min(b,x));
const smooth=x=>{x=clamp(x);return x*x*(3-2*x);};
function hash(x,y,seed){let n=Math.imul(x+seed,374761393)^Math.imul(y+seed,668265263);n=Math.imul(n^(n>>>13),1274126177);return ((n^(n>>>16))>>>0)/4294967295;}
function noise(x,y,seed){const a=Math.floor(x),b=Math.floor(y),u=smooth(x-a),v=smooth(y-b);const top=hash(a,b,seed)*(1-u)+hash(a+1,b,seed)*u;const bottom=hash(a,b+1,seed)*(1-u)+hash(a+1,b+1,seed)*u;return top*(1-v)+bottom*v;}
export function createField(width,height,{kind='directional-wipe',seed=17}={}){
 if(!Number.isInteger(width)||!Number.isInteger(height)||width<=0||height<=0||width*height>16777216)throw Error('Invalid field dimensions');
 if(!['directional-wipe','dry-brush','ink-spread'].includes(kind))throw Error('Unknown mask kind');
 if(!Number.isInteger(seed))throw Error('Seed must be an integer');
 const values=new Float32Array(width*height);let min=Infinity,max=-Infinity;
 for(let y=0;y<height;y++)for(let x=0;x<width;x++){
  const u=(x+.5)/width,v=(y+.5)/height;
  let q=u;
  if(kind==='dry-brush'){
   // Longitudinal bristle variation with a rough advancing edge.
   q=u+.19*(noise(v*65,0,seed)-.5)+.065*(noise(u*18,v*90,seed+1)-.5)+.025*Math.sin(v*180);
  }else if(kind==='ink-spread'){
   // Multiple fixed absorption origins; no frame-history dependence.
   q=Infinity;
   for(const [cx,cy,delay] of [[.25,.46,0],[.55,.25,.12],[.72,.7,.18]]){
    const d=Math.hypot((u-cx)*width/height,v-cy);
    q=Math.min(q,d+delay+.085*(noise(u*13,v*13,seed)-.5)+.025*(noise(u*49,v*49,seed+3)-.5));
   }
  }
  const i=y*width+x;values[i]=q;min=Math.min(min,q);max=Math.max(max,q);
 }
 const range=max-min||1;for(let i=0;i<values.length;i++)values[i]=(values[i]-min)/range;
 return {width,height,kind,seed,values};
}
export function maskAt(field,progress,feather=.012){
 if(!Number.isFinite(progress)||!Number.isFinite(feather)||feather<0||feather>.2)throw Error('Invalid progress or feather');
 const p=clamp(progress),out=new Float32Array(field.values.length);
 if(p===0)return out;if(p===1){out.fill(1);return out;}
 for(let i=0;i<out.length;i++)out[i]=feather===0?(p>=field.values[i]?1:0):smooth((p-field.values[i])/feather+.5);
 return out;
}
export function compositeOpaque(a,b,mask,out=new Uint8ClampedArray(a.length)){
 if(a.length!==b.length||a.length!==mask.length*4||out.length!==a.length)throw Error('Size mismatch');
 for(let i=0;i<mask.length;i++){
  const j=i*4,m=mask[i];
  if(a[j+3]!==255||b[j+3]!==255)throw Error('Flatten transparent assets onto the intended backdrop first');
  if(!Number.isFinite(m)||m<0||m>1)throw Error('Invalid mask weight');
  for(let c=0;c<3;c++)out[j+c]=a[j+c]*(1-m)+b[j+c]*m;
  out[j+3]=255;
 }
 return out;
}
