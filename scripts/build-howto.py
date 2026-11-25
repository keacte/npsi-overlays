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

PAGES.append(dict(
 slug='what-is-npsi', short='THE BASICS', title='What Is NPSI?',
 sub='Not Purple Shoot It explained', status=[('PURPLE', 'FRIEND'), ('NOT PURPLE', 'TARGET'), ('STRINGS', 'NONE')],
 tldr='<b>NPSI = Not Purple Shoot It.</b> Pilots in the fleet appear <b>purple</b> on your overview. Anything that is not purple is a valid target. It is public, open to everyone, with no blues and no strings: <i>just content</i>.',
 secs=[
  ('The idea', '''<p class="lead">NPSI is a style of public PvP fleet. You do not need to be blue to anyone. You fly with whoever is in the fleet: if they are purple they are on your side, and if it is not purple, shoot it.</p>
<div class="g3"><div class="card do"><b>Purple</b><small>In fleet</small><p>Friends. Do not shoot, and protect them.</p></div>
<div class="card dont"><b>Not purple</b><small>Everyone else</small><p>Valid targets. The FC tells you what to shoot first.</p></div>
<div class="card"><b>No strings</b><small>No commitments</small><p>No standings, no corp application, no obligations. Just show up.</p></div></div>''' + note('"Not purple? Shoot it!" and "No blues, no strings, just content!" is how NPSI.rocks describes it.', 'FROM THE SITE')),
  ('Why people love it', cards([
   ('do', 'Accessible PvP', 'For new pilots', 'You do not need to be an expert, or in a big alliance, to get into fights.'),
   ('do', 'Meet people', 'Community', 'You meet pilots from many groups and learn from different FCs.'),
   ('do', 'Variety', 'Different every night', 'Frigates one day, battlecruisers the next, in different parts of space.'),
   ('do', 'Real content', 'Fun to watch', 'Many NPSI fleets are streamed and recorded.')])),
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
   ('Tackle', 'Ships that hold targets down so the fleet can kill them.'),
   ('D-scan', 'Directional scanner. Finds ships nearby, even if not on grid.'),
   ('Broadcast', 'Fleet signals like Align To, Warp To and Target.'),
   ('SRP', 'Ship Replacement Program. Some groups replace lost ships. Check the advert.'),
   ('GF', 'Good fight. Say it after a fight, win or lose.')]))]))

PAGES.append(dict(
 slug='what-is-npsi-rocks', short='THE HUB', title='What Is NPSI.rocks?',
 sub='The central hub for public EVE fleets', status=[('HUB', 'CENTRAL'), ('COST', 'FREE'), ('LOGIN', 'NOT NEEDED')],
 tldr=f'<a href="{HOME}" target="_blank">NPSI.rocks</a> is <b>the central hub for public EVE Online fleets</b>. It lists upcoming fleets from many hosts in one calendar, shows who runs them, and helps the community find, schedule and celebrate NPSI content.',
 secs=[
  ('What it is', f'''<p class="lead">NPSI.rocks is the home of the NPSI Community Gateway. Instead of searching a dozen Discords for tonight's fleet, you open one site and see everything.</p>
{cards([
 ('do', 'Calendar', 'npsi.rocks/calendar', f'Every upcoming fleet from every host. <a href="{CAL}" target="_blank">Open it</a>.'),
 ('do', 'Hosts', 'Who runs fleets', 'A directory of the communities that host NPSI content, so you can find a style you like.'),
 ('do', 'Leaderboards', 'Bragging rights', 'Pilot kill rankings, including weekly top lists.'),
 ('do', 'News', 'What is new', 'Announcements from the gateway and community.')])}'''),
  ('What you will find on it', gloss([
   ('Upcoming fleets', 'A list of fleets coming up in the next week, with host, FC, staging and time.'),
   ('Roam reports', 'Results from past fleets, such as ISK destroyed and the FC who led them.'),
   ('How to NPSI', f'A short new-pilot page. <a href="{HOWTO}" target="_blank">Read it</a>.'),
   ('Community charter', f'The values behind the site. <a href="{CHARTER}" target="_blank">Read it</a>.'),
   ('Discord bot', 'Fleet announcements are delivered through the Fluffy bot in Discord.'),
   ('Becoming an NPSI FC', 'An application page for anyone who wants to lead fleets. Linked from the site footer.')])),
  ('How it works', steps([
   ('Hosts post fleets', 'Communities add their fleets to the central calendar.'),
   ('The calendar collects them', 'Everything appears in one place, in EVE time.'),
   ('Discord spreads the word', 'Announcements and reminders go out through the NPSI Discord and the Fluffy bot.'),
   ('Pilots turn up', 'You pick a fleet, prepare and join. No sign-up on the site is needed to fly.'),
   ('Feedback closes the loop', 'After a roam, pilots fill in the fleet feedback form, which helps FCs improve.')])),
  ('The numbers', '<p>According to the About page there are <b>over 20 NPSI hosts</b> and roughly <b>30 to 50 fleets each week</b>. Partners include F.U.N. Inc., EVE LinkNet, Spectre Fleet, The Morgue, Bombers Bar and more, so there is a wide range of styles.</p>' + note('The site is run as an EVE partner project and promotes variety, visibility and inclusivity of NPSI public content.', 'CHARTER')),
  ('How to use it', cards([
   ('do', 'Check it before you play', 'Daily', 'Open the calendar to see what is on tonight and this week.'),
   ('do', 'Follow hosts you like', 'Discord', f'Join the Discord for reminders. <a href="{DISCORD}" target="_blank">Join here</a>.'),
   ('do', 'Read roam reports', 'Learn', 'See how fleets went and which FCs run the style you like.'),
   ('do', 'Share it', 'Spread the word', 'Tell new pilots. More pilots means more and better fleets.')]))]))

PAGES.append(dict(
 slug='how-to-get-involved', short='HOW', title='How to Get Involved',
 sub='Find a fleet, join it and fly', status=[('STEPS', 'SIX'), ('SIGN-UP', 'NONE'), ('INVITE', 'FROM FC')],
 tldr=f'Find a fleet on the <a href="{CAL}" target="_blank">calendar</a>, read the advert, move your ship to staging, join the host\'s comms, then <b>XUP when the FC asks</b>. That is all it takes.',
 secs=[
  ('The six steps', steps([
   ('Find a fleet', f'Open the <a href="{CAL}" target="_blank">NPSI calendar</a>. Pick something that suits your ship and your time.'),
   ('Read the advert', 'Check staging system, start time, ship or doctrine, and the comms and channel to use.'),
   ('Prepare your ship', 'Right ship, correct fit, ammo, paste, drugs, boosters, drones, a PvP clone. <a href="surviving-your-first-fleet.html">Checklist &rarr;</a>'),
   ('Move to staging', 'Do this in the days before, and set your home station there.'),
   ('Join comms and XUP', 'Be in the right channel early. When the FC asks, type <b>x</b> with your ship, for example "x Caracal".'),
   ('Accept the invite and follow the FC', 'Read the MOTD, then listen and follow instructions.')])),
  ('Reading a fleet advert', gloss([
   ('Fleet name', 'Hints at the ship class or theme.'),
   ('Host and FC', 'The community and the Fleet Commander leading it.'),
   ('Staging system', 'Where to bring your ship. The most important detail.'),
   ('Start time', 'Given in EVE time (UTC). <a href="when-to-get-involved.html">Convert it &rarr;</a>'),
   ('Ship / doctrine', 'What to fly. Some fleets are "bring anything", some are strict.'),
   ('Handouts', 'Some hosts provide ships. Check, do not assume.')])),
  ('What XUP means', '''<p><b>XUP</b> means "I am ready, here is my ship". It lets the FC see who is available and which ships are coming.</p>
<div class="g3"><div class="card"><b>Format</b><small>Usually</small><p><span class="chip">x Caracal</span> or xup plus your ship.</p></div>
<div class="card"><b>When</b><small>Only on call</small><p>Wait until the FC asks. Early messages clutter the channel.</p></div>
<div class="card"><b>After</b><small>Be patient</small><p>You may wait a few minutes. Stay in comms and watch for invites.</p></div></div>'''),
  ('Your first fleet: picking well', cards([
   ('do', 'Pick a friendly format', 'Beginner-safe', 'Frigate and cruiser roams are cheap, fast and forgiving.'),
   ('do', 'Pick a time you can finish', 'Commit', 'A roam can run a couple of hours. Do not join if you must leave soon.'),
   ('do', 'Pick a ship you can afford to lose', 'Budget', 'Cheap fits are a feature, not a flaw.'),
   ('dont', 'Avoid fleets you cannot reach', 'Logistics', 'If staging is many jumps away, choose another fleet.')])),
  ('If something goes wrong', gloss([
   ('No invite arrived', 'Check you are in the correct channel and used the right XUP format. Politely ask the FC, once.'),
   ('Wrong staging system', 'Tell the channel. Experienced pilots will help you catch up.'),
   ('Late to formup', 'Message the channel, say where you are and ask if you can catch up.'),
   ('Unsure what to fly', 'Ask which ship class fits the roam. The right role beats your favourite ship.')]) + note('Never be afraid to ask. FCs would rather answer a question than lose a pilot to confusion.', 'TIP'))]))

PAGES.append(dict(
 slug='when-to-get-involved', short='WHEN', title='When to Get Involved',
 sub='Finding fleets at your time of day', status=[('EVE TIME', 'UTC'), ('REGIONS', 'EU / US / AU'), ('LEAD TIME', 'UP TO A WEEK')],
 tldr=f'<b>EVE time is UTC.</b> Fleets are advertised up to a week ahead in EVE time. Convert with the clock below, check the <a href="{CAL}" target="_blank">calendar</a>, and follow hosts whose times suit you.',
 secs=[
  ('EVE time and your time', '''<p class="lead">EVE Online runs on UTC, called <b>EVE time</b>. Fleet times are quoted in it. Convert to your timezone before you plan your evening.</p>
<div class="clockbox"><div class="c"><small>EVE TIME (UTC)</small><b id="cu">--:--:--</b></div><div class="c"><small>YOUR TIME <span id="tzn"></span></small><b id="cl">--:--:--</b></div></div>
<div class="conv"><span>Fleet starts at</span><input id="ch" type="number" min="0" max="23" value="19" style="width:90px"><span>:</span><input id="cm" type="number" min="0" max="59" value="00" style="width:90px"><span>EVE time</span><span>&rarr;</span><span class="out" id="co">--</span></div>'''),
  ('Typical regional windows', '''<p>Broad guides to when each region tends to be active. Always check the calendar for real times.</p>
<table><tr><th>Region</th><th>Typical window (EVE time)</th><th>Notes</th></tr>
<tr><td>EU</td><td>About 17:00 to 23:00</td><td>Often the busiest window, with the most fleets to choose from.</td></tr>
<tr><td>US</td><td>About 00:00 to 04:00</td><td>Evening in the Americas. Many hosts run US-friendly slots.</td></tr>
<tr><td>AU / Asia-Pacific</td><td>About 08:00 to 12:00</td><td>Fewer fleets, so following AU hosts helps.</td></tr></table>''' + note('These windows are indicative only, not published rules. Hosts set their own times and the calendar is the source of truth.', 'IMPORTANT', True)),
  ('Local time reference', '''<p>What a 19:00 EVE time fleet looks like around the world. Daylight saving shifts these by an hour.</p>
<table><tr><th>Where</th><th>19:00 EVE time is about</th></tr>
<tr><td>UK (winter)</td><td>19:00 &nbsp;<span class="chip">UTC+0</span></td></tr>
<tr><td>Central Europe (winter)</td><td>20:00 &nbsp;<span class="chip">UTC+1</span></td></tr>
<tr><td>US East (winter)</td><td>14:00 &nbsp;<span class="chip">UTC-5</span></td></tr>
<tr><td>US West (winter)</td><td>11:00 &nbsp;<span class="chip">UTC-8</span></td></tr>
<tr><td>Sydney (summer)</td><td>06:00 next day &nbsp;<span class="chip">UTC+11</span></td></tr></table>'''),
  ('A fleet\'s timeline', tl([
   ('A WEEK BEFORE', 'The fleet is advertised on the calendar and in Discord.'),
   ('DAYS BEFORE', 'Decide on a ship, move it to staging, set your home station.'),
   ('1 HOUR BEFORE', 'Check the advert for changes. Test comms. Load ammo and drones.'),
   ('15 MINUTES BEFORE', 'Join the channel and voice. Ship ready.'),
   ('FORM UP', 'The FC calls XUP. Read the MOTD. Listen.')])),
  ('Never miss one', steps([
   ('Convert the time', 'Use the converter above or add the fleet to your phone calendar.'),
   ('Scan the calendar for your evenings', f'Open the <a href="{CAL}" target="_blank">calendar</a> and look at the days you play.'),
   ('Follow hosts in your window', 'Join the Discords of hosts whose fleets fit your timezone.'),
   ('Check again before you go', 'Times and staging can change. Re-read the advert on the day.')]))],
 script='tz'))

PAGES.append(dict(
 slug='surviving-your-first-fleet', short='SURVIVE', title='Surviving Your First Fleet',
 sub='Prepare, fly, lose a ship, come back', status=[('SHIP', 'FITTED'), ('CLONE', 'PVP'), ('LOSSES', 'EXPECTED')],
 tldr='<b>Right ship, correct fit, ammo, paste, drugs, drones, a PvP clone, home station at staging.</b> Stay with the fleet, follow the FC, and when you lose a ship, say GF and reship. It is part of the game.',
 secs=[
  ('Pre-flight checklist', '<p>Tick each one off. Your progress is saved on this device.</p>' + checklist('prep', [
   ('Read the advert again', 'Time, staging, ship, comms'),
   ('Ship moved to staging', 'Do this days ahead, not minutes'),
   ('Right ship and correct fit', 'Check the doctrine or class'),
   ('Weapons loaded with the right ammo', 'Plus spare ammo in the cargo'),
   ('Nanite repair paste', 'For repairing modules in the field'),
   ('Boosters (drugs) if the fleet uses them', 'Check the advert, only if affordable'),
   ('Drones ready', 'Right type and number'),
   ('PvP clone selected', 'Cheap implants'),
   ('Home station set to staging', 'So a pod-out returns you to the fleet'),
   ('Overview loaded', 'A PvP overview with hostiles clear'),
   ('Voice comms installed and tested', 'Mic, speakers, push-to-talk'),
   ('Know your ship', 'Speed, range, tank, EWAR')])),
  ('Staying alive', steps([
   ('Stay with the fleet', 'Stay on grid and near your logistics. Lone pilots die first.'),
   ('Follow the FC', 'Align, warp and shoot when told, not before.'),
   ('Know your ship', 'Speed, weapon range, EWAR and drones. Know your limits.'),
   ('Watch the overview', 'Keep an eye on what is on grid and what is targeting you.'),
   ('Retreat when called', 'If the FC calls a retreat, go. Do not stay behind alone.')])),
  ('Clones and implants', cards([
   ('do', 'Use a PvP clone', 'Cheap', 'Wear affordable implants. Do not risk expensive ones.'),
   ('do', 'Home station at staging', 'Reship quickly', 'If podded, you wake up at staging and can rejoin.'),
   ('do', 'Check jump clones', 'Where am I?', 'Know which clone you are in and where it is.'),
   ('dont', 'Do not fly what you cannot lose', 'Rule 1', 'If it would hurt to lose it, leave it in the hangar.')])),
  ('When you lose your ship', '<p>NPSI is PvP, so ships die. It is normal for every pilot, including experienced FCs.</p>' + steps([
   ('Stay calm', 'Do not rage in comms. The fight continues.'),
   ('Say "GF"', 'A quick good fight is the NPSI way, win or lose.'),
   ('Save your pod', 'If your capsule survived, warp it to safety or follow the FC.'),
   ('Reship and rejoin', 'Fit a replacement and come back if the fleet is still running and the FC agrees.'),
   ('Learn from it', 'Look at the killmail later. Did you stay on grid? Did you know your range?')])),
  ('Replacements and SRP', '<p><b>SRP</b> (Ship Replacement Program) means a group replaces ships lost in their fleets. Some NPSI hosts do. Many do not.</p>' + gloss([
   ('Check the advert', 'It says whether handouts or replacements are offered.'),
   ('Do not assume', 'If it is not mentioned, assume you are on your own.'),
   ('Ask early', 'If unsure, ask in the host\'s channel before the fleet, not during.'),
   ('Fly cheap', 'If a loss would sour your evening, fly something cheaper.')]) + note('Replacement rules are set by each host. There is no single NPSI scheme.', 'IMPORTANT', True)),
  ('After the fleet', cards([
   ('do', 'Say thanks', 'FCs volunteer', 'A thank-you is always appreciated.'),
   ('do', 'Fill in the feedback form', 'Two minutes', 'It helps FC development and improves NPSI fleets.'),
   ('do', 'Replace your ship', 'Ready for next time', 'Restock ammo and paste so you can undock fast.'),
   ('do', 'Book the next one', 'Keep going', 'Everyone good at this lost a lot of ships first.')]))],
 script='check'))

PAGES.append(dict(
 slug='getting-involved', short='COMMUNITY', title='Getting Involved',
 sub='From first fleet to regular pilot', status=[('FLEETS', 'REGULAR'), ('FRIENDS', 'GROWING'), ('FC', 'MAYBE ONE DAY')],
 tldr='<b>Show up regularly, join a few communities, be friendly and reliable, and volunteer for roles.</b> The more you fly, the more names you know. Maybe you will lead a fleet one day.',
 secs=[
  ('Make it a habit', steps([
   ('Pick a weekly slot', 'Choose one or two evenings. Regular pilots are the ones who build friendships.'),
   ('Try different hosts', f'NPSI.rocks lists over 20 hosts and roughly 30 to 50 fleets a week. Try several. <a href="{ABOUT}" target="_blank">About NPSI</a>.'),
   ('Join their Discord servers', 'Each host has a community. Say hello. People answer questions and invite you to fleets.'),
   ('Recognise names', 'Soon you will spot FCs and pilots you enjoy flying with. Follow them.'),
   ('Keep coming back', 'Consistency is the best way to become a known face.')])),
  ('Finding your communities', cards([
   ('do', 'Browse the host directory', 'NPSI.rocks', 'See what each host flies, when, and which style fits you.'),
   ('do', 'Join the main Discord', 'Announcements', f'Fleets and news are announced there. <a href="{DISCORD}" target="_blank">Join the Discord</a>.'),
   ('do', 'Follow partner groups', 'Variety', 'NPSI.rocks lists partners from many groups, so there is something for every style.'),
   ('do', 'Watch streams and videos', 'Get a feel', 'Watch a few fleets before you fly if you are nervous.')])),
  ('Building friendships', gloss([
   ('Be friendly in comms', 'Say hello, say thanks, say GF.'),
   ('Learn names', 'Using names makes you memorable.'),
   ('Help new pilots', 'You were new once. Share what you have learned.'),
   ('Thank FCs', 'FCs volunteer their time.'),
   ('Be reliable', 'If you say you will be there, be there.'),
   ('Add people in-game', 'Add pilots you like. You will spot them in fleet and on the calendar.')])),
  ('Level up', tl([
   ('FLEET 1', 'Show up, listen, follow the FC, enjoy it.'),
   ('FLEETS 2 TO 5', 'Start recognising names. Join a host\'s Discord. Try different ship classes.'),
   ('FLEETS 5 TO 15', 'Volunteer as a scout or D-scan. Give feedback. Help newer pilots.'),
   ('REGULAR', 'You know the FCs, they know you.'),
   ('FC', f'Want to lead? The footer of <a href="{HOME}" target="_blank">NPSI.rocks</a> links to a "Becoming an NPSI FC" page.')])),
  ('Give back', cards([
   ('do', 'Fill in the feedback form', 'Two minutes', 'It helps FCs improve and makes fleets better.'),
   ('do', 'Share the fleets you enjoy', 'Spread the word', 'More pilots means better fleets.'),
   ('do', 'Support content creators', 'Streams and videos', 'Watch, follow and share the people who show NPSI fights.'),
   ('do', 'Keep it welcoming', 'The charter', f'Inclusion, not exclusion. <a href="{CHARTER}" target="_blank">Read the community charter</a>.')]) +
   '<div class="cmds"><div class="c"><b>Fly together</b><small>win together</small></div><div class="c"><b>No blues</b><small>no strings</small></div><div class="c"><b>Just content</b><small>see you out there</small></div></div>')]))

PAGES.append(dict(
 slug='fleet-etiquette', short='ETIQUETTE', title='Fleet Etiquette',
 sub='How to fly well with strangers', status=[('EGOS', 'DOCKED'), ('ORDERS', 'FOLLOWED'), ('MOOD', 'FRIENDLY')],
 tldr='<b>Be on time, be prepared, listen to the FC and follow instructions.</b> Do not backseat fly. Be kind: everyone was new once, and the best fleets are ones people want to rejoin.',
 secs=[
  ('The golden rules', steps([
   ('Be on time', 'Arrive early and in the right ship. Late pilots slow everyone down.'),
   ('Be prepared', 'Correct fit, ammo, paste, drugs, clone and overview. Do it before the fleet.'),
   ('Listen to the FC', 'They make dozens of decisions a minute. Turn off distractions.'),
   ('Follow instructions at all times', 'Align when told, warp when told, shoot what is called. Argue afterwards.'),
   ('Read the MOTD first', 'Most questions are answered there.'),
   ('Be kind', 'Treat new pilots like you hoped to be treated.')])),
  ('Do and do not', '<div class="g2"><div class="card do"><b>Do</b><small>Be that pilot</small><ul>' + ''.join(f'<li>{x}</li>' for x in [
   'XUP when the FC asks', 'Keep chatter short and clear', 'Call out new hostiles with system and distance', 'Volunteer to scout, scan or D-scan',
   'Say thanks at the end', 'Stay on grid and with the fleet', 'Admit mistakes and move on', 'Help newer pilots']) +
   '</ul></div><div class="card dont"><b>Do not</b><small>Common mistakes</small><ul>' + ''.join(f'<li>{x}</li>' for x in [
   'Backseat fly or argue tactics', 'Talk over the FC', 'Break from the fleet', 'Spam chat or broadcasts',
   'Blame others after a loss', 'Ask what the MOTD already says', 'Rage when you lose a ship', 'Undock ahead of the fleet']) + '</ul></div></div>'),
  ('What FCs expect from you', cards([
   ('do', 'Reliability', 'Show up, stay', 'If you say you will join, join. If things change, say so.'),
   ('do', 'Awareness', 'Eyes open', 'Know your ship\'s speed, range, EWAR and drones, and your role.'),
   ('do', 'Flexibility', 'Adapt', 'Plans change. The FC may switch targets or retreat. Go with it.'),
   ('do', 'Feedback', 'After the fleet', 'Fill in the feedback form. It takes about two minutes.')]) + note(f'NPSI.rocks charter values: <i>variety, visibility, inclusivity</i> and "fly together, win together". <a href="{CHARTER}" target="_blank">Read the charter.</a>', 'COMMUNITY')),
  ('Following instructions', steps([
   ('Align when told', 'Align to the next gate or target as called. Be ready to warp.'),
   ('Warp on command', 'Wait for the call, then go together as a fleet.'),
   ('Shoot the called target', 'Lock and fire on the primary. Do not pick your own unless told.'),
   ('Say if you cannot', 'If you lag, crash or lose comms, tell the FC.'),
   ('Retreat when called', 'If the FC calls a retreat, go.')]) + note('Follow commands at all times and do not backseat fly. Suggestions can wait until after the fleet.', 'RULE')),
  ('When things go wrong', cards([
   ('do', 'You lose a ship', 'It happens', 'Say GF and keep comms clear. Do not blame others.'),
   ('do', 'You make a mistake', 'Own it', 'Say it once, learn from it, move on.'),
   ('do', 'You disagree', 'Wait', 'Raise it afterwards or in the feedback form.'),
   ('do', 'Someone is rude', 'Do not feed it', 'Do not reply in kind. Tell the FC or host quietly if it continues.')]))]))

PAGES.append(dict(
 slug='comms', short='COMMS', title='Comms',
 sub='Voice, fleet chat and broadcasts', status=[('MIC', 'PUSH-TO-TALK'), ('CHATTER', 'SHORT'), ('BROADCASTS', 'WATCHED')],
 tldr='<b>Set up and test your voice comms before the fleet.</b> Join the right channel, use push-to-talk, listen more than you talk, keep calls short, and watch the fleet broadcasts.',
 secs=[
  ('Voice comms', '''<p class="lead">Each group lists its voice comms details on its page, so set them up and test them in advance. Mumble is commonly used, but check the advert.</p>''' + gloss([
   ('Get set up early', 'Install and test your voice client days before, not at formup.'),
   ('Join the right channel', 'Follow the advert. There may be separate rooms for the FC, scouts and general fleet.'),
   ('Push-to-talk', 'Avoid open mics. Keyboard noise, music and background chatter do not help.'),
   ('Listen first', 'Most of the time your job is to listen.'),
   ('Stay muted when unsure', 'If you are not sure, stay quiet and ask in text.')])),
  ('How to make a call', '<p>Say <b>what, where, how many</b>. Then stop.</p>' + cards([
   ('do', 'Good call', 'Clear and short', '"Three hostile Caracals, Jita gate, 40 km."'),
   ('dont', 'Bad call', 'Vague and long', '"There are some ships, I think, and I am not sure where they went."'),
   ('do', 'Questions go in text', 'Keep voice clear', 'Voice is for fleet information. Ask questions in chat.'),
   ('do', 'Use the channel the FC asks for', 'Not private tells', 'Keep fleet talk in fleet channels.')])),
  ('Fleet chat and the MOTD', steps([
   ('Check you are in the fleet', 'Open the fleet window and confirm your name and squad.'),
   ('Read the MOTD', 'It holds the rules, comms and objectives for the roam. Read it before asking questions.'),
   ('Open fleet chat', 'Keep the fleet channel visible. Questions in text, orders in voice.'),
   ('XUP in the right channel', 'Use the channel named in the advert, and wait for the FC\'s call.')])),
  ('Fleet broadcasts', '<p>Broadcasts are one-click signals in the fleet window. They let the fleet communicate without voice.</p>' + cards([
   ('do', 'Align To / Warp To', 'Movement', 'Do what it says, when told. Never warp without the FC\'s say-so.'),
   ('do', 'Target', 'Primary', 'The fleet is shooting this. Lock it if the FC has called it.'),
   ('do', 'Need Armor / Shield / Capacitor', 'Logistics', 'Pilots asking for repairs. Logistics ships respond.'),
   ('do', 'In Position / Hold Position', 'Tactics', 'Take your place or stay where you are.'),
   ('do', 'Jump To / Travel To', 'Travel', 'Follow the route and check you are in the right system.'),
   ('dont', 'Broadcast spam', 'Avoid', 'Do not send broadcasts for fun. It confuses the fleet.')], 'g3')),
  ('Roles you can volunteer for', cards([
   ('do', 'Scout', 'Eyes ahead', 'Fly ahead and report what is in the next system.'),
   ('do', 'D-scan', 'Watch the edges', 'Run directional scan and call what you see.'),
   ('do', 'Scanner', 'Find targets', 'Scan down hidden targets if you have the skills.'),
   ('do', 'Tackle', 'Hold them down', 'Scramblers and webs. Often a fast frigate role.')])),
  ('Comms checklist', cards([
   ('do', 'Before the fleet', 'Days before', 'Install the voice client, test mic and speakers, find the channel.'),
   ('do', 'At formup', '15 minutes before', 'Join voice and text, read the MOTD, wait for XUP.'),
   ('do', 'During', 'Roam', 'Push-to-talk, short calls, watch broadcasts, follow the FC.'),
   ('do', 'After', 'Wrap-up', 'Say thanks and GF, then fill in the feedback form.')]))]))


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
          '<div class="status"><span>GUIDES <b>' + str(len(PAGES)) + '</b></span><span>DIFFICULTY <b>ROOKIE</b></span><span>COST <b>FREE</b></span></div></section>')
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
