from content import add,p,ol,ul,note,table,link,PAGES
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import re
W=Path(__file__).resolve().parents[2]/'wiki'
# Editorial summaries and actionable instructions, supplemented by article-specific extracted reference notes.
categories={
'Getting Started':('Getting Started','Start here','✧','A guided introduction to the first moments on Ashenfall.'),
'Guide for new players':('New player survival handbook','Start here','✧','A practical checklist for your first several play sessions.'),
'First Steps':('First Steps walkthrough','Quest walkthroughs','⚑','Follow the tutorial and meet the characters who introduce Ashenfall.'),
'Ratcatcher':('Ratcatcher walkthrough','Quest walkthroughs','⚑','Learn basic combat with Vannaka before harder encounters.'),
'Rune Mysteries':('Rune Mysteries walkthrough','Quest walkthroughs','⚑','Learn how runes, essence and magical abilities fit together.'),
'Dragon Slayer':('Dragon Slayer walkthrough','Quest walkthroughs','⚑','Prepare for the early main-story dragon encounter.'),
'Withering Heights':('Withering Heights walkthrough','Quest walkthroughs','⚑','Enter Fellhollow and understand the curse-fragment objectives.'),
'Black Knight’s Fortress':('Black Knight’s Fortress walkthrough','Quest walkthroughs','⚑','Explore the fortress story without losing your bearings.'),
'Icthlarin’s Little Helper':('Icthlarin’s Little Helper','Quest walkthroughs','⚑','Understand this quest’s objectives and progression.'),
'Regicide':('Regicide walkthrough','Quest walkthroughs','⚑','A structured reference for the Regicide story quest.'),
'Saga':('The saga and story order','World & lore','◈','Follow the main adventure without mixing questlines.'),
'History':('History of Ashenfall','World & lore','◈','Understand the events and ruins behind the world.'),
'Gods':('Gods of RuneScape','World & lore','◈','A quick orientation to deities referenced across Ashenfall.'),
'Player Character':('Your character explained','Core systems','◇','Learn what belongs to your character and how progression works.'),
'Inventory':('Inventory and equipment','Core systems','◇','Sort equipment, materials and supplies before each trip.'),
'Artisan':('Artisan and crafting progression','Core systems','◇','Make sense of artisan activity and processing stations.'),
'Agility':('Agility training basics','Skills deep dives','✦','Move confidently and understand agility progression.'),
'Fishing':('Fishing: nets and rods','Skills deep dives','✦','Learn the difference between net fishing and rod fishing.'),
'Mining':('Mining and ore tiers','Skills deep dives','✦','Find mineable deposits and plan better ore runs.'),
'Woodcutting':('Woodcutting and timber','Skills deep dives','✦','Choose the right axe and gather useful logs.'),
'Construction':('Construction skill','Skills deep dives','✦','Develop useful building skills and improve your camp.'),
'Magic':('Magic skill explained','Skills deep dives','✦','Learn the role of spell unlocks and rune resources.'),
'Combat':('Combat skill explained','Skills deep dives','✦','Understand progression, stamina and readiness.'),
'Skills':('Skills and milestones','Skills deep dives','✦','Where to view levels, skill trees and milestones.'),
'Furnace':('Furnace: smelt your first bars','Crafting stations','⚒','Turn mined ore into metal bars using a furnace.'),
'Kiln':('Kiln: make charcoal','Crafting stations','⚒','Prepare fuel and materials for smelting.'),
'Blacksmith’s Bench':('Blacksmith’s Bench','Crafting stations','⚒','Find the right place to forge metal equipment.'),
'Armour Bench':('Armour Bench','Crafting stations','⚒','Craft armour using the correct resources and unlocks.'),
'Fletching Bench':('Fletching Bench','Crafting stations','⚒','Prepare bows, arrows and other ranged equipment.'),
'Jeweler’s Bench':('Jeweler’s Bench','Crafting stations','⚒','Work toward jewellery and related equipment.'),
'Loom':('Loom: process fibres','Crafting stations','⚒','Turn gathered fibres into practical materials.'),
'Spinning Wheel':('Spinning Wheel','Crafting stations','⚒','Process fibres as part of your crafting chain.'),
'Tannery':('Tannery: process hides','Crafting stations','⚒','Prepare leather from animal materials.'),
'Cooking Range':('Cooking Range and food','Crafting stations','⚒','Cook ingredients and prepare journey supplies.'),
'Mystic Forge':('Mystic Forge','Crafting stations','⚒','Learn about specialised magical equipment crafting.'),
'Rune Altar':('Rune Altar and runecrafting','Crafting stations','⚒','Convert gathered magical resources into useful runes.'),
'Buildings':('Building pieces and facilities','Crafting stations','⌂','Find out which kinds of structures support your settlement.'),
}
steps={
'Fishing':['Craft a coarse net and follow the Shrimp Catcher introduction.','Find a net fishing spot and equip your net.','Use the Trawl action near the spot; each attempt consumes stamina.','For rod fishing, equip a suitable rod, cast into a rod fishing spot, then respond to the fish’s movement and reel when prompted.'],
'Furnace':['Collect tin or copper ore to unlock the furnace recipe, if not already unlocked.','Build the furnace after checking its materials and placement requirements.','Produce charcoal using a kiln and load it as fuel.','Place suitable ores in the furnace, start processing and collect finished metal bars.'],
'First Steps':['Speak to the Wise Old Man at the temple and accept his introduction.','Follow the introductory activities to meet Doric and Vannaka.','Use the quests and Journal to complete the gathering, crafting and combat lessons.','Meet the Wise Old Man in Bramblemead Village to continue the main story.'],
'Withering Heights':['Complete Dragon Slayer and begin Withering Heights with the Wise Old Man near Ashien’s Watch.','Enter the Forgotten Temple and travel onward to Fellhollow.','Follow the route past the Wither water, watching for soul-rift hazards and purification fountains.','Find Cathan and investigate the three required curse fragments.','Use the objectives shown in your Journal to complete shrine and barrier puzzles before approaching Imaru’s Tower.'],
'Mining':['Check the recipe you are gathering ore for.','Equip a pickaxe that meets the deposit’s tier requirement.','Mine the correct deposit and check your remaining inventory space.','Take gathered ores to an appropriate smelting station when ready.'],
'Woodcutting':['Equip a suitable axe and choose a tree that matches its tier.','Gather the right wood for your current recipe or building piece.','Watch durability and carrying capacity.','Return to camp and process or store logs for future projects.'],
'Rune Altar':['Check the spell or recipe to determine which runes you need.','Collect the appropriate magical resources and required materials.','Interact with the rune altar and select the available rune recipe.','Craft what you need and check your inventory before leaving camp.'],
'Kiln':['Gather the ingredients required by the kiln recipe.','Build or find a kiln, confirming that it is accessible.','Load its appropriate input and start the process.','Collect charcoal for the furnace or another processing recipe.'],
}
for raw,(title,group,icon,desc) in categories.items():
 file=next((x for x in W.glob('*.html') if x.name.split(' - RuneScape')[0].replace("'",'’')==raw),None)
 if not file: print('missing',raw);continue
 soup=BeautifulSoup(file.read_text(errors='ignore'),'html.parser'); root=soup.select_one('.mw-parser-output')
 paras=[]
 if root:
  for el in root.find_all('p',recursive=False):
   t=el.get_text(' ',strip=True)
   t=re.sub(r'\[\s*\d+\s*\]','',t)
   if len(t)>75 and not ('This information is based on' in t) and len(t)<1250:paras.append(t)
 excerpt=paras[0] if paras else 'See the linked wiki reference for exact in-game requirements.'
 excerpt=re.sub(r'\s+',' ',excerpt)[:650].rsplit(' ',1)[0]
 canonical=raw.replace('’',"'")
 wiki=canonical.replace(' ','_')
 how=steps.get(raw)
 if group=='Quest walkthroughs':
  intro=p('Use your in-game <strong>Journal</strong> to track the active objective. World state and quest stage can change what you see; the steps below are a route overview, not a guaranteed complete puzzle-by-puzzle solution.')
  advice=how or ['Open the Journal and choose this quest as your active objective.','Travel to the current objective marker and speak to the indicated character.','Read notes or dialogue before activating a puzzle or fighting a boss.','After each objective completes, check the Journal for the next location.','If you are playing together, coordinate major story encounters with your group.']
 elif group=='Crafting stations':
  intro=p('A station is useful only when the recipe is unlocked and you have the correct input materials. Check the Journal for exact ingredients and unlock conditions; recipes may change with updates.')
  advice=how or ['Find or build this station at an accessible crafting area.','Inspect the recipe you want to produce and identify missing materials.','Gather or process its inputs at any prerequisite stations.','Use the station interface to craft your item and collect the output.','Store excess materials in the correctly labelled communal chest.']
 else:
  intro=p('This entry is designed to help you get started without being overwhelmed. For full item stats, level tables and exact unlock thresholds, use the full wiki page linked at the bottom.')
  advice=how or ['Open your Journal, skills menu or inventory and inspect the relevant unlocks.','Pick a small achievable goal or recipe that uses this system.','Gather the tools and materials you need, then practise somewhere safe.','Check the output and your progress before travelling to a more difficult area.']
 sections=[('At a glance',intro+p(escape(excerpt))+note('This page is a player-friendly overview based on the supplied RuneScape: Dragonwilds wiki snapshot. Confirm exact requirements against the live game and the full linked article.','Wiki reference')),('What to do',ol([escape(a) for a in advice])),('Practical advice for DragonInfinity',ul(['Check the server rules before changing shared builds, supplies or the world state.','If an activity seems unavailable, check your Journal, recipe unlocks and equipped tool tier.','Use the search bar to find related topics and the wiki link below for a more detailed reference.'])+p('For help with supplies and preparation, read '+link('resources','Resource gathering')+', '+link('crafting','Crafting')+' and '+link('troubleshooting','Troubleshooting')+'.'))]
 slug='wiki-'+re.sub('[^a-z0-9]+','-',canonical.lower()).strip('-')
 add(slug,title,group,desc,sections,[wiki],[],icon,[])
print('Added',len(categories),'wiki-derived guides; total',len(PAGES))
