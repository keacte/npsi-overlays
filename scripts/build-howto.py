#!/usr/bin/env python3
"""Generates the NPSI How-To pages into ../howto/. Run: python3 scripts/build-howto.py"""
import os, html

OUT = os.path.join(os.path.dirname(__file__), '..', 'howto')
CAL = 'https://npsi.rocks/calendar'
HOWTO = 'https://npsi.rocks/how-to-npsi'
DISCORD = 'https://discord.com/invite/78CS3Aa'
CHARTER = 'https://npsi.rocks/community-charter'
ABOUT = 'https://npsi.rocks/about'
HOME = 'https://npsi.rocks'

def steps(items):
    return '<ol class="steps">' + ''.join(f'<li><b>{t}</b>{d}</li>' for t, d in items) + '</ol>'
def cards(items, cls='g2'):
    return f'<div class="{cls}">' + ''.join(
        f'<div class="card {c}"><b>{t}</b>' + (f'<small>{s}</small>' if s else '') + f'<p>{d}</p></div>' for c, t, s, d in items) + '</div>'
def note(t, label='NOTE', warn=False):
    return f'<div class="note{" warn" if warn else ""}" data-l="{label}">{t}</div>'
def tl(items):
    return '<div class="tl">' + ''.join(f'<div class="t"><b>{a}</b><p>{b}</p></div>' for a, b in items) + '</div>'
def gloss(items):
    return '<dl class="gl">' + ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in items) + '</dl>'
def checklist(key, items):
    lis = ''.join(f'<li data-k="{i}"><span>{t}{f"<small>{s}</small>" if s else ""}</span></li>' for i, (t, s) in enumerate(items))
    return (f'<div class="prog"><span id="pt">0 / {len(items)}</span><div class="pb"><i id="pf"></i></div></div>'
            f'<ul class="check" data-store="{key}">{lis}</ul>')
def sec(n, title, body, cls=''):
    return f'<section class="panel {cls}" id="s{n}"><h2><span>{n:02d}</span>{title}</h2>{body}</section>'

PAGES = []

# ---------------------------------------------------------------- 1
PAGES.append(dict(
 slug='your-first-npsi-fleet', short='START HERE', title='Your First NPSI Fleet',
 sub='Everything a new pilot needs to know before joining', status=[('LEVEL', 'ROOKIE'), ('REQUIRED', 'ONE SHIP'), ('SNEAKINESS', 'OPTIONAL')],
 tldr='NPSI fleets are <b>public PvP roams open to everyone</b>. Pick a fleet on the calendar, read the advert, fly the right ship to the staging system, join the host\'s comms, <b>XUP when the FC asks</b>, then listen and follow instructions. Losing ships is normal. Have fun.',
 secs=[
  ('The 10-minute version', f'''<p class="lead">NPSI stands for <b>Not Purple Shoot It</b>. Fleet members show as purple on your overview, so everything that is not purple is fair game. No standings, no corp membership and no application: if you can undock in a ship that suits the fleet, you can fly.</p>
{steps([
 ('Find a fleet', f'Open the <a href="{CAL}" target="_blank">NPSI calendar</a> and pick something that suits your ship and your timezone. <a href="find-a-fleet.html">Full guide &rarr;</a>'),
 ('Read the advert', 'Staging system, start time, ship or doctrine, and which comms and channel to use. <a href="join-your-first-fleet.html">How to join &rarr;</a>'),
 ('Prepare your ship', 'Right ship, correct fit, ammo, paste, drugs, a PvP clone, and home station set to staging. <a href="prepare-for-a-fleet.html">Preparation checklist &rarr;</a>'),
 ('Join comms and XUP', 'Be in the right channel early. When the FC calls for XUP, type it in channel. <a href="when-you-join-fleet.html">What to do on joining &rarr;</a>'),
 ('Follow the FC', 'Listen, align when told, warp when told, shoot what is called. <a href="fly-with-strangers.html">Etiquette &rarr;</a>'),
 ('Give feedback and come back', 'Fill in the fleet feedback form afterwards, then book your next fleet. <a href="become-a-regular.html">Becoming a regular &rarr;</a>')])}'''),
  ('What you need before you start', checklist('first-fleet', [
   ('A ship that matches the fleet advert', 'Check the doctrine or ship class'),
   ('Skills to fly it safely', 'Core skills trained, not just "can sit in it"'),
   ('Voice comms installed and tested', 'Each group lists its own comms details'),
   ('A decent PvP overview', 'Know how to find hostiles and sort by distance'),
   ('Ammo, paste, boosters, drones', 'Fit and load before the fleet, not during'),
   ('A cheap PvP clone and no precious implants', 'Do not wear what you cannot replace'),
   ('Home station set to the staging system', 'So a pod-out sends you somewhere useful'),
   ('An attitude of learning', 'Everyone was new once')])),
  ('What actually happens', tl([
   ('BEFORE', 'The FC posts the fleet. Pilots move ships to staging in the days before and join the community channel.'),
   ('FORM UP', 'The FC announces formup, asks you to XUP, and sends invites. You join the fleet and read the MOTD.'),
   ('THE ROAM', 'You move system to system, follow broadcasts, and fight what the FC finds. Expect short bursts of action between quiet gates.'),
   ('AFTER', 'Dock up, say thanks, fill in the feedback form, and replace what you lost.')]) + note('Fleets are mostly advertised up to a week ahead, so you can prepare at your own pace.', 'TIP')),
  ('New to this? Read these next', cards([
   ('do', 'What does NPSI mean?', 'Start with the basics', 'The name, the idea and the vocabulary you will hear in comms.'),
   ('do', 'How to fly with strangers', 'Expectations', 'How to behave so FCs and fleetmates enjoy flying with you.'),
   ('do', 'What happens if I lose my ship?', 'Losses', 'Why losing ships is part of the game and how to cope.'),
   ('do', 'How to prepare for a fleet', 'Your checklist', 'A printable-style checklist you can tick off on the page.')]))]))

# ---------------------------------------------------------------- 2
PAGES.append(dict(
 slug='find-a-fleet', short='FIND A FLEET', title='How to Find a Fleet',
 sub='Finding public fleets on NPSI.rocks', status=[('SOURCE', 'CALENDAR'), ('COST', 'FREE'), ('INVITE NEEDED', 'NO')],
 tldr=f'Everything is on the <a href="{CAL}" target="_blank">NPSI calendar</a>. Filter by your time, check the staging system and ship type, then follow the host in Discord to get reminders. Fleets are mostly advertised up to a week ahead.',
 secs=[
  ('Where fleets are listed', f'''<p class="lead">NPSI.rocks is the central hub for public EVE fleets. It lists upcoming fleets from many different hosts in one place, so you do not need to hunt around.</p>
{cards([
 ('do', 'NPSI calendar', 'npsi.rocks/calendar', f'Every upcoming fleet in one list. <a href="{CAL}" target="_blank">Open the calendar</a>.'),
 ('do', 'The homepage', 'npsi.rocks', f'Shows what is coming up in the next seven days and recent roam reports. <a href="{HOME}" target="_blank">Open NPSI.rocks</a>.'),
 ('do', 'Host directory', 'Hosts page', 'Browse the communities that run fleets, learn who they are and what they fly.'),
 ('do', 'Discord announcements', 'FUN Inc Discord', f'Fleets are advertised in Discord, often up to a week ahead. <a href="{DISCORD}" target="_blank">Join the Discord</a>.')])}'''),
  ('How to read a fleet listing', '''<p>Each fleet card tells you what you need to decide whether to fly it. Look for:</p>''' + gloss([
   ('Fleet name', 'Often hints at the ship class or theme. Things like "Cheap Yeet" or "T3D Tuesday" tell you what to expect.'),
   ('Host and FC', 'The community running it and the Fleet Commander leading it.'),
   ('Staging system', 'Where to bring your ship before the fleet forms. This is the most important thing to get right.'),
   ('Start time', 'Given in EVE time (UTC). <a href="fleets-for-your-timezone.html">Convert it to your timezone.</a>'),
   ('Ship / doctrine', 'Which ships you should fly. Some fleets are "bring anything", some are strict.'),
   ('Handouts / support', 'Some hosts provide ships. Always check the advert instead of assuming.')])),
  ('Choosing your first fleet', cards([
   ('do', 'Pick a friendly format', 'Beginner-safe', 'Frigate and cruiser roams are cheap, fast and forgiving. A great place to learn.'),
   ('do', 'Pick a time you can finish', 'Commit', 'A roam can run a couple of hours. Do not join if you need to leave in 20 minutes.'),
   ('do', 'Pick a ship you can afford to lose', 'Budget', 'Never fly something you would be upset to lose. Cheap fits are a feature, not a flaw.'),
   ('dont', 'Avoid fleets you cannot reach', 'Logistics', 'If staging is ten jumps away and you only have an hour, choose another fleet.')])),
  ('Never miss a fleet', steps([
   ('Follow hosts you enjoy', 'Join the host\'s Discord or community channel so you see changes and last-minute notices.'),
   ('Set a reminder', 'Add the fleet time to your phone or calendar in your own timezone.'),
   ('Check again an hour before', 'Times and staging can change. Re-read the advert on the day.')]) + note('Most hosts post a ping in their community channel when the fleet is about to form.', 'TIP'))]))

# ---------------------------------------------------------------- 3
PAGES.append(dict(
 slug='join-your-first-fleet', short='JOIN A FLEET', title='How to Join Your First Fleet',
 sub='Fleet adverts, fleet invites and joining instructions', status=[('ADVERT', 'READ IT'), ('XUP', 'ON PROMPT'), ('INVITE', 'FROM FC')],
 tldr='Read the advert, be at the staging system early, join the host\'s channel and voice comms, then <b>wait for the FC to prompt you to XUP</b>. Do not XUP early, and do not spam. The FC will send invites in order.',
 secs=[
  ('Reading a fleet advert', '''<p class="lead">A good advert answers every question you have. If it does not, do not guess. Ask politely in the community channel.</p>''' + cards([
   ('do', 'When and where', 'Time + staging', 'Start time in EVE time and the staging system. Everything else depends on these.'),
   ('do', 'What to fly', 'Doctrine', 'The ship type or doctrine the FC wants. Bring the right ship, not your favourite.'),
   ('do', 'How to communicate', 'Comms', 'Voice server details and the text channel to XUP in. Each group lists its own.'),
   ('do', 'Rules of the roam', 'MOTD / notes', 'Anything unusual: handouts, area of space, ISK limits or required boosters.')])),
  ('Joining step by step', steps([
   ('Check the advert the day before', 'Time, staging system, ship and comms. If anything is unclear, ask in the community channel.'),
   ('Move your ship to staging', 'Do this in the days before, not five minutes before formup. Set your home station there too.'),
   ('Join the voice comms and the text channel', 'Test your microphone and speakers. Join the channel the advert tells you to use. Join early and listen.'),
   ('Wait for the XUP call', 'The FC will tell the channel when to XUP. Type <b>x</b> or <b>xup</b> with your ship, for example "x, Caracal", as the host asks.'),
   ('Accept the fleet invite', 'The FC sends invites. Accept the pop-up, then check you are in the fleet window.'),
   ('Read the MOTD', 'The Message of the Day holds the rules, comms and objectives for the roam. Read it before you ask questions.'),
   ('Undock or wait for instructions', 'Do not undock until the FC says so unless the advert says otherwise.')])),
  ('What does XUP mean?', '''<p><b>XUP</b> means "I am ready to join, here is my ship". The FC uses the XUP list to see who is available, which ships are coming, and who to invite first.</p>
<div class="g3"><div class="card"><b>Format</b><small>Usually</small><p>x, or xup, plus ship name, like <span class="chip">x Caracal</span></p></div>
<div class="card"><b>When</b><small>Only on call</small><p>Wait until the FC asks. Early messages clutter the channel.</p></div>
<div class="card"><b>After</b><small>Be patient</small><p>You may wait a few minutes. Stay in comms and keep an eye on invites.</p></div></div>''' ),
  ('Troubleshooting', gloss([
   ('No invite arrived', 'Check you are in the correct channel and that your XUP matched the format. Politely ask the FC, once.'),
   ('Cannot hear the FC', 'Check you joined the right voice channel and your output device. Ask in text if you cannot fix it.'),
   ('Wrong staging system', 'Tell the channel. Experienced pilots will help you catch up, or the FC may wait.'),
   ('Late to formup', 'Message the channel, say where you are and ask if you can catch up. Do not warp straight to the fleet.'),
   ('Not sure what to fly', 'Ask which ship class fits the roam. Anything in the right role is better than the wrong ship.')]) + note('Never be afraid to ask. FCs would rather answer a question than lose a pilot to confusion.', 'TIP'))]))

# ---------------------------------------------------------------- 4
PAGES.append(dict(
 slug='what-does-npsi-mean', short='WHAT IS NPSI?', title='What Does NPSI Mean?',
 sub='Not Purple Shoot It explained', status=[('PURPLE', 'FRIEND'), ('NOT PURPLE', 'TARGET'), ('STRINGS', 'NONE')],
 tldr='<b>NPSI = Not Purple Shoot It.</b> Pilots in the fleet appear <b>purple</b> on your overview. Anything that is not purple is a valid target. It is public, open to everyone and has no blues and no strings: <i>just content</i>.',
 secs=[
  ('The idea', '''<p class="lead">NPSI is a style of public PvP fleet. Rather than being blue to everyone, you simply fly with whoever is in the fleet. If you can see purple, they are on your side. If it is not purple, shoot it.</p>
<div class="g3"><div class="card do"><b>Purple</b><small>In fleet</small><p>Friends. Do not shoot, and protect them.</p></div>
<div class="card dont"><b>Not purple</b><small>Everyone else</small><p>Valid targets. The FC will tell you what to shoot first.</p></div>
<div class="card"><b>No strings</b><small>No commitments</small><p>No standings, no corp application, no obligations. Just show up.</p></div></div>''' + note('"Not purple? Shoot it!" and "No blues, no strings, just content!" is how NPSI.rocks describes it.', 'FROM THE SITE')),
  ('Why people love it', cards([
   ('do', 'Accessible PvP', 'For new pilots', 'You do not need to be an expert, or in a big alliance, to get into fights.'),
   ('do', 'Meet people', 'Community', 'You meet pilots from many groups and learn from different FCs.'),
   ('do', 'Variety', 'Different every night', 'Frigates one day, battlecruisers the next, wormholes, nullsec, lowsec and more.'),
   ('do', 'Real content', 'Fun to watch', 'Many NPSI fleets are streamed and recorded. Plenty of pilots enjoy sharing fights.')])),
  ('A short history', f'<p>According to <a href="{ABOUT}" target="_blank">the NPSI.rocks About page</a>:</p>' + tl([
   ('APRIL 2018', 'FUN INC / Even Better With Friends is founded after Agony Unleashed ends. Its members share a love of PvP.'),
   ('SEPTEMBER 2018', 'FUN INC begins running NPSI public roams in Syndicate.'),
   ('EARLY 2020', 'Those roams grow into the NPSI Community Gateway.'),
   ('LATER', 'Discord calendar integrations, the Fluffy announcement bot and the npsi.rocks website arrive.')])),
  ('What NPSI is not', cards([
   ('dont', 'Not a corp', 'No membership', 'You do not join a corporation to fly in an NPSI fleet.'),
   ('dont', 'Not a free-for-all', 'Orders matter', 'The FC leads. Following instructions is how the fleet wins.'),
   ('dont', 'Not for friends only', 'Open to all', 'Newcomers are welcome. The charter promotes inclusion, not exclusion.'),
   ('dont', 'Not a place for toxicity', 'Fly together, win together', f'The <a href="{CHARTER}" target="_blank">community charter</a> is built around visibility, variety and inclusivity.')])),
  ('NPSI vocabulary', gloss([
   ('FC', 'Fleet Commander. The pilot leading the fleet. Listen to them.'),
   ('XUP', 'Say you are ready, with your ship, when the FC asks.'),
   ('Staging', 'The system where the fleet forms up.'),
   ('MOTD', 'Message of the Day. The fleet\'s notes, shown in the fleet window.'),
   ('Doctrine', 'The set of ships and fits the fleet is flying.'),
   ('Primary', 'The target everyone shoots first, called by the FC.'),
   ('Tackle', 'Ships that hold targets down with scramblers and webs so the fleet can kill them.'),
   ('D-scan', 'Directional scanner. Used to find ships nearby, even if not on grid.'),
   ('Broadcast', 'Fleet signals like Align To, Warp To, Target and Need Armor.'),
   ('SRP', 'Ship Replacement Program. Some groups replace lost ships. Not all do, so check.'),
   ('Staging / Home', 'Set your home station to the fleet\'s staging system.'),
   ('GF', 'Good fight. Say it after a fight, win or lose.')]))]))

# ---------------------------------------------------------------- 5
PAGES.append(dict(
 slug='fly-with-strangers', short='ETIQUETTE', title='How to Fly With Strangers',
 sub='Fleet etiquette, communication and expectations', status=[('COMMS', 'CLEAR'), ('EGOS', 'DOCKED'), ('ORDERS', 'FOLLOWED')],
 tldr='<b>Be on time, be prepared, listen to the FC, keep comms clear, and follow instructions.</b> Do not backseat fly. Be kind: everyone was new once, and the best fleets are the ones people want to rejoin.',
 secs=[
  ('The golden rules', steps([
   ('Be on time', 'Arrive early and in the right ship. Late pilots slow everyone down.'),
   ('Be prepared', 'Correct fit, ammo, paste, drugs, clone and overview. Do it before the fleet, not during.'),
   ('Listen to the FC', 'They are making dozens of decisions a minute. Silence your distractions.'),
   ('Follow instructions at all times', 'Align when told, warp when told, shoot what is called. If you disagree, argue after the fleet.'),
   ('Read the MOTD first', 'Most questions are answered in the MOTD. Read it before asking.'),
   ('Be kind', 'Everybody is here to have fun. Treat new pilots like you hoped to be treated.')])),
  ('Do and do not', '<div class="g2"><div class="card do"><b>Do</b><small>Be that pilot</small><ul>' + ''.join(f'<li>{x}</li>' for x in [
   'XUP when the FC asks', 'Keep voice chatter short and clear', 'Call out new hostiles, system and distance', 'Volunteer to scout, scan or D-scan',
   'Say "thanks" at the end', 'Stay on grid and with the fleet', 'Admit mistakes and move on', 'Offer help to newer pilots']) +
   '</ul></div><div class="card dont"><b>Do not</b><small>Common mistakes</small><ul>' + ''.join(f'<li>{x}</li>' for x in [
   'Backseat fly or argue tactics on comms', 'Talk over the FC', 'Break from the fleet to do your own thing', 'Spam chat or broadcasts',
   'Blame others when a fight goes badly', 'Ask questions already answered in the MOTD', 'Rage when you lose a ship', 'Undock early or ahead of the fleet']) + '</ul></div></div>'),
  ('Communication', gloss([
   ('Listen first', 'Most of the time your job is to listen. Only speak when you have something useful.'),
   ('Keep it short', 'Say what, where, how many. "Three hostile Caracals, on the Jita gate, 40 km." Then stop.'),
   ('Use push-to-talk', 'Avoid open mics. Keyboard noise, pets, music and family do not help the FC.'),
   ('Know when to mute', 'If the FC is calling targets, nobody else is talking.'),
   ('Text vs voice', 'Questions go in text chat. Voice is for fleet information.'),
   ('Be clear in text', 'Use the fleet or channel the FC asks you to use, not private tells.')])),
  ('What FCs expect from you', cards([
   ('do', 'Reliability', 'Show up, stay', 'If you say you will join, join. If something changes, say so.'),
   ('do', 'Awareness', 'Eyes open', 'Know your ship\'s speed, range, EWAR and drones. Know what your role is.'),
   ('do', 'Flexibility', 'Adapt', 'Plans change. The FC may switch targets or retreat. Go with it.'),
   ('do', 'Feedback', 'After the fleet', 'Fill in the feedback form. It takes about two minutes and helps FCs improve.')]) + note(f'NPSI.rocks charter values: <i>variety, visibility, inclusivity</i>, and "fly together, win together". <a href="{CHARTER}" target="_blank">Read the charter.</a>', 'COMMUNITY')),
  ('When things go wrong', cards([
   ('do', 'You lose a ship', 'It happens', 'Say "GF", keep your comms clear and do not blame others. <a href="lose-my-ship.html">More on losses</a>.'),
   ('do', 'You make a mistake', 'Own it', 'Say it once, learn from it, move on. Nobody is perfect.'),
   ('do', 'You disagree', 'Wait', 'Raise it afterwards or send the FC feedback, not during the fight.'),
   ('do', 'Someone is rude', 'Do not feed it', 'Do not reply in kind. Tell the FC or host quietly if it continues.')]))]))

# ---------------------------------------------------------------- 6
PAGES.append(dict(
 slug='fleets-for-your-timezone', short='TIMEZONES', title='How to Find Fleets for Your Timezone',
 sub='Finding EU, US and AU fleets', status=[('EVE TIME', 'UTC'), ('REGIONS', 'EU / US / AU'), ('CHECK', 'THE CALENDAR')],
 tldr=f'<b>EVE time is UTC.</b> Fleets are announced in EVE time. Use the clock below to convert, then look for fleets that fit your evening on the <a href="{CAL}" target="_blank">calendar</a>. Hosts tend to cover different regions, so follow a few.',
 secs=[
  ('EVE time and your time', '''<p class="lead">EVE Online runs on UTC, called <b>EVE time</b>. All fleet times are quoted in it. Convert to your own timezone before you plan your evening.</p>
<div class="clockbox"><div class="c"><small>EVE TIME (UTC)</small><b id="cu">--:--:--</b></div><div class="c"><small>YOUR TIME <span id="tzn"></span></small><b id="cl">--:--:--</b></div></div>
<div class="conv"><span>Fleet starts at</span><input id="ch" type="number" min="0" max="23" value="19" style="width:90px"><span>:</span><input id="cm" type="number" min="0" max="59" value="00" style="width:90px"><span>EVE time</span><span>&rarr;</span><span class="out" id="co">--</span></div>'''),
  ('Typical regional windows', '''<p>These are broad guides to when each region tends to be active. Always check the calendar for the real times.</p>
<table><tr><th>Region</th><th>Typical fleet window (EVE time)</th><th>Notes</th></tr>
<tr><td>EU</td><td>Late afternoon to late evening, about 17:00 to 23:00</td><td>Often the busiest window, with the most fleets to choose from.</td></tr>
<tr><td>US</td><td>Evening in the Americas, about 00:00 to 04:00</td><td>Quieter than EU but a strong community. Many hosts run US-friendly slots.</td></tr>
<tr><td>AU / Asia-Pacific</td><td>Evening in Australia, about 08:00 to 12:00</td><td>Fewer fleets, so following AU hosts helps a lot.</td></tr></table>''' + note('These windows are indicative only and are not published rules. Hosts set their own times, and the calendar is always the source of truth.', 'IMPORTANT', True)),
  ('Local time reference', '''<p>Roughly what a 19:00 EVE time fleet looks like around the world. Daylight saving moves these by an hour.</p>
<table><tr><th>Where</th><th>19:00 EVE time is about</th></tr>
<tr><td>UK (winter)</td><td>19:00 &nbsp;<span class="chip">UTC+0</span></td></tr>
<tr><td>Central Europe (winter)</td><td>20:00 &nbsp;<span class="chip">UTC+1</span></td></tr>
<tr><td>US East (winter)</td><td>14:00 &nbsp;<span class="chip">UTC-5</span></td></tr>
<tr><td>US West (winter)</td><td>11:00 &nbsp;<span class="chip">UTC-8</span></td></tr>
<tr><td>Sydney (summer)</td><td>06:00 next day &nbsp;<span class="chip">UTC+11</span></td></tr></table>'''),
  ('Finding fleets for your hours', steps([
   ('Convert the fleet start time', 'Use the converter above, or add the calendar to your phone.'),
   ('Scan the calendar for your evening', f'Open the <a href="{CAL}" target="_blank">calendar</a> and look at the days you play. Note which hosts run in your window.'),
   ('Follow region-friendly hosts', 'Join the Discords of hosts whose fleets fit your timezone. They post reminders you can see.'),
   ('Ask in Discord', 'Ask "any US-time frigate fleets this week?" The community usually knows.'),
   ('Be ready to adapt', 'If nothing fits tonight, look at tomorrow, or try a weekend. Weekends often have more variety.')])),
  ('Tips for off-peak pilots', cards([
   ('do', 'Plan ahead', 'A week ahead', 'Fleets are advertised up to a week ahead. Pick the ones that suit you early.'),
   ('do', 'Prepare in advance', 'Stage early', 'Move ships to staging earlier in the day so you can undock on time.'),
   ('do', 'Support smaller fleets', 'Help them grow', 'Smaller regional fleets grow if pilots keep turning up.'),
   ('do', 'Watch for pop-ups', 'Ad-hoc fleets', 'Some hosts run short-notice fleets. Notifications on Discord help you catch them.')]))],
 script='tz'))

# ---------------------------------------------------------------- 7
PAGES.append(dict(
 slug='prepare-for-a-fleet', short='PREPARE', title='How to Prepare for a Fleet',
 sub='Ships, fittings, ammunition, clones and supplies', status=[('SHIP', 'FITTED'), ('CLONE', 'PVP'), ('HOME', 'STAGING')],
 tldr='<b>Right ship, correct fit, ammo, paste, drugs, boosters, drones, a PvP clone, and home station set to staging.</b> Do it all before the fleet starts. The checklist below saves your ticks in your browser.',
 secs=[
  ('Interactive pre-flight checklist', '<p>Tick each one off as you do it. Your progress is saved on this device.</p>' + checklist('prep', [
   ('Read the advert again', 'Time, staging, ship, comms'),
   ('Ship moved to staging', 'Do this days ahead, not minutes'),
   ('Right ship and correct fit', 'Check the doctrine or class'),
   ('Weapons loaded with the right ammo', 'Plus spare ammo in the cargo'),
   ('Nanite repair paste', 'For repairing modules in the field'),
   ('Boosters (drugs) if the fleet uses them', 'Check the advert, only if affordable'),
   ('Drones launched or in the bay', 'Right type and number'),
   ('PvP clone selected', 'Cheap implants, correct location'),
   ('Home station set to staging', 'So a pod-out returns you to the fleet'),
   ('Overview loaded', 'A PvP overview with hostiles clear'),
   ('Voice comms installed and tested', 'Mic, speakers, push-to-talk'),
   ('Cap booster / charges / scripts', 'If your fit uses them'),
   ('Know your ship', 'Speed, range, tank, EWAR')])),
  ('Your ship and fit', cards([
   ('do', 'Fly what the fleet wants', 'Doctrine', 'Match the advertised ship class or doctrine. A great ship that does not fit the plan is a bad ship.'),
   ('do', 'Check your fit twice', 'Before undock', 'Make sure everything is online, nothing is overheating and modules have charges.'),
   ('do', 'Know the limits', 'Your ship', 'Speed, weapon range, EWAR and drones. Know what you can and cannot do.'),
   ('do', 'Stay within your budget', 'Accept the loss', 'Cheap and cheerful. If a loss would sour your evening, fly something cheaper.')])),
  ('Ammunition and supplies', gloss([
   ('Ammo', 'Load your weapons and carry spares. Check your damage type and range choice with the FC.'),
   ('Nanite paste', 'Repairs damaged modules. Bring some.'),
   ('Boosters / drugs', 'Temporary buffs. Optional, but check the advert if the fleet suggests them.'),
   ('Drones', 'The right type and number. Check your drone bay.'),
   ('Cap charges / scripts', 'If your fit needs them, carry spares.'),
   ('Spare modules', 'Nice to have, rarely needed on a short roam.')])),
  ('Clones and implants', '<p>When you are podded, your clone matters. Plan it before you undock.</p>' + cards([
   ('do', 'Use a PvP clone', 'Cheap', 'Wear affordable implants for fleets. Do not risk your expensive skill or training implants.'),
   ('do', 'Home station at staging', 'Reship quickly', 'If you are podded, you wake up at staging and can reship and rejoin the fleet.'),
   ('do', 'Check jump clones', 'Where am I?', 'If you use jump clones, know which one you are in and where it is.'),
   ('dont', 'Do not fly with what you cannot lose', 'Rule 1', 'If it hurts to lose it, leave it in the hangar.')])),
  ('Timeline', tl([
   ('7 DAYS BEFORE', 'Find the fleet, read the advert, decide on a ship.'),
   ('2 DAYS BEFORE', 'Buy or fit the ship. Move it to staging. Set your home station.'),
   ('1 HOUR BEFORE', 'Check the advert for changes. Install and test comms. Load ammo, drones and paste.'),
   ('15 MINUTES BEFORE', 'Join the channel and voice comms. Overview loaded. Ship ready.'),
   ('FORM UP', 'Wait for the XUP call. Read the MOTD. Listen.')]))],
 script='check'))

# ---------------------------------------------------------------- 8
PAGES.append(dict(
 slug='when-you-join-fleet', short='ON JOINING', title='What to Do When You Join Fleet',
 sub='Mumble, fleet chat, broadcasts and following instructions', status=[('COMMS', 'LIVE'), ('MOTD', 'READ'), ('BROADCASTS', 'WATCHED')],
 tldr='<b>Join voice, read the MOTD, find your squad, load your overview, and watch fleet broadcasts.</b> Listen to the FC, follow instructions at all times, and keep voice chatter short.',
 secs=[
  ('First five minutes', steps([
   ('Check you are in the fleet', 'Open the fleet window. Confirm your name is listed and your role or squad is set.'),
   ('Read the MOTD', 'The MOTD in the fleet window holds the rules, comms and objectives. Read it fully before asking.'),
   ('Join voice comms', 'Each group lists its voice details. Mumble is commonly used. Join the right channel and test your sound.'),
   ('Open fleet chat', 'Keep the fleet channel visible. Questions go in text, orders go in voice.'),
   ('Check your overview', 'Make sure hostiles are visible, and you can sort by distance.'),
   ('Wait for orders', 'Stay docked or at the staging point until the FC says to undock.')]) + note('The NPSI how-to says each group\'s page lists its voice comms details, so set them up and test them in advance.', 'TIP')),
  ('Voice comms (Mumble and friends)', gloss([
   ('Get set up early', 'Install and test your voice client days before. Do not leave it to formup.'),
   ('Join the right channel', 'Follow the advert. There may be separate rooms for the FC, scouts and general fleet.'),
   ('Push-to-talk', 'Use push-to-talk so you do not broadcast background noise.'),
   ('Listen more than you talk', 'Silence helps the FC. Speak only when you have information to share.'),
   ('Keep it short', 'Say what, where, how many. Then stop.'),
   ('Stay muted when unsure', 'If you are not sure, stay quiet and ask in text.')])),
  ('Fleet broadcasts', '<p>Broadcasts are one-click signals in the fleet window. They are how the FC and fleet communicate without voice. Learn the common ones:</p>' + cards([
   ('do', 'Align To / Warp To', 'Movement', 'Do what it says, when told. Never warp to a broadcast without the FC saying.'),
   ('do', 'Target', 'Primary', 'The fleet is shooting this. Lock it and shoot if the FC has called it.'),
   ('do', 'Need Armor / Shield / Capacitor', 'Logistics', 'Pilots asking for repairs or cap. Logistics ships respond to these.'),
   ('do', 'In Position / Hold Position', 'Tactics', 'Tells the fleet to take their place or stay where they are.'),
   ('do', 'Jump To / Travel To', 'Travel', 'Follow the route. Make sure you are in the right system.'),
   ('dont', 'Broadcast spam', 'Avoid', 'Do not send broadcasts for fun. It confuses the fleet.')], 'g3') ),
  ('Following instructions', steps([
   ('Align when told', 'Align to the next gate or target as called. Be ready to warp.'),
   ('Warp on the FC\'s command', 'Wait for "warp" or a clear instruction, then go together as a fleet.'),
   ('Shoot the called target', 'Lock and fire on the primary. Do not pick your own unless told.'),
   ('Stay on grid', 'Stay with the fleet and within range of your logistics.'),
   ('Say if you cannot', 'If you lag, crash or lose comms, say so. The FC can adjust.'),
   ('Retreat when called', 'If the FC calls a retreat, go. Do not stay behind to fight alone.')]) + note('Follow commands at all times and do not backseat fly. If you want to suggest something, wait until after the fleet.', 'RULE')),
  ('Roles you can volunteer for', cards([
   ('do', 'Scout', 'Eyes ahead', 'Fly ahead and report what is in the next system. Very valuable.'),
   ('do', 'D-scan', 'Watch the edges', 'Run directional scan and call what you see.'),
   ('do', 'Scanner / prober', 'Find targets', 'Scan down hidden targets if you have the skills.'),
   ('do', 'Tackle', 'Hold them down', 'Scramblers and webs. Often a fast frigate role.')]))]))

# ---------------------------------------------------------------- 9
PAGES.append(dict(
 slug='lose-my-ship', short='LOSSES', title='What Happens If I Lose My Ship?',
 sub='Losses, replacement ships and expectations', status=[('LOSS', 'EXPECTED'), ('MOOD', 'GF'), ('REPLACEMENT', 'VARIES')],
 tldr='<b>You will lose ships. It is normal.</b> Fly what you can afford to lose, say "GF", and reship. Some hosts offer handouts or replacements (check the advert), but never assume. Losses are how you learn.',
 secs=[
  ('Losing ships is part of the game', '''<p class="lead">NPSI fleets are PvP, and PvP means ships die, on both sides. Nobody wins every fight. A loss is not a failure. It is how people learn and why the next fight feels good.</p>''' + cards([
   ('do', 'Normal', 'Expected', 'Every pilot, including experienced FCs, loses ships regularly.'),
   ('do', 'Cheap by design', 'Budget fits', 'Frigates and cruisers keep losses small, so you can fly again tomorrow.'),
   ('do', 'Part of the content', 'Memorable fights', 'The best stories usually involve someone exploding.'),
   ('do', 'Learning opportunities', 'Read the killmail', 'zKillboard shows what happened. Use it to improve.')])),
  ('What to do when your ship dies', steps([
   ('Stay calm', 'Take a breath. Do not rage in comms. The fight continues.'),
   ('Say "GF"', 'A quick "good fight" is the NPSI way, win or lose.'),
   ('Check your pod', 'If your capsule survived, warp it to safety or a station. Follow the FC if they give instructions.'),
   ('Get back to staging', 'If you were podded, you wake up in your home station, which should be staging.'),
   ('Reship', 'Fit a replacement and rejoin, if the fleet is still running and the FC is happy to have you.'),
   ('Learn from it', 'Look at the killmail later. Did you stay on grid? Did you know your range?')]) + note('Set your home station to the staging system so a pod-out puts you right where you need to be.', 'TIP')),
  ('Replacement ships and SRP', '''<p><b>SRP</b> (Ship Replacement Program) means a group pays for or replaces ships lost in their fleets. Some NPSI hosts do. Many do not.</p>''' + gloss([
   ('Always check the advert', 'It will say whether handouts or replacements are offered. For example, some fleets provide ships for pilots.'),
   ('Do not assume', 'If it is not mentioned, assume you are on your own.'),
   ('Handouts', 'Some fleets give out ships at staging so you can join easily. Use them if you need to.'),
   ('Ask politely', 'If unsure, ask in the host\'s channel before the fleet. Not during.'),
   ('Follow the rules', 'If SRP exists, follow the process. Do not expect payment otherwise.')]) + note('The NPSI how-to does not set out any universal replacement scheme. Replacement rules are set by each host.', 'IMPORTANT', True)),
  ('Reduce the pain', cards([
   ('do', 'Fly cheap', 'Budget', 'If you cannot afford the loss, do not fly it.'),
   ('do', 'Plan ahead', 'Think ahead', 'Keep a spare ship at staging and a spare fit saved, so reshipping takes seconds.'),
   ('do', 'Keep a reship ready', 'Spare', 'Bring a second ship to staging so you can rejoin fast.'),
   ('do', 'Follow orders', 'Survive longer', 'Staying with the fleet and following the FC is the best way to stay alive.')])),
  ('Handling the feeling', '''<p>Losing a ship can sting, especially the first time. That is okay.</p>''' + cards([
   ('do', 'Be a good sport', 'Attitude', 'A calm attitude after a loss is remembered by FCs and fleetmates.'),
   ('do', 'Talk about it', 'After the fleet', 'Ask what you could have done differently. People enjoy helping.'),
   ('dont', 'Do not blame others', 'Avoid', 'Complaining in comms hurts the fleet and your reputation.'),
   ('dont', 'Do not quit', 'Keep going', 'Everyone who is good at this lost a lot of ships first.')]))]))

# ---------------------------------------------------------------- 10
PAGES.append(dict(
 slug='become-a-regular', short='BECOME A REGULAR', title='How to Become a Regular NPSI Pilot',
 sub='Finding communities and building friendships', status=[('FLEETS', 'REGULAR'), ('FRIENDS', 'GROWING'), ('FC', 'MAYBE ONE DAY')],
 tldr='<b>Show up regularly, join a few communities, be friendly and reliable, and volunteer for roles.</b> The more you fly, the more names you recognise, and soon you will know half the fleet. Maybe you will lead one.',
 secs=[
  ('Make it a habit', steps([
   ('Pick a weekly slot', 'Choose one or two evenings that suit you. Regular pilots are the ones who build friendships.'),
   ('Try different hosts', f'NPSI.rocks lists over 20 hosts and roughly 30 to 50 fleets per week. Try several and see who you enjoy. <a href="{ABOUT}" target="_blank">About NPSI</a>.'),
   ('Join their Discord servers', 'Each host has a community. Say hello. People answer questions and invite you to fleets.'),
   ('Recognise names', 'Soon you will spot FCs and pilots you enjoy flying with. Follow them.'),
   ('Keep coming back', 'Consistency is the best way to become a known face.')])),
  ('Finding your communities', cards([
   ('do', 'Browse the host directory', 'NPSI.rocks', 'Learn what each host flies, when they fly, and which communities fit your style.'),
   ('do', 'Join the main Discord', 'Fleet announcements', f'Fleets and news are announced there. <a href="{DISCORD}" target="_blank">Join the Discord</a>.'),
   ('do', 'Follow partner groups', 'Variety', 'NPSI.rocks lists partners from many different groups, so there is something for every style.'),
   ('do', 'Watch streams and videos', 'Get a feel', 'Many fleets are streamed or recorded. Watch a few before you fly if you are nervous.')])),
  ('Building friendships', gloss([
   ('Be friendly in comms', 'Say hello, say thanks, say GF. It goes a long way.'),
   ('Learn names', 'Use names when you speak to people. It makes you memorable.'),
   ('Help new pilots', 'You were new once. Share what you have learned.'),
   ('Say thanks to FCs', 'FCs volunteer their time. A thank-you is always appreciated.'),
   ('Be reliable', 'If you say you will be there, be there. Reliability earns trust.'),
   ('Add people in-game', 'Add pilots you like to your contacts. You will spot them in fleet and on the calendar.')])),
  ('Level up', tl([
   ('FLEET 1', 'Show up, listen, follow the FC, enjoy it.'),
   ('FLEETS 2 TO 5', 'Start recognising names. Join a host\'s Discord. Try different ship classes.'),
   ('FLEETS 5 TO 15', 'Volunteer as a scout or D-scan. Give feedback on fleets. Help newer pilots.'),
   ('REGULAR', 'You know the FCs, they know you. You are part of the community.'),
   ('FC', f'Want to lead? The site has a "Becoming an NPSI FC" page linked in the footer of <a href="{HOME}" target="_blank">NPSI.rocks</a>.')])),
  ('Give back', cards([
   ('do', 'Fill in the feedback form', 'Two minutes', 'It helps FCs improve and makes fleets better for everyone.'),
   ('do', 'Share the fleets you enjoy', 'Spread the word', 'Tell friends. More pilots means better fleets.'),
   ('do', 'Support content creators', 'Streams and videos', 'Watch, follow and share the streamers and video makers who show NPSI fights.'),
   ('do', 'Keep it welcoming', 'The charter', f'Inclusion, not exclusion. <a href="{CHARTER}" target="_blank">Read the community charter</a>.')]) +
   '<div class="cmds"><div class="c"><b>Fly together</b><small>win together</small></div><div class="c"><b>No blues</b><small>no strings</small></div><div class="c"><b>Just content</b><small>see you out there</small></div></div>')]))

# ================================================================ templates
RINGS = '''<div id="rings"><svg viewBox="0 0 760 760"><g fill="none" stroke="#8a3ffc">
<circle class="pulsering" cx="380" cy="380" r="200" stroke-width="2"/>
<g class="r1"><circle cx="380" cy="380" r="370" stroke-width="1.5" stroke-dasharray="4 14" opacity=".7"/><circle cx="380" cy="380" r="355" stroke-width="5" stroke-dasharray="120 300" stroke="#b98bff"/></g>
<g class="r2"><circle cx="380" cy="380" r="310" stroke-width="2" stroke-dasharray="40 20 4 20" opacity=".8"/><circle cx="380" cy="380" r="295" stroke-width="8" stroke-dasharray="80 500" stroke="#a35cff"/></g>
<g class="r3"><circle cx="380" cy="380" r="250" stroke-width="1" stroke-dasharray="2 8"/><path d="M380 120 L400 150 L360 150 Z M380 640 L400 610 L360 610 Z" fill="#b98bff" stroke="none"/></g>
</g></svg></div><div class="br tl"></div><div class="br tr"></div><div class="br bl"></div><div class="br brr"></div>'''

TICK = 'NPSI.ROCKS  //  FLY TOGETHER, WIN TOGETHER  //  NOT PURPLE? SHOOT IT!  //  NO BLUES, NO STRINGS, JUST CONTENT  //  JOIN THE DISCORD  //  NULLSEC · SOLO · SMALL GANG PVP  //  '

HEAD = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{t} – NPSI.ROCKS How To</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{d}">
<link href="https://fonts.googleapis.com/css2?family=Oxanium:wght@400;600;800&family=Orbitron:wght@500;700;900&family=Rajdhani:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="howto.css">
<link rel="icon" href="logo.png">
</head><body>
'''

def topbar(cur):
    return ('<header id="top"><div class="in"><a class="lg" href="index.html"><img src="logo.png" alt="NPSI logo"></a>'
            '<a class="nm" href="index.html">NPSI.ROCKS<small>HOW TO NPSI</small></a>'
            '<nav><a href="index.html"' + (' class="on"' if cur == 'index' else '') + '>ALL GUIDES</a>'
            f'<a href="{CAL}" target="_blank">CALENDAR</a><a href="{DISCORD}" target="_blank">DISCORD</a></nav>'
            '<div class="feed"><span>BRIEFING</span><span class="dot"></span></div></div></header>')

FOOT = ('<footer class="f">NPSI.ROCKS // FLY TOGETHER, WIN TOGETHER</footer></div>'
        f'<div class="ticker"><div class="tickwrap"><div>{TICK*3}</div></div><div class="clock" id="clock">00:00:00 UTC</div></div>'
        '<script>const c=document.getElementById("clock");function t(){c.textContent=new Date().toISOString().substr(11,8)+" UTC"}t();setInterval(t,1000);</script>')

SCRIPTS = {
 'check': '''<script>(function(){var ul=document.querySelector('.check');if(!ul)return;var key='npsi_'+ul.dataset.store,saved=[];
try{saved=JSON.parse(localStorage.getItem(key)||'[]')}catch(e){}
var li=[].slice.call(ul.children);function upd(){var n=li.filter(function(x){return x.classList.contains('done')}).length;
document.getElementById('pt').textContent=n+' / '+li.length;document.getElementById('pf').style.width=(n/li.length*100)+'%';
try{localStorage.setItem(key,JSON.stringify(li.map(function(x,i){return x.classList.contains('done')?i:-1}).filter(function(i){return i>=0})))}catch(e){}}
li.forEach(function(x,i){if(saved.indexOf(i)>-1)x.classList.add('done');x.onclick=function(){x.classList.toggle('done');upd()}});upd()})();</script>''',
 'tz': '''<script>(function(){var cu=document.getElementById('cu'),cl=document.getElementById('cl'),tz=document.getElementById('tzn');
try{tz.textContent='('+Intl.DateTimeFormat().resolvedOptions().timeZone+')'}catch(e){}
function p(n){return String(n).padStart(2,'0')}
function tick(){var d=new Date();cu.textContent=d.toISOString().substr(11,8);cl.textContent=p(d.getHours())+':'+p(d.getMinutes())+':'+p(d.getSeconds())}
tick();setInterval(tick,1000);
var h=document.getElementById('ch'),m=document.getElementById('cm'),o=document.getElementById('co');
function conv(){var hh=Math.max(0,Math.min(23,+h.value||0)),mm=Math.max(0,Math.min(59,+m.value||0)),n=new Date();
var d=new Date(Date.UTC(n.getUTCFullYear(),n.getUTCMonth(),n.getUTCDate(),hh,mm));
var day=d.getDate()===n.getDate()?'today':(d>n?'tomorrow':'yesterday');
o.textContent=p(d.getHours())+':'+p(d.getMinutes())+' your time ('+day+')'}
h.oninput=m.oninput=conv;conv()})();</script>'''}

def page(i, pg):
    prev = PAGES[i-1] if i > 0 else None
    nxt = PAGES[i+1] if i < len(PAGES)-1 else None
    toc = ''.join(f'<a href="#s{n+1}">{s[0]}</a>' for n, s in enumerate(pg['secs']))
    body = ''.join(sec(n+1, s[0], s[1]) for n, s in enumerate(pg['secs']))
    st = ''.join(f'<span>{a} <b>{b}</b></span>' for a, b in pg['status'])
    pager = '<div class="pager">' + (f'<a href="{prev["slug"]}.html"><small>&larr; PREVIOUS</small><b>{prev["title"]}</b></a>' if prev else '<a href="index.html"><small>&larr; ALL GUIDES</small><b>How to NPSI index</b></a>') + \
            (f'<a class="nx" href="{nxt["slug"]}.html"><small>NEXT &rarr;</small><b>{nxt["title"]}</b></a>' if nxt else '<a class="nx" href="index.html"><small>DONE &rarr;</small><b>Back to all guides</b></a>') + '</div>'
    plain = html.unescape(''.join(c for c in pg['tldr'] if c))
    import re
    desc = re.sub('<[^>]+>', '', pg['tldr'])[:160]
    h = HEAD.format(t=pg['title'], d=html.escape(desc, quote=True)) + RINGS + topbar('') + '<div class="wrap">'
    h += (f'<section class="hero"><div class="kick"><i></i>GUIDE {i+1:02d} // {pg["short"]}</div><br>'
          f'<h1 class="title" data-t="{pg["title"]}">{pg["title"]}</h1>'
          f'<div class="sub">{pg["sub"]}<i>_</i></div><div class="bar"></div><div class="status">{st}</div>'
          f'<div class="toc" style="margin-top:26px">{toc}</div></section>')
    h += f'<section class="panel tldr"><h2><span>TL;DR</span>The short version</h2><p class="lead">{pg["tldr"]}</p></section>'
    h += body + pager + FOOT + SCRIPTS.get(pg.get('script'), '') + '</body></html>'
    return h

def index():
    cards_ = ''.join(
        f'<a href="{p["slug"]}.html" data-n="{i+1:02d}" class="{"first" if i == 0 else ""}" style="animation-delay:{i*.06}s"><b>{p["title"]}</b><span>{p["sub"]}</span></a>'
        for i, p in enumerate(PAGES))
    h = HEAD.format(t='How to NPSI', d='New pilot guides for NPSI public EVE Online fleets.') + RINGS + topbar('index') + '<div class="wrap">'
    h += ('<section class="hero"><div class="kick"><i></i>NEW PILOT BRIEFING</div><br>'
          '<h1 class="title" data-t="HOW TO NPSI">HOW TO NPSI</h1>'
          '<div class="sub">Not Purple Shoot It<i>_</i></div><div class="bar"></div>'
          '<div class="status"><span>GUIDES <b>10</b></span><span>DIFFICULTY <b>ROOKIE</b></span><span>COST <b>FREE</b></span></div></section>')
    h += ('<section class="panel tldr"><h2><span>START</span>New to public fleets?</h2><p class="lead">These guides walk you from "what is NPSI?" to flying regularly with new friends. '
          'Start with the first one, then jump to whatever you need.</p>'
          '<div class="cmds"><div class="c"><b>!discord</b><small>community</small></div><div class="c"><b>!npsi</b><small>website</small></div></div></section>')
    h += f'<div class="idx">{cards_}</div>'
    h += FOOT + '</body></html>'
    return h

os.makedirs(OUT, exist_ok=True)
for i, pg in enumerate(PAGES):
    open(os.path.join(OUT, pg['slug'] + '.html'), 'w').write(page(i, pg))
open(os.path.join(OUT, 'index.html'), 'w').write(index())
print('built', len(PAGES) + 1, 'pages')
