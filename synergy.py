# synergy.py

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

def calculate_modifier(player1, player2):
    work_rate_diff = abs(player1.get("Work Rate", 10) - player2.get("Work Rate", 10)) * 0.01
    aggression_diff = abs(player1.get("Aggression", 10) - player2.get("Aggression", 10)) * 0.01
    return -(work_rate_diff + aggression_diff)

def calculate_synergy(role1, role2, player1_attrs, player2_attrs):
    key = (role1, role2)
    reverse_key = (role2, role1)
    base_score = SYNERGY_MATRIX.get(key) or SYNERGY_MATRIX.get(reverse_key) or 0.70
    modifier = calculate_modifier(player1_attrs, player2_attrs)
    return round(base_score + modifier, 2)

def is_role_supported(role, bench_players, threshold=10):
    from roles import score_player_for_role  # assumes this exists
    for sub in bench_players:
        score = score_player_for_role(sub["attributes"], role, "Support")
        if score >= threshold:
            return True
    return False

def select_best_pairing(possible_pairings, bench_players):
    scored = []
    for pairing in possible_pairings:
        role1, role2 = pairing["roles"]
        p1_attrs = pairing["player1"]["attributes"]
        p2_attrs = pairing["player2"]["attributes"]
        synergy = calculate_synergy(role1, role2, p1_attrs, p2_attrs)
        if is_role_supported(role1, bench_players) and is_role_supported(role2, bench_players):
            scored.append((pairing, synergy))
    if not scored:
        return None
    return max(scored, key=lambda x: x[1])[0]