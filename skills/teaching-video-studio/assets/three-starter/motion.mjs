export const DURATION = 18;
export const clamp = (v, lo = 0, hi = 1) => Math.max(lo, Math.min(hi, v));
export const smooth = v => { const t = clamp(v); return t * t * (3 - 2 * t); };
const mix = (a, b, t) => a.map((v, i) => v + (b[i] - v) * t);
const keys = [
  {t: 0, position: [-6, 3.4, 8], target: [-4, 1, 0]},
  {t: 4, position: [-4, 2.6, 6], target: [-4, 1, 0]},
  {t: 8, position: [1, 3, 7], target: [0, 1, 0]},
  {t: 12, position: [7, 3.5, 6], target: [4, 1, 0]},
  {t: 18, position: [8, 9, 17], target: [0, .7, 0]}
];
export function stateAt(seconds) {
  if (!Number.isFinite(seconds)) throw new Error('Time must be finite');
  const t = clamp(seconds, 0, DURATION);
  const i = Math.min(keys.length - 2, keys.findIndex((key, index) => index < keys.length - 1 && t <= keys[index + 1].t));
  const a = keys[i], b = keys[i + 1], u = smooth((t-a.t)/(b.t-a.t));
  const outbound = t <= 12;
  const packetX = outbound ? -4 + 8*smooth((t-3)/9) : 4-8*smooth((t-12)/4);
  return {t, camera: mix(a.position,b.position,u), target: mix(a.target,b.target,u), packetX,
    packetY: 1.2 + .25*Math.sin(Math.PI*clamp((t-3)/13)),
    active: t < 5 ? 0 : t < 10 ? 1 : t < 14 ? 2 : 0};
}
