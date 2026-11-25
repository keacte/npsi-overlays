// Pulls the npsi.rocks fleet schedule (yesterday + next 7 days) and writes fleets.json next to the widgets,
// so the stream view can read it from the same site (no CORS problems).
import { writeFileSync, readFileSync, existsSync, mkdirSync } from 'node:fs';
const API = 'https://npsi.rocks/events/api/events/';
const pad = n => String(n).padStart(2, '0');
const days = Array.from({ length: 9 }, (_, i) => new Date(Date.now() + (i - 1) * 864e5));
const seen = new Map();
let ok = 0;
for (const d of days) {
  const day = `${pad(d.getUTCDate())}-${pad(d.getUTCMonth() + 1)}-${d.getUTCFullYear()}`;
  try {
    const r = await fetch(API + day, { headers: { 'User-Agent': 'npsi-overlays (fleet schedule widget)', Accept: 'application/json' } });
    if (!r.ok) throw new Error('HTTP ' + r.status);
    const j = await r.json();
    if (!Array.isArray(j.events)) throw new Error('no events array');
    ok++;
    for (const e of j.events) if (!seen.has(e.id))
      seen.set(e.id, { id: e.id, name: e.name, host: e.host, fc: e.fc, staging: e.location, time: e.start, end: e.end, ended: !!e.ended, hostImage: e.hostImage || null });
  } catch (e) { console.error(day, 'failed:', e.message); }
}
if (!ok) { console.error('No day could be loaded; leaving fleets.json unchanged'); process.exit(0); }
const fleets = [...seen.values()].sort((a, b) => new Date(a.time) - new Date(b.time));

// Download each host's logo into logos/ so the widget can load it from the same site (npsi.rocks blocks hotlinking).
mkdirSync('logos', { recursive: true });
for (const f of fleets) {
  if (!f.hostImage) continue;
  const file = 'logos/' + f.hostImage.split('/').pop().replace(/[^A-Za-z0-9._-]/g, '_');
  if (!existsSync(file)) {
    try {
      const url = /^https?:/.test(f.hostImage) ? f.hostImage : 'https://npsi.rocks' + f.hostImage;
      const r = await fetch(url, { headers: { 'User-Agent': 'npsi-overlays (fleet schedule widget)' } });
      if (!r.ok) throw new Error('HTTP ' + r.status);
      writeFileSync(file, Buffer.from(await r.arrayBuffer()));
      console.log('saved', file);
    } catch (e) { console.error('logo failed', f.hostImage, e.message); continue; }
  }
  f.logo = file;
}
const next = JSON.stringify({ fleets }, null, 1);
const prev = existsSync('fleets.json') ? JSON.stringify({ fleets: JSON.parse(readFileSync('fleets.json', 'utf8')).fleets }, null, 1) : '';
if (next !== prev) writeFileSync('fleets.json', JSON.stringify({ updated: new Date().toISOString(), fleets }, null, 1));
console.log(`days ok: ${ok}/${days.length}, fleets: ${fleets.length}, changed: ${next !== prev}`);
