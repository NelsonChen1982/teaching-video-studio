// Optional: install playwright externally, then set PLAYWRIGHT_MODULE if not resolvable.
import {createRequire} from 'node:module';
import {createServer} from 'node:http';
import {readFile, mkdir} from 'node:fs/promises';
import path from 'node:path';
import {tmpdir} from 'node:os';
import {fileURLToPath} from 'node:url';
import assert from 'node:assert/strict';
const require=createRequire(import.meta.url);
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const root=fileURLToPath(new URL('../skills/teaching-video-studio/assets/transitions/',import.meta.url));
const output=path.resolve(process.env.SMOKE_OUTPUT||path.join(tmpdir(),'teaching-video-transition-smoke'));
await mkdir(output,{recursive:true});
const server=createServer(async(req,res)=>{try{const pathname=new URL(req.url,'http://localhost').pathname;const file=path.resolve(root,'.'+decodeURIComponent(pathname==='/'?'/demo.html':pathname));if(!file.startsWith(root)){res.writeHead(403);res.end();return;}res.setHeader('Content-Type',file.endsWith('.html')?'text/html; charset=utf-8':'text/javascript');res.end(await readFile(file));}catch{res.writeHead(404);res.end();}});
await new Promise((resolve,reject)=>{server.on('error',reject);server.listen(0,'127.0.0.1',resolve);});
let browser;
try{
 browser=await chromium.launch({headless:true,...(process.env.CHROME_PATH?{executablePath:process.env.CHROME_PATH}:{})});
 const page=await browser.newPage({viewport:{width:1024,height:820},deviceScaleFactor:1});const errors=[];page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(`http://127.0.0.1:${server.address().port}/`);await page.waitForFunction(()=>window.demoReady);
 for(const kind of ['directional-wipe','dry-brush','ink-spread']){
  for(const p of [0,.25,.5,.75,1]){await page.evaluate(([kind,p])=>window.renderMask(kind,p),[kind,p]);await page.locator('canvas').screenshot({path:path.join(output,`${kind}-${p}.png`)});}
  await page.evaluate(k=>window.renderMask(k,.5),kind);const a=await page.locator('canvas').screenshot();await page.evaluate(k=>window.renderMask(k,.1),kind);await page.evaluate(k=>window.renderMask(k,.5),kind);assert.deepEqual(await page.locator('canvas').screenshot(),a);
 }
 assert.deepEqual(errors,[]);console.log(JSON.stringify({snapshots:15,randomSeekPixelIdentical:true,pageErrors:errors,output}));
}finally{if(browser)await browser.close();server.close();}
