import os

path = os.path.join(r'h:\Antigravity\Ahoy Matey\Wayfinder_Sourcebook', '10_DM_Appendix.md')
with open(path, 'a', encoding='utf-8') as file:
    file.write('\n## NPC Captains and Villain Builds\n')
    file.write('To seamlessly integrate Captain\'s Techniques into your campaign, you can assign them to notable NPCs and recurring villains.\n\n')
    file.write('### Low-Level Rival: The Upstart Corsair (CR 4)\n')
    file.write('- **Role:** Aggressive privateer or early campaign antagonist.\n')
    file.write('- **Techniques:** Find the Weak Board (Least Corsair), Sea Legs (Least Seamanship).\n')
    file.write('- **Tactics:** Relies on aggressive boarding actions and environmental hazards to overwhelm the party\'s ship.\n\n')
    file.write('### Mid-Level Antagonist: The Fleet Commander (CR 10)\n')
    file.write('- **Role:** Leader of a regional naval force or pirate armada.\n')
    file.write('- **Techniques:** Crew Rotation (Least Fleet), Captain\'s Challenge (Least Duelist), plus Lesser Fleet techniques.\n')
    file.write('- **Tactics:** Engages at scale, using formations and coordinated bombardments before closing for a dramatic duel.\n\n')
    file.write('### Legendary Villain: The Immortal Pirate King (CR 19)\n')
    file.write('- **Role:** Campaign-ending threat with world-shaping influence.\n')
    file.write('- **Techniques:** Reserve the Hold (Least First Captain), Whispering Compass (Least Mystic), plus Greater and Legendary Corsair/First Captain techniques.\n')
    file.write('- **Tactics:** Operates on a strategic level, controlling factions and impossible routes. Rarely fights directly unless backed by overwhelming supernatural support.\n\n')
    
    file.write('## Treasure Considerations\n')
    file.write('When awarding treasure to a party with a Wayfinder, consider items that enhance their chosen techniques rather than just raw stats. For example, a spyglass that grants bonus uses of *Chart the Unknown* or an enchanted cutlass that augments the *Captain\'s Challenge* technique.\n')
print('Updated DM Appendix.')
