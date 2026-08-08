# Chapter 27: Naval Combat & Ship Mechanics

The Shattered Expanse is a world of oceans, storms, and piracy. While standard combat excels at close-quarters skirmishes, simulating ship-to-ship combat requires a system that makes the vessel feel like a customizable fortress, while keeping the players—the officers—at the center of the action.

The system presented here is both **cinematic and deeply modular**. Rather than treating ships as static tokens, this system allows players to capture, retrofit, and build highly customized vessels using Weapon Slots and Upgrade Slots.

---

## 1. Ship Chassis & Size Categories

Every vessel in the Expanse is built upon a fundamental chassis, defined by its **Size Category**. A ship's size dictates its durability, speed, and how many modular upgrades and weapons it can support.

| Size Category | Description | Examples | Base HP | Base AC | Base Speed | Weapon Slots | Upgrade Slots | Minimum Crew |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Light / Skiff | Salvage Skiff, Dinghy | 50 | 12 | 50 ft. | 1 | 2 | 1-2 |
| **2** | Sloop / Escort | Smuggler's Sloop, Corvette | 150 | 15 | 60 ft. | 4 | 8 | 10 |
| **3** | Cutter / Brig | Heavy Cutter, Corsair Brig | 300 | 16 | 45 ft. | 12 | 15 | 40 |
| **4** | Galleon / Heavy Cargo | Merchant Galleon, Carrack | 600 | 14 | 30 ft. | 20 | 25 | 100 |
| **5** | Capital Vessel / Dreadnought | Experimental Ironclad, Flagship | 1,200 | 18 | 20 ft. | 40 | 50 | 300+ |
| **6** | Leviathan / Floating City | Sovereign Braid, Mobile Pirate Haven | 5,000 | 20 | 10 ft. | 100 | 150 | 5,000+ Population |

*Note: Base HP and AC represent a standard wooden hull. Precursor Plating or Magical Wards will modify these numbers.*

---

## 2. Weapon Slots & Naval Artillery

A ship's **Weapon Slots** represent the hardpoints available for mounting cannons, ballistas, or magical siege engines. Weapons take up a specific number of slots based on their size and power. When a Gunner takes the "Fire Artillery" Ship Action, they command a battery of installed weapons to fire simultaneously.

### Available Naval Artillery

| Weapon Module | Slots Required | Cost | Attack | Damage & Effect |
| :--- | :---: | :--- | :--- | :--- |
| **Light Swivel Gun** | 1 | 250 gp | Ranged Weapon (+5) | 2d8 Piercing. Range 100/400. Hits personnel as well as hulls. |
| **Standard Broadside Cannon** | 2 | 800 gp | Ranged Weapon (+6) | 3d10 Bludgeoning. Range 120/480. Standard ship-to-ship armament. |
| **Heavy Ballista** | 2 | 600 gp | Ranged Weapon (+6) | 4d8 Piercing. Range 150/600. Can be loaded with chain-shot to cripple rigging. |
| **Precursor Naval Cannon** | 4 | 2,500 gp | Ranged Weapon (+8) | 5d10 Bludgeoning + 1d10 Arcane. Range 200/800. Ignores standard wood hardness. |
| **Heavy Siege-Breaker Mortar** | 4 | 3,000 gp | Ranged AoE (DC 15 Reflex) | 6d10 Fire/Bludgeoning in a 40 ft radius. Range 400/1600. Long reload times (2 rounds). |
| **Experimental Aether-Beam** | 6 | Rare/Loot | Ranged Spell (+10) | 6d10 Force. Range 300/1200. Leaves lingering Aether-Burn on the target hull. |

---

## 3. Upgrade Slots & Ship Customization

A ship's **Upgrade Slots** represent the internal volume and structural hardpoints available for retrofits, magical wards, armor plating, and specialized facilities. 

### Common Upgrades

| Upgrade Module | Slots Required | Cost | Effect |
| :--- | :---: | :--- | :--- |
| **Smuggler's Compartment** | 2 | 1,000 gp | Adds a hidden cargo hold that requires a DC 20 Perception check to find. |
| **Diving Bell & Winch** | 3 | 1,500 gp | A pressurized sphere that can be lowered to the ocean floor, holding up to 4 Medium creatures. |
| **Captain's Extravagant Quarters** | 4 | 2,000 gp | Opulent furnishings. Grants the Captain a +2 circumstance bonus on Diplomacy and Intimidate checks while parleying in the cabin. |
| **Medical / Triage Bay** | 5 | 3,000 gp | Grants a +4 circumstance bonus on Heal checks. Crew natural healing rates double while aboard. |

### Heavy / Precursor Upgrades
*These upgrades often require specific salvaged materials, like Aether-Slag or intact Precursor Cores, and a Master Artificer to install.*

| Upgrade Module | Slots Required | Materials Needed | Effect |
| :--- | :---: | :--- | :--- |
| **Aether-Rammed Prow** | 5 | 50 Crates Aether-Slag | Adds +3d6 Force damage on successful naval ramming maneuvers. |
| **Masterwork Precursor Plating** | 10 | 50 Crates Aether-Slag | Replaces the hull with Precursor alloy. Grants +2 Hardness (Damage Reduction) and +10 to +50 HP depending on ship size. |
| **Violet Aether-Core Engine** | 15 | Pristine Violet Core | Ship no longer relies on wind. Grants +2 Speed (e.g. +20 ft), +1 Maneuverability, and a passive 20 HP Ward-Shield that regenerates daily. |
| **Sentential Drone Bay** | 4 | Salvaged Drone Core | Houses an aquatic drone that provides automated perimeter defense and underwater scouting. |

### City Districts (Size 6 Only)
*These massive installations turn a Dreadnought into a true Floating City. They consume vast amounts of space and require a permanent civilian population to operate.*

| District Module | Slots Required | Cost / Materials | Effect |
| :--- | :---: | :--- | :--- |
| **The Warrens (Slums)** | 10 | 10,000 gp | Basic civilian housing. Increases maximum population capacity by 1,000. Reduces city Morale if overcrowded. |
| **Merchant's Ward** | 15 | 25,000 gp | A sprawling bazaar. Generates a passive income of 1d4 x 1,000 gp per week, provided the ship visits populated waters to trade. |
| **Temple of the Four Energies** | 20 | Pristine Core + 50,000 gp | A monumental ziggurat channeling Arcane, Divine, Psionic, and Deep Magic. Grants massive city-wide wards (e.g. permanent *Control Weather* and *Forbiddance*). |
| **Precursor Forge District** | 20 | Automated Forge Module | A massive industrial zone. Allows the city to mint its own Precursor Naval Cannons and Aether-tech over time. |

---

## 4. Floating City Mechanics (Size 6)

When a vessel reaches Size 6 (Leviathan), it transcends standard naval combat. It operates on macro-scale mechanics:
1. **Population & Morale:** Instead of a Minimum Crew, the ship requires a **Population** to man the districts. The Captain must manage a **Morale Gauge** (1-100). If Morale drops below 30 (due to starvation, plague, or defeat in battle), riots break out in The Warrens, shutting down District modules.
2. **City Turns:** In ship-to-ship combat, a Size 6 vessel is too massive to maneuver like a sloop. It operates on "City Turns," acting at Initiative Count 20 and 10 to unleash devastating, synchronized broadsides across multiple batteries at once.
3. **Internal Ecosystem:** A Floating City must consume massive resources. Feeding 5,000 citizens requires specialized Upgrades (e.g., Hydroponic Gardens, Colossal Fishing Nets) or draining the Pirate Economy treasury weekly.
4. **Flotilla Mooring:** A Floating City does not expand by simply building higher wooden towers; it expands by consuming other ships. Allied or captured vessels (Sizes 1-4) can permanently moor themselves to the hull of a Size 6 vessel, physically lashing themselves to the main structure. Each permanently moored vessel adds its internal volume to the Floating City, allowing the Captain to install new City Districts inside the lashed hulls of the flotilla.

---

## 5. Officer Roles & Combat Flow

Naval combat happens in standard initiative. The ship itself does not roll initiative; instead, it moves and acts on the turn of the **Helmsman**. 

During combat, players take on specific **Officer Roles**. An officer can use their Standard Action to take a typical action (like casting a spell or making an attack), OR they can use their Standard Action to take a special **Ship Action** associated with their role.

### The Captain
The leader of the vessel, responsible for morale and coordination.
- **Standard Action - "Fire at Will!":** You grant a +2 bonus to all artillery attack rolls made by your ship until the start of your next turn.
- **Standard Action - "Brace for Impact!":** You shout a warning. Until the start of your next turn, the ship gains Damage Reduction (DR) 5/- against ship weapons or environmental hazards, and the crew gains a +4 bonus on saving throws to avoid being knocked prone.

### The Helmsman (Tide-Caller)
The one steering the ship. The ship moves on the Helmsman's turn.
- **Move Action - Move:** You use the ship's speed to move it across the battlefield.
- **Standard Action - "Hard to Port/Starboard!":** You make a DC 15 Profession (Sailor) check. On a success, the ship can immediately turn up to 90 degrees and move up to half its speed, avoiding an incoming hazard or lining up a perfect broadside.
- **Standard Action - Ramming Speed:** You move the ship in a straight line toward a target. If you hit, make an opposed Profession (Sailor) check or a melee attack. On a hit, both ships take 6d10 bludgeoning damage (modified by Aether-Rammed Prows or Precursor Plating).

### The Gunner
The master of the ship's artillery.
- **Standard Action - Fire Artillery:** You direct the crew to fire a battery of installed Weapon Modules. Make an attack roll for the battery. You can add your Base Attack Bonus and your Intelligence or Dexterity modifier to the attack roll instead of the ship's base modifier. (Having a Master Cannoneer officer grants a flat +2 to these rolls).
- **Standard Action - Targeted Shot:** You aim for a specific part of the enemy ship (e.g., the mast, the rudder). Make an artillery attack with a -4 penalty. If it hits, you cripple that component. (A crippled mast halves speed; a crippled rudder prevents turning).

### The Bosun (Artificer / Engineer)
The chief engineer and disciplinarian, keeping the ship and crew functioning.
- **Standard Action - Emergency Repairs:** You direct the damage control crew. Make a DC 15 Craft (ships) or Knowledge (engineering) check. On a success, the ship regains 4d10 Hull Points or a crippled system is temporarily bypassed.
- **Standard Action - Overclock Engine:** If the ship has an Aether-Core, you push the engines beyond their limits. The ship's speed increases by 30 feet until the end of the round, but the engine requires an Aether-Burn check or takes 1d10 damage from the strain.

---

## 6. Wayfinder Ship Bond Synergy

Wayfinder Corsairs possess the **Ship Bond** class feature. When a Wayfinder acts as the Captain of a vessel, the ship transcends its mechanical limitations:
1. **Magical Evasion:** The ship can substitute the Wayfinder's AC bonuses or saving throws for its own when subjected to magical or broadside attacks.
2. **Support Crew Multiplier:** A Wayfinder's crew acts with supernatural coordination. Even massive Capital Vessels (Size 5) can be operated effectively by a skeleton crew of magically bound sailors without suffering the standard penalties for being undercrewed.
