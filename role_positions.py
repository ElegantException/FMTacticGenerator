#role_positions.py
ROLE_CATEGORIES = {
    # 🧤 Goalkeepers
    "Goalkeeper": "Goalkeeper",
    "Sweeper Keeper": "Goalkeeper",

    # 🛡️ Defenders
    "Central Defender": "Defender",
    "Ball-Playing Defender": "Defender",
    "No-Nonsense Centre-Back": "Defender",
    "Wide Centre-Back": "Defender",
    "Libero": "Defender",
    "Stopper": "Defender",
    "Cover": "Defender",

    "Full Back": "Defender",
    "Wing Back": "Defender",
    "Complete Wing Back": "Defender",
    "Inverted Wing-Back": "Defender",
    "No-Nonsense Full Back": "Defender",

    # 🧱 Defensive Midfielders
    "Defensive Midfielder": "Midfielder",
    "Anchor Man": "Midfielder",
    "Half Back": "Midfielder",
    "Regista": "Midfielder",
    "Segundo Volante": "Midfielder",
    "Ball Winning Midfielder": "Midfielder",
    "Volante": "Midfielder",

    # ⚙️ Central Midfielders
    "Central Midfielder": "Midfielder",
    "Box-To-Box Midfielder": "Midfielder",
    "Mezzala": "Midfielder",
    "Carrilero": "Midfielder",
    "Deep-Lying Playmaker": "Midfielder",
    "Roaming Playmaker": "Midfielder",

    # 🎨 Attacking Midfielders
    "Attacking Midfielder": "Midfielder",
    "Advanced Playmaker": "Midfielder",
    "Shadow Striker": "Midfielder",
    "Enganche": "Midfielder",
    "Trequartista": "Midfielder",

    # 🏃 Wide Midfielders
    "Wide Midfielder": "Midfielder",
    "Wide Playmaker": "Midfielder",
    "Defensive Winger": "Midfielder",

    # 🎯 Forwards
    "Winger": "Attacker",
    "Inverted Winger": "Attacker",
    "Inside Forward": "Attacker",

    "Advanced Forward": "Attacker",
    "Poacher": "Attacker",
    "Complete Forward": "Attacker",
    "Target Forward": "Attacker",
    "False Nine": "Attacker",
    "Deep-Lying Forward": "Attacker",
    "Pressing Forward": "Attacker",
    "Second Striker": "Attacker"
}



ROLE_POSITION_MAP = {
    # 🧤 Goalkeeper
    "Goalkeeper": ["GK"],
    "Sweeper Keeper": ["GK"],

    # 🛡️ Defenders
    "Central Defender": ["D"],
    "Ball-Playing Defender": ["D"],
    "No-Nonsense Centre-Back": ["D"],
    "Wide Centre-Back": ["D"],
    "Libero": ["D"],
    "Stopper": ["D"],
    "Cover": ["D"],

    "Full Back": ["DL", "DR"],
    "Wing Back": ["WBL", "WBR"],
    "Complete Wing Back": ["WBL", "WBR"],
    "Inverted Wing-Back": ["DL", "DR"],
    "No-Nonsense Full Back": ["DL", "DR"],

    # 🧱 Defensive Midfielders
    "Defensive Midfielder": ["DM", "DMC"],
    "Anchor Man": ["DM", "DMC"],
    "Half Back": ["DM", "DMC"],
    "Regista": ["DMC"],
    "Segundo Volante": ["DMC", "MC"],
    "Volante": ["DMC", "MC"],
    "Ball Winning Midfielder": ["DM", "MC", "DMC"],

    # ⚙️ Central Midfielders
    "Central Midfielder": ["MC", "ML", "MR"],
    "Box-To-Box Midfielder": ["MC", "M","ML", "MR"],
    "Mezzala": ["ML", "MR", "MC"],
    "Carrilero": ["ML", "MR", "MC"],
    "Deep-Lying Playmaker": ["ML", "MR","MC", "DMC"],
    "Roaming Playmaker": ["ML", "MR","MC", "AMC"],
    "Advanced Playmaker": ["ML", "MR","MC","AMC",],

    # 🎨 Attacking Midfielders
    "Attacking Midfielder": ["AMC", "AML", "AMR"],
    
    "Shadow Striker": ["AMC"],
    "Enganche": ["AMC"],
    "Trequartista": ["AMC"],

    # 🏃 Wide Midfielders
    "Wide Midfielder": ["ML", "MR"],
    "Wide Playmaker": ["ML", "MR"],
    "Defensive Winger": ["ML", "MR"],

    # 🎯 Forwards
    "Winger": ["AML", "AMR", "ML", "MR"],
    "Inverted Winger": ["AML", "AMR"],
    "Inside Forward": ["AML", "AMR"],
    "Wide Target Forward": ["AML", "AMR"],

    "Advanced Forward": ["ST", "SC", "SL", "SR"],
    "Poacher": ["ST", "SC", "SL", "SR"],
    "Target Forward": ["ST", "SC", "SL", "SR"],
    "Deep-Lying Forward": ["ST", "SC", "AMC"],
    "Complete Forward": ["ST", "SC"],
    "Pressing Forward": ["ST", "SC"],
    "Second Striker": ["AMC", "ST"]
}

ROLE_ALIASES = {
    # 🧤 Goalkeepers
    "Goalkeeper": ["Sweeper Keeper"],
    "Sweeper Keeper": ["Goalkeeper"],

    # 🛡️ Central Defenders
    "Central Defender": ["No-Nonsense Centre-Back", "Ball-Playing Defender", "Wide Centre-Back", "Stopper", "Cover"],
    "Ball-Playing Defender": ["Central Defender", "Wide Centre-Back"],
    "No-Nonsense Centre-Back": ["Central Defender"],
    "Wide Centre-Back": ["Ball-Playing Defender"],
    "Libero": ["Ball-Playing Defender", "Central Defender"],

    # 🛞 Full-Backs & Wing-Backs
    "Full Back": ["Wing Back", "Complete Wing Back", "Inverted Wing-Back", "No-Nonsense Full Back"],
    "Wing Back": ["Full Back", "Complete Wing Back", "Inverted Wing-Back"],
    "Complete Wing Back": ["Wing Back"],
    "Inverted Wing-Back": ["Wing Back"],
    "No-Nonsense Full Back": ["Full Back"],

    # 🧱 Defensive Midfielders
    "Defensive Midfielder": ["Anchor Man", "Half Back", "Regista", "Segundo Volante", "Ball Winning Midfielder"],
    "Anchor Man": ["Defensive Midfielder"],
    "Half Back": ["Defensive Midfielder"],
    "Regista": ["Defensive Midfielder", "Deep-Lying Playmaker"],
    "Segundo Volante": ["Defensive Midfielder", "Box-To-Box Midfielder", "Volante"],
    "Ball Winning Midfielder": ["Defensive Midfielder", "Volante"],
    "Volante": ["Ball Winning Midfielder", "Segundo Volante"],

    # 🧠 Central Midfielders
    "Central Midfielder": ["Box-To-Box Midfielder", "Mezzala", "Carrilero", "Deep-Lying Playmaker"],
    "Box-To-Box Midfielder": ["Central Midfielder", "Segundo Volante"],
    "Mezzala": ["Central Midfielder", "Box-To-Box Midfielder"],
    "Carrilero": ["Central Midfielder"],
    "Deep-Lying Playmaker": ["Central Midfielder", "Regista"],
    "Roaming Playmaker": ["Central Midfielder", "Advanced Playmaker"],

    # 🏃 Wide Midfielders
    "Wide Midfielder": ["Winger", "Wide Playmaker", "Defensive Winger"],
    "Winger": ["Wide Midfielder", "Inverted Winger", "Inside Forward"],
    "Inverted Winger": ["Inside Forward", "Winger"],
    "Inside Forward": ["Inverted Winger", "Winger"],
    "Wide Playmaker": ["Advanced Playmaker", "Wide Midfielder"],
    "Defensive Winger": ["Wide Midfielder"],

    # 🎨 Attacking Midfielders
    "Attacking Midfielder": ["Advanced Playmaker", "Shadow Striker", "Enganche", "Trequartista"],
    "Advanced Playmaker": ["Attacking Midfielder", "Wide Playmaker", "Roaming Playmaker"],
    "Shadow Striker": ["Attacking Midfielder"],
    "Enganche": ["Advanced Playmaker", "Trequartista"],
    "Trequartista": ["Attacking Midfielder", "False Nine", "Advanced Playmaker"],

    # 🎯 Strikers & Forwards
    "Striker": ["Advanced Forward", "Poacher", "Complete Forward", "Target Forward", "False Nine"],
    "Advanced Forward": ["Poacher", "Complete Forward", "Deep-Lying Forward"],
    "Poacher": ["Advanced Forward", "Complete Forward", "Target Forward"],
    "Complete Forward": ["Advanced Forward", "Target Forward", "Poacher"],
    "Target Forward": ["Complete Forward", "Advanced Forward", "Pressing Forward"],
    "Deep-Lying Forward": ["Advanced Forward", "False Nine", "Trequartista"],
    "False Nine": ["Deep-Lying Forward", "Trequartista"],
    "Pressing Forward": ["Target Forward", "Advanced Forward"],
}

zone_map = {
    # 🧱 Defense
    "Goalkeeper": "defense",
    "Sweeper Keeper": "defense",
    "Central Defender": "defense",
    "Ball Playing Defender": "defense",
    "No-Nonsense Centre-Back": "defense",
    "Libero": "defense",
    "Wide Centre-Back": "defense",

    # 🛡️ Defensive Midfield
    "Anchor Man": "midfield-defensive",
    "Defensive Midfielder": "midfield-defensive",
    "Half Back": "midfield-defensive",
    "Volante": "midfield-defensive",
    "Deep Lying Playmaker": "midfield-defensive",
    "Segundo Volante": "midfield-defensive",

    # 🔄 Central Midfield
    "Box to Box Midfielder": "midfield-central",
    "Ball Winning Midfielder": "midfield-central",
    "Carrilero": "midfield-central",
    "Mezzala": "midfield-central",
    "Central Midfielder": "midfield-central",

    # 🎨 Attacking Midfield
    "Advanced Playmaker": "midfield-attacking",
    "Enganche": "midfield-attacking",
    "Shadow Striker": "midfield-attacking",
    "Trequartista": "midfield-attacking",
    "Roaming Playmaker": "midfield-attacking",

    # 🧭 Wide Roles (Defensive & Midfield)
    "Full Back": "wide-defensive",
    "Wing-Back": "wide-defensive",
    "Inverted Wing-Back": "wide-defensive",
    "Wide Midfielder": "wide-midfield",
    "Wide Playmaker": "wide-midfield",
    "Defensive Winger": "wide-midfield",

    # 🚀 Attacking Wings
    "Winger": "wide-attacking",
    "Inside Forward": "wide-attacking",
    "Inverted Winger": "wide-attacking",
    "Raumdeuter": "wide-attacking",

    # 🎯 Forward Roles
    "Advanced Forward": "attack",
    "Complete Forward": "attack",
    "Target Forward": "attack",
    "Poacher": "attack",
    "Pressing Forward": "attack",
    "Deep Lying Forward": "attack",
    "False Nine": "attack",
    "Trequartista (ST role)": "attack"
}

ROLE_POSITION_SHORT = {
    "Goalkeeper": ["GK"],
    "Sweeper Keeper": ["SK"],
    "Central Defender": ["CD"],
    "Ball-Playing Defender": ["BPD"],
    "No-Nonsense Centre-Back": ["NCB"],
    "Wide Centre-Back": ["WCB"],
    "Libero": ["LIB"],
    "Stopper": ["STP"],
    "Cover": ["COV"],
    "Full Back": ["FB"],
    "Wing Back": ["WB"],
    "Complete Wing Back": ["CWB"],
    "Inverted Wing-Back": ["IWB"],
    "No-Nonsense Full Back": ["NNFB"],
    "Central Midfielder": ["CM"],
    "Box-To-Box Midfielder": ["BBM"],
    "Ball Winning Midfielder": ["BWM"],
    "Mezzala": ["MEZ"],
    "Carrilero": ["CAR"],
    "Deep-Lying Playmaker": ["DLP"],
    "Roaming Playmaker": ["RPM"],
    "Defensive Midfielder": ["DM"],
    "Anchor Man": ["ANM"],
    "Half Back": ["HB"],
    "Regista": ["REG"],
    "Volante": ["VOL"],
    "Segundo Volante": ["SV"],
    "Advanced Playmaker": ["AP"],
    "Attacking Midfielder": ["AM"],
    "Shadow Striker": ["SS"],
    "Enganche": ["ENG"],
    "Trequartista": ["TRE"],
    "Wide Midfielder": ["WM"],
    "Winger": ["WNG"],
    "Inside Forward": ["IF"],
    "Inverted Winger": ["IW"],
    "Wide Playmaker": ["WP"],
    "Defensive Winger": ["DW"],
    "Wide Target Forward": ["WTF"],
    "Raumdeuter": ["RMD"],
    "Wide Target Man": ["WTM"],
    "False Nine": ["F9"],
    "Deep-Lying Forward": ["DLF"],
    "Target Forward": ["TF"],
    "Complete Forward": ["CF"],
    "Poacher": ["PCH"],
    "Advanced Forward": ["AF"],
    "Pressing Forward": ["PF"]
}    "Roaming Playmaker": "Midfielder",

    # 🎨 Attacking Midfielders
    "Attacking Midfielder": "Midfielder",
    "Advanced Playmaker": "Midfielder",
    "Shadow Striker": "Midfielder",
    "Enganche": "Midfielder",
    "Trequartista": "Midfielder",

    # 🏃 Wide Midfielders
    "Wide Midfielder": "Midfielder",
    "Wide Playmaker": "Midfielder",
    "Defensive Winger": "Midfielder",

    # 🎯 Forwards
    "Winger": "Attacker",
    "Inverted Winger": "Attacker",
    "Inside Forward": "Attacker",

    "Advanced Forward": "Attacker",
    "Poacher": "Attacker",
    "Complete Forward": "Attacker",
    "Target Forward": "Attacker",
    "False Nine": "Attacker",
    "Deep-Lying Forward": "Attacker",
    "Pressing Forward": "Attacker",
    "Second Striker": "Attacker"
}



ROLE_POSITION_MAP = {
    # 🧤 Goalkeeper
    "Goalkeeper": ["GK"],
    "Sweeper Keeper": ["GK"],

    # 🛡️ Defenders
    "Central Defender": ["D"],
    "Ball-Playing Defender": ["D"],
    "No-Nonsense Centre-Back": ["D"],
    "Wide Centre-Back": ["D"],
    "Libero": ["D"],
    "Stopper": ["D"],
    "Cover": ["D"],

    "Full Back": ["DL", "DR"],
    "Wing Back": ["WBL", "WBR"],
    "Complete Wing Back": ["WBL", "WBR"],
    "Inverted Wing-Back": ["DL", "DR"],
    "No-Nonsense Full Back": ["DL", "DR"],

    # 🧱 Defensive Midfielders
    "Defensive Midfielder": ["DM", "DMC"],
    "Anchor Man": ["DM", "DMC"],
    "Half Back": ["DM", "DMC"],
    "Regista": ["DMC"],
    "Segundo Volante": ["DMC", "M", "MC"],
    "Volante": ["DMC","M", "MC"],
    "Ball Winning Midfielder": ["DM", "MC", "M", "DMC"],

    # ⚙️ Central Midfielders
    "Central Midfielder": ["MC","M", "ML", "MR"],
    "Box-To-Box Midfielder": ["MC", "M","ML", "MR"],
    "Mezzala": ["ML", "MR", "MC", "M"],
    "Carrilero": ["ML", "MR", "M", "MC"],
    "Deep-Lying Playmaker": ["ML", "MR","M","MC", "DMC"],
    "Roaming Playmaker": ["ML", "MR","M", "MC", "AMC"],
    "Advanced Playmaker": ["ML", "MR","M", "MC","AMC",],

    # 🎨 Attacking Midfielders
    "Attacking Midfielder": ["AMC", "AM", "AML", "AMR"],
    
    "Shadow Striker": ["AMC, "AM"],
    "Enganche": ["AMC, "AM"],
    "Trequartista": ["AMC", "AM"],

    # 🏃 Wide Midfielders
    "Wide Midfielder": ["ML", "MR"],
    "Wide Playmaker": ["ML", "MR"],
    "Defensive Winger": ["ML", "MR"],

    # 🎯 Forwards
    "Winger": ["AML", "AMR", "ML", "MR"],
    "Inverted Winger": ["AML", "AMR"],
    "Inside Forward": ["AML", "AMR"],
    "Wide Target Forward": ["AML", "AMR"],

    "Advanced Forward": ["ST", "SC", "SL", "SR"],
    "Poacher": ["ST", "SC", "SL", "SR"],
    "Target Forward": ["ST", "SC", "SL", "SR"],
    "Deep-Lying Forward": ["ST", "SC", "AMC"],
    "Complete Forward": ["ST", "SC"],
    "Pressing Forward": ["ST", "SC"],
    "Second Striker": ["AMC", "ST"]
}

ROLE_ALIASES = {
    # 🧤 Goalkeepers
    "Goalkeeper": ["Sweeper Keeper"],
    "Sweeper Keeper": ["Goalkeeper"],

    # 🛡️ Central Defenders
    "Central Defender": ["No-Nonsense Centre-Back", "Ball-Playing Defender", "Wide Centre-Back", "Stopper", "Cover"],
    "Ball-Playing Defender": ["Central Defender", "Wide Centre-Back"],
    "No-Nonsense Centre-Back": ["Central Defender"],
    "Wide Centre-Back": ["Ball-Playing Defender"],
    "Libero": ["Ball-Playing Defender", "Central Defender"],

    # 🛞 Full-Backs & Wing-Backs
    "Full Back": ["Wing Back", "Complete Wing Back", "Inverted Wing-Back", "No-Nonsense Full Back"],
    "Wing Back": ["Full Back", "Complete Wing Back", "Inverted Wing-Back"],
    "Complete Wing Back": ["Wing Back"],
    "Inverted Wing-Back": ["Wing Back"],
    "No-Nonsense Full Back": ["Full Back"],

    # 🧱 Defensive Midfielders
    "Defensive Midfielder": ["Anchor Man", "Half Back", "Regista", "Segundo Volante", "Ball Winning Midfielder"],
    "Anchor Man": ["Defensive Midfielder"],
    "Half Back": ["Defensive Midfielder"],
    "Regista": ["Defensive Midfielder", "Deep-Lying Playmaker"],
    "Segundo Volante": ["Defensive Midfielder", "Box-To-Box Midfielder", "Volante"],
    "Ball Winning Midfielder": ["Defensive Midfielder", "Volante"],
    "Volante": ["Ball Winning Midfielder", "Segundo Volante"],

    # 🧠 Central Midfielders
    "Central Midfielder": ["Box-To-Box Midfielder", "Mezzala", "Carrilero", "Deep-Lying Playmaker"],
    "Box-To-Box Midfielder": ["Central Midfielder", "Segundo Volante"],
    "Mezzala": ["Central Midfielder", "Box-To-Box Midfielder"],
    "Carrilero": ["Central Midfielder"],
    "Deep-Lying Playmaker": ["Central Midfielder", "Regista"],
    "Roaming Playmaker": ["Central Midfielder", "Advanced Playmaker"],

    # 🏃 Wide Midfielders
    "Wide Midfielder": ["Winger", "Wide Playmaker", "Defensive Winger"],
    "Winger": ["Wide Midfielder", "Inverted Winger", "Inside Forward"],
    "Inverted Winger": ["Inside Forward", "Winger"],
    "Inside Forward": ["Inverted Winger", "Winger"],
    "Wide Playmaker": ["Advanced Playmaker", "Wide Midfielder"],
    "Defensive Winger": ["Wide Midfielder"],

    # 🎨 Attacking Midfielders
    "Attacking Midfielder": ["Advanced Playmaker", "Shadow Striker", "Enganche", "Trequartista"],
    "Advanced Playmaker": ["Attacking Midfielder", "Wide Playmaker", "Roaming Playmaker"],
    "Shadow Striker": ["Attacking Midfielder"],
    "Enganche": ["Advanced Playmaker", "Trequartista"],
    "Trequartista": ["Attacking Midfielder", "False Nine", "Advanced Playmaker"],

    # 🎯 Strikers & Forwards
    "Striker": ["Advanced Forward", "Poacher", "Complete Forward", "Target Forward", "False Nine"],
    "Advanced Forward": ["Poacher", "Complete Forward", "Deep-Lying Forward"],
    "Poacher": ["Advanced Forward", "Complete Forward", "Target Forward"],
    "Complete Forward": ["Advanced Forward", "Target Forward", "Poacher"],
    "Target Forward": ["Complete Forward", "Advanced Forward", "Pressing Forward"],
    "Deep-Lying Forward": ["Advanced Forward", "False Nine", "Trequartista"],
    "False Nine": ["Deep-Lying Forward", "Trequartista"],
    "Pressing Forward": ["Target Forward", "Advanced Forward"],
}

zone_map = {
    # 🧱 Defense
    "Goalkeeper": "defense",
    "Sweeper Keeper": "defense",
    "Central Defender": "defense",
    "Ball Playing Defender": "defense",
    "No-Nonsense Centre-Back": "defense",
    "Libero": "defense",
    "Wide Centre-Back": "defense",

    # 🛡️ Defensive Midfield
    "Anchor Man": "midfield-defensive",
    "Defensive Midfielder": "midfield-defensive",
    "Half Back": "midfield-defensive",
    "Volante": "midfield-defensive",
    "Deep Lying Playmaker": "midfield-defensive",
    "Segundo Volante": "midfield-defensive",

    # 🔄 Central Midfield
    "Box to Box Midfielder": "midfield-central",
    "Ball Winning Midfielder": "midfield-central",
    "Carrilero": "midfield-central",
    "Mezzala": "midfield-central",
    "Central Midfielder": "midfield-central",

    # 🎨 Attacking Midfield
    "Advanced Playmaker": "midfield-attacking",
    "Enganche": "midfield-attacking",
    "Shadow Striker": "midfield-attacking",
    "Trequartista": "midfield-attacking",
    "Roaming Playmaker": "midfield-attacking",

    # 🧭 Wide Roles (Defensive & Midfield)
    "Full Back": "wide-defensive",
    "Wing-Back": "wide-defensive",
    "Inverted Wing-Back": "wide-defensive",
    "Wide Midfielder": "wide-midfield",
    "Wide Playmaker": "wide-midfield",
    "Defensive Winger": "wide-midfield",

    # 🚀 Attacking Wings
    "Winger": "wide-attacking",
    "Inside Forward": "wide-attacking",
    "Inverted Winger": "wide-attacking",
    "Raumdeuter": "wide-attacking",

    # 🎯 Forward Roles
    "Advanced Forward": "attack",
    "Complete Forward": "attack",
    "Target Forward": "attack",
    "Poacher": "attack",
    "Pressing Forward": "attack",
    "Deep Lying Forward": "attack",
    "False Nine": "attack",
    "Trequartista (ST role)": "attack"
}

ROLE_POSITION_SHORT = {
    "Goalkeeper": ["GK"],
    "Sweeper Keeper": ["SK"],
    "Central Defender": ["CD"],
    "Ball-Playing Defender": ["BPD"],
    "No-Nonsense Centre-Back": ["NCB"],
    "Wide Centre-Back": ["WCB"],
    "Libero": ["LIB"],
    "Stopper": ["STP"],
    "Cover": ["COV"],
    "Full Back": ["FB"],
    "Wing Back": ["WB"],
    "Complete Wing Back": ["CWB"],
    "Inverted Wing-Back": ["IWB"],
    "No-Nonsense Full Back": ["NNFB"],
    "Central Midfielder": ["CM"],
    "Box-To-Box Midfielder": ["BBM"],
    "Ball Winning Midfielder": ["BWM"],
    "Mezzala": ["MEZ"],
    "Carrilero": ["CAR"],
    "Deep-Lying Playmaker": ["DLP"],
    "Roaming Playmaker": ["RPM"],
    "Defensive Midfielder": ["DM"],
    "Anchor Man": ["ANM"],
    "Half Back": ["HB"],
    "Regista": ["REG"],
    "Volante": ["VOL"],
    "Segundo Volante": ["SV"],
    "Advanced Playmaker": ["AP"],
    "Attacking Midfielder": ["AM"],
    "Shadow Striker": ["SS"],
    "Enganche": ["ENG"],
    "Trequartista": ["TRE"],
    "Wide Midfielder": ["WM"],
    "Winger": ["WNG"],
    "Inside Forward": ["IF"],
    "Inverted Winger": ["IW"],
    "Wide Playmaker": ["WP"],
    "Defensive Winger": ["DW"],
    "Wide Target Forward": ["WTF"],
    "Raumdeuter": ["RMD"],
    "Wide Target Man": ["WTM"],
    "False Nine": ["F9"],
    "Deep-Lying Forward": ["DLF"],
    "Target Forward": ["TF"],
    "Complete Forward": ["CF"],
    "Poacher": ["PCH"],
    "Advanced Forward": ["AF"],
    "Pressing Forward": ["PF"]
}
