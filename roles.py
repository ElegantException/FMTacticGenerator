#roles.py
SYNERGY_MATRIX = {
    ("BBM", "BWM"): 0.90,
    ("BBM", "CM"): 0.85,
    ("BBM", "DLP"): 0.83,
    ("BBM", "AP"): 0.80,
    ("BBM", "BBM"): 0.65,
    ("BWM", "CM"): 0.82,
    ("BWM", "DLP"): 0.84,
    ("BWM", "AP"): 0.75,
    ("BWM", "BWM"): 0.60,
    ("CM", "CM"): 0.80,
    ("CM", "DLP"): 0.83,
    ("CM", "AP"): 0.78,
    ("DLP", "AP"): 0.82,
    ("AP", "AP"): 0.70,
    ("AM", "AP"): 0.75,
    ("DM", "BBM"): 0.88,
    ("DM", "BWM"): 0.85,
    ("DM", "CM"): 0.86,
    ("DM", "DLP"): 0.80,
    ("DM", "AP"): 0.78,
    ("DM", "AM"): 0.76,
    ("DM", "DM"): 0.60
}

ROLE_FLEX_MAP = {
    # 🛡️ Defensive Midfielders
    ("Defensive Midfielder", "C"): (40, 50),
    ("Defensive Midfielder", "L"): (40, 40),
    ("Defensive Midfielder", "R"): (40, 60),
    ("Anchor Man", "C"): (40, 50),
    ("Anchor Man", "L"): (40, 40),
    ("Anchor Man", "R"): (40, 60),
    ("Half Back", "C"): (38, 50),
    ("Half Back", "L"): (38, 40),
    ("Half Back", "R"): (38, 60),
    ("Regista", "C"): (43, 50),
    ("Regista", "L"): (43, 40),
    ("Regista", "R"): (43, 60),

    # ⚙️ Central Midfielders
    ("Central Midfielder", "C"): (45, 50),
    ("Central Midfielder", "L"): (45, 35),
    ("Central Midfielder", "R"): (45, 65),
    ("Box-To-Box Midfielder", "C"): (44, 50),
    ("Box-To-Box Midfielder", "L"): (45, 35),
    ("Box-To-Box Midfielder", "R"): (45, 65),
    ("Deep-Lying Playmaker", "C"): (43, 50),
    ("Deep-Lying Playmaker", "L"): (43, 35),
    ("Deep-Lying Playmaker", "R"): (43, 65),
    ("Roaming Playmaker", "C"): (46, 50),
    ("Roaming Playmaker", "L"): (46, 35),
    ("Roaming Playmaker", "R"): (46, 65),
    ("Mezzala", "L"): (48, 30),
    ("Mezzala", "R"): (48, 70),
    ("Carrilero", "L"): (44, 40),
    ("Carrilero", "R"): (44, 60),
    ("Segundo Volante", "C"): (42, 50),
    ("Segundo Volante", "L"): (42, 35),
    ("Segundo Volante", "R"): (42, 65),

    # 🎯 Attacking Midfielders
    ("Attacking Midfielder", "C"): (60, 50),
    ("Attacking Midfielder", "L"): (60, 35),
    ("Attacking Midfielder", "R"): (60, 65),
    ("Advanced Playmaker", "C"): (58, 50),
    ("Advanced Playmaker", "L"): (58, 35),
    ("Advanced Playmaker", "R"): (58, 65),
    ("Shadow Striker", "C"): (62, 50),
    ("Shadow Striker", "L"): (62, 35),
    ("Shadow Striker", "R"): (62, 65),
    ("Trequartista", "C"): (63, 50),
    ("Trequartista", "L"): (63, 35),
    ("Trequartista", "R"): (63, 65),
    ("Enganche", "C"): (59, 50),
    ("Enganche", "L"): (59, 35),
    ("Enganche", "R"): (59, 65)
}

# Full FM24 Role + Duty Attribute Weights for Tactic Analyzer
ROLE_ATTRIBUTES = {
"Goalkeeper": {
  "Defend": {
    "Handling": 0.25, "Reflexes": 0.20, "Positioning": 0.20,
    "Concentration": 0.10, "Composure": 0.10, "Jumping Reach": 0.10,
    "Strength": 0.05
  }
},
"Sweeper Keeper": {
  "Defend": {
    "Anticipation": 0.20, "Communication": 0.15, "Positioning": 0.15,
    "Passing": 0.15, "Composure": 0.15, "Reflexes": 0.10, "Acceleration": 0.10
  },
  "Support": {
    "Anticipation": 0.20, "Communication": 0.15, "Passing": 0.15,
    "Composure": 0.15, "Vision": 0.10, "Acceleration": 0.10, "First Touch": 0.15
  },
  "Attack": {
    "Passing": 0.20, "Composure": 0.15, "Vision": 0.15,
    "First Touch": 0.15, "Anticipation": 0.10, "Acceleration": 0.15, "Kicking": 0.10
  }
},
"Central Defender": {
  "Defend": {
    "Marking": 0.20, "Tackling": 0.20, "Positioning": 0.20,
    "Heading": 0.15, "Strength": 0.10, "Jumping Reach": 0.10,
    "Concentration": 0.05
  },
  "Stopper": {
    "Aggression": 0.20, "Bravery": 0.20, "Tackling": 0.20,
    "Heading": 0.15, "Strength": 0.10, "Positioning": 0.10,
    "Jumping Reach": 0.05
  },
  "Cover": {
    "Anticipation": 0.20, "Positioning": 0.20, "Pace": 0.15,
    "Tackling": 0.15, "Composure": 0.10, "Concentration": 0.10,
    "Decisions": 0.10
  }
},
"Ball-Playing Defender": {
  "Defend": {
    "Passing": 0.20, "Composure": 0.20, "Positioning": 0.15,
    "Marking": 0.15, "Tackling": 0.10, "Vision": 0.10,
    "Technique": 0.10
  },
  "Stopper": {
    "Aggression": 0.20, "Passing": 0.15, "Composure": 0.15,
    "Tackling": 0.15, "Technique": 0.10, "Vision": 0.10,
    "Strength": 0.15
  },
  "Cover": {
    "Anticipation": 0.20, "Passing": 0.15, "Composure": 0.15,
    "Pace": 0.15, "Positioning": 0.10, "Technique": 0.10,
    "Decisions": 0.15
  }
},
"No-Nonsense Centre-Back": {
  "Defend": {
    "Marking": 0.25, "Tackling": 0.25, "Heading": 0.20,
    "Strength": 0.15, "Jumping Reach": 0.10, "Bravery": 0.05
  }
},
"Libero": {
  "Defend": {
    "Positioning": 0.20, "Marking": 0.15, "Tackling": 0.15,
    "Passing": 0.15, "Composure": 0.15, "Vision": 0.10,
    "Technique": 0.10
  },
  "Support": {
    "Passing": 0.20, "Composure": 0.20, "Vision": 0.15,
    "Technique": 0.15, "Anticipation": 0.10, "Acceleration": 0.10,
    "Dribbling": 0.10
  }
},
"Wide Centre-Back": {
  "Defend": {
    "Positioning": 0.20, "Marking": 0.15, "Tackling": 0.15,
    "Crossing": 0.10, "Passing": 0.10, "Stamina": 0.10,
    "Work Rate": 0.10, "Pace": 0.10
  },
  "Support": {
    "Passing": 0.20, "Crossing": 0.15, "Dribbling": 0.15,
    "Stamina": 0.10, "Work Rate": 0.10, "Technique": 0.10,
    "Positioning": 0.10, "Acceleration": 0.10
  },
  "Attack": {
    "Dribbling": 0.20, "Crossing": 0.15, "Passing": 0.15,
    "Technique": 0.15, "Acceleration": 0.10, "Off The Ball": 0.10,
    "Flair": 0.10, "Composure": 0.05
  }
},
"Full Back": {
  "Defend": {
    "Marking": 0.20, "Tackling": 0.18, "Positioning": 0.15,
    "Work Rate": 0.15, "Stamina": 0.12, "Teamwork": 0.10,
    "Passing": 0.10
  },
  "Support": {
    "Crossing": 0.20, "Passing": 0.15, "Work Rate": 0.15,
    "Stamina": 0.15, "Dribbling": 0.10, "Technique": 0.10,
    "Positioning": 0.10, "Tackling": 0.05
  },
  "Attack": {
    "Crossing": 0.22, "Dribbling": 0.18, "Work Rate": 0.15,
    "Technique": 0.15, "Acceleration": 0.10, "Off The Ball": 0.10,
    "Composure": 0.10
  }
},
"Complete Wing-Back": {
  "Support": {
    "Crossing": 0.20, "Dribbling": 0.18, "Work Rate": 0.15,
    "Stamina": 0.15, "Technique": 0.10, "Passing": 0.10,
    "Teamwork": 0.07, "Composure": 0.05
  },
  "Attack": {
    "Crossing": 0.20, "Dribbling": 0.20, "Acceleration": 0.15,
    "Technique": 0.15, "Off The Ball": 0.10, "Flair": 0.10,
    "Composure": 0.10
  }
},
"No-Nonsense Full Back": {
  "Defend": {
    "Marking": 0.25, "Tackling": 0.25, "Positioning": 0.20,
    "Strength": 0.10, "Work Rate": 0.10, "Jumping Reach": 0.10
  }
},
"Inverted Wing-Back": {
  "Defend": {
    "Marking": 0.18, "Tackling": 0.15, "Positioning": 0.15,
    "Passing": 0.15, "Composure": 0.10, "Vision": 0.10,
    "Work Rate": 0.12, "Technique": 0.05
  },
  "Support": {
    "Passing": 0.20, "Off The Ball": 0.15, "Dribbling": 0.15,
    "Composure": 0.15, "Vision": 0.10, "Work Rate": 0.10,
    "Pace": 0.10, "Technique": 0.05
  },
  "Attack": {
    "Dribbling": 0.20, "Off The Ball": 0.20, "Passing": 0.15,
    "Vision": 0.10, "Composure": 0.10, "Technique": 0.15,
    "Pace": 0.10, "Flair": 0.05
  }
},
"Defensive Midfielder": {
  "Defend": {
    "Positioning": 0.20, "Marking": 0.20, "Tackling": 0.18,
    "Teamwork": 0.12, "Strength": 0.10, "Concentration": 0.10,
    "Work Rate": 0.10
  },
  "Support": {
    "Passing": 0.20, "Vision": 0.15, "Teamwork": 0.15,
    "Positioning": 0.15, "Composure": 0.10, "Stamina": 0.10,
    "Work Rate": 0.15
  }
},
"Anchor Man": {
  "Defend": {
    "Positioning": 0.25, "Marking": 0.20, "Tackling": 0.20,
    "Strength": 0.15, "Work Rate": 0.10, "Concentration": 0.10
  }
},
"Half Back": {
  "Defend": {
    "Positioning": 0.20, "Marking": 0.20, "Tackling": 0.15,
    "Passing": 0.15, "Composure": 0.10, "Vision": 0.10,
    "Decisions": 0.10
  }
},
"Regista": {
  "Support": {
    "Passing": 0.25, "Vision": 0.20, "Technique": 0.15,
    "Composure": 0.15, "Anticipation": 0.10, "First Touch": 0.10,
    "Decisions": 0.05
  }
},
"Segundo Volante": {
  "Support": {
    "Work Rate": 0.20, "Passing": 0.15, "Stamina": 0.15,
    "Composure": 0.15, "Off The Ball": 0.10, "Technique": 0.10,
    "Positioning": 0.15
  },
  "Attack": {
    "Off The Ball": 0.20, "Passing": 0.15, "Technique": 0.15,
    "Composure": 0.15, "Stamina": 0.10, "Dribbling": 0.15,
    "Vision": 0.10
  }
},
"Central Midfielder": {
  "Defend": {
    "Positioning": 0.20, "Tackling": 0.18, "Strength": 0.15,
    "Work Rate": 0.15, "Teamwork": 0.10, "Passing": 0.10,
    "Stamina": 0.12
  },
  "Support": {
    "Passing": 0.20, "Vision": 0.18, "Decisions": 0.15,
    "Technique": 0.10, "Work Rate": 0.12, "Stamina": 0.10,
    "Teamwork": 0.10, "Positioning": 0.05
  },
  "Attack": {
    "Off The Ball": 0.20, "Long Shots": 0.18, "Technique": 0.15,
    "Passing": 0.12, "Composure": 0.10, "Flair": 0.10,
    "Finishing": 0.05
  }
},
"Box-To-Box Midfielder": {
  "Support": {
    "Stamina": 0.20, "Work Rate": 0.18, "Passing": 0.15,
    "Off The Ball": 0.15, "Composure": 0.10, "Dribbling": 0.10,
    "Positioning": 0.12
  }
},
"Ball Winning Midfielder": {
  "Defend": {
    "Tackling": 0.25, "Aggression": 0.20, "Positioning": 0.15,
    "Work Rate": 0.15, "Bravery": 0.10, "Teamwork": 0.10,
    "Anticipation": 0.05
  },
  "Support": {
    "Tackling": 0.20, "Work Rate": 0.20, "Positioning": 0.15,
    "Passing": 0.15, "Teamwork": 0.10, "Aggression": 0.10,
    "Decisions": 0.10
  }
},
"Deep-Lying Playmaker": {
  "Defend": {
    "Positioning": 0.20, "Passing": 0.20, "Composure": 0.15,
    "Vision": 0.15, "Technique": 0.10, "Teamwork": 0.10,
    "Decisions": 0.10
  },
  "Support": {
    "Passing": 0.25, "Vision": 0.20, "Composure": 0.15,
    "Technique": 0.15, "Decisions": 0.10, "Positioning": 0.10,
    "Teamwork": 0.05
  }
},
"Roaming Playmaker": {
  "Support": {
    "Passing": 0.20, "Off The Ball": 0.15, "Dribbling": 0.15,
    "Stamina": 0.15, "Work Rate": 0.10, "Technique": 0.10,
    "Composure": 0.10, "Vision": 0.05
  }
},
"Carrilero": {
  "Support": {
    "Positioning": 0.20, "Work Rate": 0.18, "Teamwork": 0.15,
    "Passing": 0.15, "Stamina": 0.10, "Composure": 0.10,
    "Decisions": 0.12
  }
},
"Mezzala": {
  "Support": {
    "Passing": 0.20, "Off The Ball": 0.15, "Technique": 0.15,
    "Dribbling": 0.15, "Composure": 0.10, "Flair": 0.10,
    "Stamina": 0.10, "Vision": 0.05
  },
  "Attack": {
    "Dribbling": 0.20, "Off The Ball": 0.20, "Technique": 0.15,
    "Flair": 0.15, "Passing": 0.10, "Vision": 0.10,
    "Composure": 0.10
  }
},
"Wide Midfielder": {
  "Defend": {
    "Positioning": 0.20, "Work Rate": 0.18, "Tackling": 0.15,
    "Teamwork": 0.15, "Stamina": 0.10, "Passing": 0.10,
    "Technique": 0.12
  },
  "Support": {
    "Crossing": 0.20, "Passing": 0.18, "Work Rate": 0.15,
    "Stamina": 0.15, "Dribbling": 0.10, "Off The Ball": 0.10,
    "Technique": 0.12
  },
  "Attack": {
    "Crossing": 0.22, "Dribbling": 0.18, "Off The Ball": 0.15,
    "Acceleration": 0.15, "Flair": 0.10, "Technique": 0.10,
    "Finishing": 0.10
  }
},
"Winger": {
  "Support": {
    "Crossing": 0.22, "Dribbling": 0.20, "Acceleration": 0.15,
    "Flair": 0.10, "Off The Ball": 0.10, "Stamina": 0.10,
    "Technique": 0.13
  },
  "Attack": {
    "Dribbling": 0.22, "Crossing": 0.20, "Acceleration": 0.15,
    "Flair": 0.15, "Off The Ball": 0.10, "Composure": 0.10,
    "Technique": 0.08
  }
},
"Inverted Winger": {
  "Support": {
    "Dribbling": 0.22, "Cutting Inside": 0.20, "Acceleration": 0.15,
    "Off The Ball": 0.10, "Vision": 0.10, "Technique": 0.13,
    "Finishing": 0.10
  },
  "Attack": {
    "Dribbling": 0.22, "Finishing": 0.18, "Acceleration": 0.15,
    "Off The Ball": 0.10, "Technique": 0.10, "Flair": 0.15,
    "Vision": 0.10
  }
},
"Wide Playmaker": {
  "Support": {
    "Vision": 0.22, "Passing": 0.20, "Technique": 0.18,
    "First Touch": 0.10, "Flair": 0.10, "Composure": 0.10,
    "Work Rate": 0.10
  },
  "Attack": {
    "Passing": 0.20, "Dribbling": 0.18, "Technique": 0.18,
    "Flair": 0.10, "Off The Ball": 0.10, "Vision": 0.15,
    "Composure": 0.09
  }
},
"Defensive Winger": {
  "Defend": {
    "Positioning": 0.22, "Work Rate": 0.20, "Tackling": 0.15,
    "Marking": 0.15, "Stamina": 0.10, "Teamwork": 0.10,
    "Concentration": 0.08
  },
  "Support": {
    "Crossing": 0.15, "Work Rate": 0.20, "Stamina": 0.15,
    "Teamwork": 0.15, "Positioning": 0.10, "Passing": 0.10,
    "Tackling": 0.10
  }
},
"Attacking Midfielder": {
  "Support": {
    "Passing": 0.20, "Vision": 0.18, "Off The Ball": 0.15,
    "Dribbling": 0.15, "Technique": 0.10, "First Touch": 0.10,
    "Flair": 0.12
  },
  "Attack": {
    "Dribbling": 0.20, "Off The Ball": 0.18, "Finishing": 0.15,
    "Passing": 0.15, "Flair": 0.10, "Composure": 0.10,
    "Technique": 0.12
  }
},
"Advanced Playmaker": {
  "Support": {
    "Vision": 0.25, "Passing": 0.22, "Composure": 0.15,
    "Technique": 0.15, "First Touch": 0.10, "Decisions": 0.10,
    "Teamwork": 0.03
  },
  "Attack": {
    "Dribbling": 0.20, "Flair": 0.18, "Off The Ball": 0.15,
    "Passing": 0.15, "Technique": 0.12, "Vision": 0.10,
    "Composure": 0.10
  }
},
"Shadow Striker": {
  "Attack": {
    "Off The Ball": 0.22, "Finishing": 0.20, "Anticipation": 0.15,
    "Composure": 0.15, "Dribbling": 0.10, "Technique": 0.10,
    "First Touch": 0.08
  }
},
"Enganche": {
  "Support": {
    "Vision": 0.25, "Passing": 0.20, "Technique": 0.15,
    "Composure": 0.15, "First Touch": 0.10, "Flair": 0.10,
    "Decisions": 0.05
  }
},
"Trequartista": {
  "Support": {
    "Dribbling": 0.20, "Flair": 0.18, "Passing": 0.15,
    "Technique": 0.15, "Vision": 0.15, "Composure": 0.10,
    "Off The Ball": 0.07
  },
  "Attack": {
    "Dribbling": 0.22, "Flair": 0.20, "Off The Ball": 0.15,
    "Passing": 0.15, "Technique": 0.13, "Composure": 0.10,
    "Vision": 0.05
  }
},
"Advanced Forward": {
  "Attack": {
    "Finishing": 0.25, "Off The Ball": 0.20, "Acceleration": 0.15,
    "Composure": 0.15, "Dribbling": 0.10, "Technique": 0.10,
    "Anticipation": 0.05
  }
},
"Complete Forward": {
  "Support": {
    "Passing": 0.20, "Dribbling": 0.18, "Technique": 0.15,
    "Composure": 0.15, "Vision": 0.10, "Off The Ball": 0.12,
    "First Touch": 0.10, "Heading": 0.08  
  },
  "Attack": {
    "Finishing": 0.22, "Off The Ball": 0.18, "Dribbling": 0.15,
    "Technique": 0.15, "Acceleration": 0.10, "Composure": 0.10,
    "Flair": 0.10, "Heading": 0.10  
  }
},
"Target Forward": {
  "Support": {
    "Heading": 0.25, "Strength": 0.20, "Off The Ball": 0.15,
    "Passing": 0.15, "Work Rate": 0.10, "First Touch": 0.10,
    "Vision": 0.05
  },
  "Attack": {
    "Finishing": 0.22, "Heading": 0.20, "Strength": 0.15,
    "Off The Ball": 0.12, "Composure": 0.10, "Technique": 0.10,
    "Jumping Reach": 0.11
  }
},
"Poacher": {
  "Attack": {
    "Finishing": 0.30, "Off The Ball": 0.25, "Anticipation": 0.15,
    "Composure": 0.10, "Acceleration": 0.10, "Technique": 0.10,
    "Heading": 0.10 
  }
},
"False Nine": {
  "Support": {
    "Passing": 0.22, "Technique": 0.20, "Vision": 0.18,
    "Off The Ball": 0.15, "Composure": 0.10, "Flair": 0.10,
    "Dribbling": 0.05
  }
},
"Deep-Lying Forward": {
  "Support": {
    "Passing": 0.22, "Vision": 0.20, "Composure": 0.15,
    "Technique": 0.15, "Off The Ball": 0.10, "First Touch": 0.10,
    "Decisions": 0.08
  },
  "Attack": {
    "Finishing": 0.20, "Off The Ball": 0.18, "Passing": 0.15,
    "Composure": 0.15, "Dribbling": 0.12, "Technique": 0.10
  }
},
"Pressing Forward": {
  "Defend": {
    "Work Rate": 0.25, "Aggression": 0.20, "Stamina": 0.15,
    "Acceleration": 0.10, "Tackling": 0.10, "Strength": 0.10,
    "Positioning": 0.10
  },
  "Support": {
    "Work Rate": 0.22, "Off The Ball": 0.18, "Acceleration": 0.15,
    "Passing": 0.12, "Dribbling": 0.10, "Technique": 0.10,
    "Composure": 0.13
  },
  "Attack": {
    "Finishing": 0.22, "Work Rate": 0.18, "Acceleration": 0.15,
    "Off The Ball": 0.12, "Composure": 0.10, "Flair": 0.10,
    "Dribbling": 0.13, "Heading": 0.08 
  }
},
"Trequartista": {
  "Support": {
    "Dribbling": 0.20, "Flair": 0.18, "Passing": 0.15,
    "Technique": 0.15, "Vision": 0.15, "Composure": 0.10,
    "Off The Ball": 0.07
  },
  "Attack": {
    "Dribbling": 0.22, "Flair": 0.20, "Off The Ball": 0.15,
    "Passing": 0.15, "Technique": 0.13, "Composure": 0.10,
    "Vision": 0.05
  }
}

}

def score_player_for_role(player, role, duty):
    score = 0
    weights = ROLE_ATTRIBUTES.get(role, {}).get(duty, {})
    
    for attr, weight in weights.items():
        score += player.get(attr, 0) * weight
    
    return round(score, 2)