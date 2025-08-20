#formations.py
# 8 columns (A–H), 4 rows (1–4)
ZONE_GRID = [
    ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"],  # Defensive third
    ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"],  # Midfield third
    ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3"],  # Attacking third
    ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4"]   # Final third / box
]

ZONE_MAP = {
    # 🧤 Goalkeepers
    "Goalkeeper": {"C": ["D1", "E1"]},
    "Sweeper Keeper": {"C": ["C1", "D1", "E1", "F1"]},

    # 🛡️ Central Defenders
    "Central Defender": {"C": ["D1", "E1", "D2", "E2"]},
    "Ball-Playing Defender": {"C": ["C1", "D1", "E1", "F1"]},
    "No-Nonsense Centre-Back": {"C": ["D1", "E1"]},
    "Wide Centre-Back": {"L": ["B1", "C1"], "R": ["F1", "G1"]},
    "Libero": {"C": ["D1", "E1", "D2", "E2", "D3", "E3"]},
    "Stopper": {"C": ["D1", "E1", "D2"]},
    "Cover": {"C": ["D1", "E1", "E2"]},

    # 🛡️ Full/Wing Backs
    "Full Back": {
        "L": ["A1", "B1", "A2"],
        "R": ["G1", "H1", "H2"]
    },
    "Wing Back": {
        "L": ["A1", "B1", "A2", "B2"],
        "R": ["G1", "H1", "G2", "H2"]
    },
    "Complete Wing Back": {
        "L": ["A1", "B1", "A2", "B2", "A3"],
        "R": ["G1", "H1", "G2", "H2", "H3"]
    },
    "Inverted Wing-Back": {
        "L": ["B1", "C1", "B2"],
        "R": ["F1", "G1", "G2"]
    },
    "No-Nonsense Full Back": {
        "L": ["A1", "B1"],
        "R": ["G1", "H1"]
    },

    # 🧱 Defensive Midfielders
    "Defensive Midfielder": {
        "C": ["C2", "D2", "E2", "F2"],
        "L": ["B2", "C2", "B3"],
        "R": ["E2", "F2", "F3"]
    },
    "Anchor Man": {
        "C": ["D2", "E2"],
        "L": ["C2", "D2"],
        "R": ["E2", "F2"]
    },
    "Half Back": {
        "C": ["C1", "D1", "E1", "D2"],
        "L": ["B1", "C1", "C2"],
        "R": ["E1", "F1", "F2"]
    },
    "Regista": {
        "C": ["D2", "E2", "D3"],
        "L": ["C2", "D2", "C3"],
        "R": ["E2", "F2", "F3"]
    },
    "Segundo Volante": {
        "C": ["C2", "D2", "E2", "F2", "C3", "D3", "E3", "F3"],
        "L": ["B2", "C2", "B3", "C3"],
        "R": ["E2", "F2", "F3", "G3"]
    },
    "Volante": {
        "C": ["C2", "D2", "E2", "F2", "C3", "D3", "E3", "F3"],
        "L": ["B2", "C2", "B3", "C3"],
        "R": ["E2", "F2", "F3", "G3"]
    },
    "Ball Winning Midfielder": {
        "C": ["C2", "D2", "E2", "F2", "C3", "D3", "E3", "F3"],
        "L": ["B2", "C2", "B3", "C3"],
        "R": ["E2", "F2", "F3", "G3"]
    },

    # ⚙️ Central Midfielders
    "Central Midfielder": {
        "C": ["C2", "D2", "E2", "F2", "C3", "D3", "E3", "F3"],
        "L": ["B2", "C2", "B3", "C3"],
        "R": ["E2", "F2", "F3", "G3"]
    },
    "Box-To-Box Midfielder": {
        "C": ["C2", "D2", "E2", "F2", "C3", "D3", "E3", "F3"],
        "L": ["B2", "C2", "B3", "C3"],
        "R": ["E2", "F2", "F3", "G3"]
    },
    "Mezzala": {
        "L": ["B2", "C2", "B3"],
        "R": ["F2", "G2", "F3"]
    },
    "Carrilero": {
        "L": ["B2", "C2"],
        "R": ["F2", "G2"]
    },
    "Deep-Lying Playmaker": {
        "C": ["D2", "E2"],
        "L": ["C2", "D2"],
        "R": ["E2", "F2"]
    },
    "Roaming Playmaker": {
        "C": ["D2", "E2", "D3", "E3", "D4"],
        "L": ["C2", "D2", "C3", "D3"],
        "R": ["E2", "F2", "E3", "F3"]
    },

    # 🎨 Attacking Midfielders
    "Attacking Midfielder": {
        "C": ["D3", "E3", "D4", "E4"],
        "L": ["B3", "C3", "B4"],
        "R": ["F3", "G3", "F4"]
    },
    "Advanced Playmaker": {
        "C": ["D3", "E3", "D4"],
        "L": ["B3", "C3"],
        "R": ["F3", "G3"]
    },
    "Shadow Striker": {
        "C": ["D3", "E3", "D4", "E4"]
    },
    "Enganche": {
        "C": ["D3", "E3"]
    },
    "Trequartista": {
        "C": ["D3", "E3", "D4", "E4"]
    },

    # 🏃 Wide Midfielders
    "Wide Midfielder": {
        "L": ["A2", "B2", "A3"],
        "R": ["G2", "H2", "H3"]
    },
    "Wide Playmaker": {
        "L": ["B2", "C2", "B3"],
        "R": ["F2", "G2", "F3"]
    },
    "Defensive Winger": {
        "L": ["A2", "B2"],
        "R": ["G2", "H2"]
    },

    # 🎯 Forwards
    "Winger": {
        "L": ["A3", "B3", "A4", "B4"],
        "R": ["G3", "H3", "G4", "H4"]
    },
    "Inverted Winger": {
        "L": ["B3", "C3", "B4"],
        "R": ["F3", "G3", "F4"]
    },
    "Inside Forward": {
        "L": ["C3", "D3", "C4"],
        "R": ["E3", "F3", "E4"]
    },
    "Wide Target Forward": {
        "L": ["B3", "C3", "B4"],
        "R": ["F3", "G3", "F4"]
    },

    "Advanced Forward": {"C": ["D4", "E4", "C4", "F4"]},
    "Poacher": {"C": ["D4", "E4"]},
    "Target Forward": {"C": ["C4", "D4", "E4", "F4"]},
    "Deep-Lying Forward": {"C": ["D3", "E3", "D4"]},
    "Complete Forward": {"C": ["C4", "D4", "E4", "F4"]},
    "Pressing Forward": {"C": ["D4", "E4", "C4", "F4"]},
    "Second Striker": {"C": ["D3", "E3", "D4", "E4"]}
}


# Define formations with roles, sides, duties, and positions on the pitch
formations = [
    {
        "name": "5-4-1",
        "roles": [
            {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
            {"role": "Central Defender", "side": "C", "duty": "Defend", "position": (25, 50)},
            {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 35)},
            {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 65)},
            {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 25)},
            {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 75)},
            {"role": "Ball Winning Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
            {"role": "Box-To-Box Midfielder", "side": "R", "duty": "Support", "position": (45, 65)},
            {"role": "Winger", "side": "L", "duty": "Attack", "position": (60, 20)},
            {"role": "Winger", "side": "R", "duty": "Attack", "position": (60, 80)},
            {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (78, 50)}
        ],
        "attribute_multipliers": {
            "Full Back": {
                "Positioning": 1.2,
                "Stamina": 1.1,
                "Marking": 1.1
            },
            "Ball Winning Midfielder": {
                "Tackling": 1.3,
                "Work Rate": 1.2
            },
            "Winger": {
                "Crossing": 1.2,
                "Acceleration": 1.1
            },
            "Advanced Forward": {
                "Finishing": 1.3,
                "Off the Ball": 1.2
            }
        }
    },
    {
    "name": "4-4-2",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 42)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 58)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 28)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 72)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Ball Winning Midfielder", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Winger", "side": "L", "duty": "Attack", "position": (60, 20)},
        {"role": "Winger", "side": "R", "duty": "Attack", "position": (60, 80)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 42)},
        {"role": "Target Forward", "side": "R", "duty": "Attack", "position": (78, 58)}
    ],
    "attribute_multipliers": {
        "Full Back": {
            "Crossing": 1.2,
            "Stamina": 1.1
        },
        "Box-To-Box Midfielder": {
            "Work Rate": 1.2,
            "Passing": 1.1
        },
        "Winger": {
            "Dribbling": 1.2,
            "Acceleration": 1.1
        },
        "Poacher": {
            "Finishing": 1.3,
            "Anticipation": 1.2
        },
        "Target Forward": {
            "Strength": 1.3,
            "Heading": 1.2
        }
    }
},
    {
    "name": "4-2-3-1 Wide",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 40)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 60)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 25)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 75)},
        {"role": "Defensive Midfielder", "side": "L", "duty": "Support", "position": (40, 40)},
        {"role": "Defensive Midfielder", "side": "R", "duty": "Support", "position": (40, 60)},
        {"role": "Winger", "side": "L", "duty": "Attack", "position": (55, 20)},
        {"role": "Attacking Midfielder", "side": "C", "duty": "Attack", "position": (60, 50)},
        {"role": "Winger", "side": "R", "duty": "Attack", "position": (55, 80)},
        {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (80, 50)}
    ],
    "attribute_multipliers": {
        "Full Back": {
            "Crossing": 1.3,
            "Off the Ball": 1.2
        },
        "Defensive Midfielder": {
            "Positioning": 1.2,
            "Tackling": 1.1
        },
        "Attacking Midfielder": {
            "Vision": 1.3,
            "Passing": 1.2
        },
        "Winger": {
            "Dribbling": 1.3,
            "Acceleration": 1.2
        },
        "Advanced Forward": {
            "Finishing": 1.3,
            "Composure": 1.2
        }
    }
},
    {
    "name": "4-3-3",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 40)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 60)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 25)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 75)},
        {"role": "Ball Winning Midfielder", "side": "C", "duty": "Support", "position": (42, 50)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Advanced Playmaker", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Inside Forward", "side": "L", "duty": "Attack", "position": (65, 30)},
        {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (78, 50)},
        {"role": "Inside Forward", "side": "R", "duty": "Attack", "position": (65, 70)}
    ],
    "attribute_multipliers": {
        "Full Back": {
            "Crossing": 1.3,
            "Stamina": 1.2
        },
        "Ball Winning Midfielder": {
            "Aggression": 1.2,
            "Tackling": 1.3
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Passing": 1.2
        },
        "Inside Forward": {
            "Dribbling": 1.3,
            "Finishing": 1.2
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Composure": 1.2
        }
    }
},
{
    "name": "4-2-4",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 40)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 60)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 25)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 75)},
        {"role": "Ball Winning Midfielder", "side": "L", "duty": "Support", "position": (40, 35)},
        {"role": "Box-To-Box Midfielder", "side": "R", "duty": "Support", "position": (40, 65)},
        {"role": "Winger", "side": "L", "duty": "Attack", "position": (60, 20)},
        {"role": "Winger", "side": "R", "duty": "Attack", "position": (60, 80)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 42)},
        {"role": "Advanced Forward", "side": "R", "duty": "Attack", "position": (78, 58)}
    ],
    "attribute_multipliers": {
        "Full Back": {
            "Crossing": 1.2,
            "Acceleration": 1.1
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.2,
            "Work Rate": 1.2
        },
        "Winger": {
            "Dribbling": 1.3,
            "Crossing": 1.2
        },
        "Poacher": {
            "Finishing": 1.4,
            "Anticipation": 1.3
        },
        "Advanced Forward": {
            "Pace": 1.3,
            "Off the Ball": 1.2
        }
    }
},
{
    "name": "3-4-3",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 35)},
        {"role": "Central Defender", "side": "C", "duty": "Defend", "position": (25, 50)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 65)},
        {"role": "Wing Back", "side": "L", "duty": "Support", "position": (30, 25)},
        {"role": "Wing Back", "side": "R", "duty": "Support", "position": (30, 75)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Advanced Playmaker", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Inside Forward", "side": "L", "duty": "Attack", "position": (65, 30)},
        {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (78, 50)},
        {"role": "Inside Forward", "side": "R", "duty": "Attack", "position": (65, 70)}
    ],
    "attribute_multipliers": {
        "Wing Back": {
            "Stamina": 1.3,
            "Crossing": 1.2
        },
        "Box-To-Box Midfielder": {
            "Work Rate": 1.3,
            "Passing": 1.1
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Technique": 1.2
        },
        "Inside Forward": {
            "Dribbling": 1.3,
            "Finishing": 1.2
        },
        "Advanced Forward": {
            "Composure": 1.3,
            "Off the Ball": 1.2
        }
    }
},
{
    "name": "3-5-2",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 35)},
        {"role": "Central Defender", "side": "C", "duty": "Defend", "position": (25, 50)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 65)},
        {"role": "Wing Back", "side": "L", "duty": "Support", "position": (30, 25)},
        {"role": "Wing Back", "side": "R", "duty": "Support", "position": (30, 75)},
        {"role": "Ball Winning Midfielder", "side": "L", "duty": "Support", "position": (42, 30)},
        {"role": "Box-To-Box Midfielder", "side": "R", "duty": "Support", "position": (42, 70)},
        {"role": "Advanced Playmaker", "side": "C", "duty": "Support", "position": (50, 50)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 42)},
        {"role": "Advanced Forward", "side": "R", "duty": "Attack", "position": (78, 58)}
    ],
    "attribute_multipliers": {
        "Wing Back": {
            "Stamina": 1.3,
            "Crossing": 1.2,
            "Work Rate": 1.2
        },
        "Ball Winning Midfielder": {
            "Aggression": 1.3,
            "Tackling": 1.2
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.3,
            "Passing": 1.1
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Technique": 1.2
        },
        "Poacher": {
            "Finishing": 1.4,
            "Anticipation": 1.3
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Composure": 1.2
        }
    }
},
{
    "name": "4-1-2-1-2 Narrow",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 42)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 58)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 28)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 72)},
        {"role": "Defensive Midfielder", "side": "C", "duty": "Support", "position": (40, 50)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (50, 38)},
        {"role": "Advanced Playmaker", "side": "R", "duty": "Support", "position": (50, 62)},
        {"role": "Attacking Midfielder", "side": "C", "duty": "Attack", "position": (60, 50)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 45)},
        {"role": "Advanced Forward", "side": "R", "duty": "Attack", "position": (78, 55)}
    ],
    "attribute_multipliers": {
        "Defensive Midfielder": {
            "Positioning": 1.3,
            "Tackling": 1.2
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.3,
            "Work Rate": 1.2
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Passing": 1.2
        },
        "Attacking Midfielder": {
            "Technique": 1.2,
            "Composure": 1.2
        },
        "Poacher": {
            "Finishing": 1.4,
            "Anticipation": 1.3
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Pace": 1.2
        }
    }
},
{
    "name": "4-3-1-2",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 42)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 58)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 28)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 72)},
        {"role": "Ball Winning Midfielder", "side": "L", "duty": "Support", "position": (42, 35)},
        {"role": "Box-To-Box Midfielder", "side": "R", "duty": "Support", "position": (42, 65)},
        {"role": "Advanced Playmaker", "side": "C", "duty": "Support", "position": (50, 50)},
        {"role": "Attacking Midfielder", "side": "C", "duty": "Attack", "position": (60, 50)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 45)},
        {"role": "Advanced Forward", "side": "R", "duty": "Attack", "position": (78, 55)}
    ],
    "attribute_multipliers": {
        "Ball Winning Midfielder": {
            "Aggression": 1.3,
            "Tackling": 1.2
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.3,
            "Passing": 1.1
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Technique": 1.2
        },
        "Attacking Midfielder": {
            "Composure": 1.2,
            "Finishing": 1.1
        },
        "Poacher": {
            "Finishing": 1.4,
            "Anticipation": 1.3
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Acceleration": 1.2
        }
    }
},
{
    "name": "4-5-1",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 42)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 58)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 28)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 72)},
        {"role": "Ball Winning Midfielder", "side": "C", "duty": "Support", "position": (42, 50)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Advanced Playmaker", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Winger", "side": "L", "duty": "Attack", "position": (60, 20)},
        {"role": "Winger", "side": "R", "duty": "Attack", "position": (60, 80)},
        {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (78, 50)}
    ],
    "attribute_multipliers": {
        "Ball Winning Midfielder": {
            "Tackling": 1.3,
            "Work Rate": 1.2
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.3,
            "Passing": 1.1
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Technique": 1.2
        },
        "Winger": {
            "Crossing": 1.3,
            "Acceleration": 1.2
        },
        "Advanced Forward": {
            "Finishing": 1.3,
            "Off the Ball": 1.2
        }
    }
},
{
    "name": "3-4-2-1",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 35)},
        {"role": "Central Defender", "side": "C", "duty": "Defend", "position": (25, 50)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 65)},
        {"role": "Wing Back", "side": "L", "duty": "Support", "position": (30, 25)},
        {"role": "Wing Back", "side": "R", "duty": "Support", "position": (30, 75)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Ball Winning Midfielder", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Attacking Midfielder", "side": "L", "duty": "Attack", "position": (60, 38)},
        {"role": "Attacking Midfielder", "side": "R", "duty": "Attack", "position": (60, 62)},
        {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (78, 50)}
    ],
    "attribute_multipliers": {
        "Wing Back": {
            "Stamina": 1.3,
            "Crossing": 1.2
        },
        "Box-To-Box Midfielder": {
            "Work Rate": 1.3,
            "Passing": 1.1
        },
        "Ball Winning Midfielder": {
            "Aggression": 1.3,
            "Tackling": 1.2
        },
        "Attacking Midfielder": {
            "Vision": 1.3,
            "Technique": 1.2
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Finishing": 1.2
        }
    }
},

{
    "name": "4-4-1-1",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 42)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 58)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 28)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 72)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Ball Winning Midfielder", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Winger", "side": "L", "duty": "Attack", "position": (60, 20)},
        {"role": "Winger", "side": "R", "duty": "Attack", "position": (60, 80)},
        {"role": "Attacking Midfielder", "side": "C", "duty": "Support", "position": (63, 50)},
        {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (78, 50)}
    ],
    "attribute_multipliers": {
        "Full Back": {
            "Crossing": 1.2,
            "Stamina": 1.1
        },
        "Box-To-Box Midfielder": {
            "Work Rate": 1.3,
            "Passing": 1.1
        },
        "Ball Winning Midfielder": {
            "Aggression": 1.3,
            "Tackling": 1.2
        },
        "Winger": {
            "Dribbling": 1.3,
            "Acceleration": 1.2
        },
        "Attacking Midfielder": {
            "Vision": 1.3,
            "Composure": 1.2
        },
        "Advanced Forward": {
            "Finishing": 1.3,
            "Off the Ball": 1.2
        }
    }
},

{
    "name": "3-4-1-2",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 35)},
        {"role": "Central Defender", "side": "C", "duty": "Defend", "position": (25, 50)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 65)},
        {"role": "Wing Back", "side": "L", "duty": "Support", "position": (30, 25)},
        {"role": "Wing Back", "side": "R", "duty": "Support", "position": (30, 75)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Ball Winning Midfielder", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Attacking Midfielder", "side": "C", "duty": "Attack", "position": (60, 50)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 45)},
        {"role": "Advanced Forward", "side": "R", "duty": "Attack", "position": (78, 55)}
    ],
    "attribute_multipliers": {
        "Wing Back": {
            "Stamina": 1.3,
            "Crossing": 1.2
        },
        "Box-To-Box Midfielder": {
            "Work Rate": 1.3,
            "Passing": 1.1
        },
        "Ball Winning Midfielder": {
            "Aggression": 1.3,
            "Tackling": 1.2
        },
        "Attacking Midfielder": {
            "Vision": 1.3,
            "Technique": 1.2
        },
        "Poacher": {
            "Finishing": 1.4,
            "Anticipation": 1.3
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Composure": 1.2
        }
    }
},

{
    "name": "4-2-2-2 Narrow",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 42)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 58)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 28)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 72)},
        {"role": "Ball Winning Midfielder", "side": "L", "duty": "Support", "position": (42, 35)},
        {"role": "Box-To-Box Midfielder", "side": "R", "duty": "Support", "position": (42, 65)},
        {"role": "Advanced Playmaker", "side": "L", "duty": "Attack", "position": (60, 40)},
        {"role": "Advanced Playmaker", "side": "R", "duty": "Attack", "position": (60, 60)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 45)},
        {"role": "Advanced Forward", "side": "R", "duty": "Attack", "position": (78, 55)}
    ],
    "attribute_multipliers": {
        "Ball Winning Midfielder": {
            "Aggression": 1.3,
            "Tackling": 1.2
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.3,
            "Work Rate": 1.2
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Passing": 1.2
        },
        "Poacher": {
            "Finishing": 1.4,
            "Anticipation": 1.3
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Composure": 1.2
        }
    }
},

{
    "name": "3-1-4-2",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 35)},
        {"role": "Central Defender", "side": "C", "duty": "Defend", "position": (25, 50)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 65)},
        {"role": "Defensive Midfielder", "side": "C", "duty": "Defend", "position": (40, 50)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (50, 35)},
        {"role": "Box-To-Box Midfielder", "side": "R", "duty": "Support", "position": (50, 65)},
        {"role": "Wide Midfielder", "side": "L", "duty": "Support", "position": (50, 20)},
        {"role": "Wide Midfielder", "side": "R", "duty": "Support", "position": (50, 80)},
        {"role": "Poacher", "side": "L", "duty": "Attack", "position": (78, 45)},
        {"role": "Advanced Forward", "side": "R", "duty": "Attack", "position": (78, 55)}
    ],
    "attribute_multipliers": {
        "Defensive Midfielder": {
            "Positioning": 1.3,
            "Tackling": 1.2
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.3,
            "Work Rate": 1.2
        },
        "Wide Midfielder": {
            "Crossing": 1.3,
            "Acceleration": 1.2
        },
        "Poacher": {
            "Finishing": 1.4,
            "Anticipation": 1.3
        },
        "Advanced Forward": {
            "Off the Ball": 1.3,
            "Composure": 1.2
        }
    }
},

{
    "name": "4-3-2-1 Christmas Tree",
    "roles": [
        {"role": "Goalkeeper", "side": "C", "duty": "Defend", "position": (12, 50)},
        {"role": "Central Defender", "side": "L", "duty": "Defend", "position": (25, 42)},
        {"role": "Central Defender", "side": "R", "duty": "Defend", "position": (25, 58)},
        {"role": "Full Back", "side": "L", "duty": "Support", "position": (18, 28)},
        {"role": "Full Back", "side": "R", "duty": "Support", "position": (18, 72)},
        {"role": "Ball Winning Midfielder", "side": "C", "duty": "Support", "position": (40, 50)},
        {"role": "Box-To-Box Midfielder", "side": "L", "duty": "Support", "position": (45, 35)},
        {"role": "Box-To-Box Midfielder", "side": "R", "duty": "Support", "position": (45, 65)},
        {"role": "Advanced Playmaker", "side": "L", "duty": "Support", "position": (55, 42)},
        {"role": "Advanced Playmaker", "side": "R", "duty": "Support", "position": (55, 58)},
        {"role": "Advanced Forward", "side": "C", "duty": "Attack", "position": (78, 50)}
    ],
    "attribute_multipliers": {
        "Ball Winning Midfielder": {
            "Aggression": 1.3,
            "Tackling": 1.2
        },
        "Box-To-Box Midfielder": {
            "Stamina": 1.3,
            "Work Rate": 1.2
        },
        "Advanced Playmaker": {
            "Vision": 1.3,
            "Passing": 1.2
        },
        "Advanced Forward": {
            "Finishing": 1.3,
            "Composure": 1.2
        }
    }
}
]