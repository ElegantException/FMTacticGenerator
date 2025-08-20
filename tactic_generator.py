# tactic_generator.py
from roles import ROLE_ATTRIBUTES, score_player_for_role
from role_positions import ROLE_POSITION_MAP,ROLE_CATEGORIES
from formations import ZONE_MAP
import re
import csv
import os

CENTRAL_ROLES = {
    "Central Defender",
    "Defensive Midfielder",
    "Box-To-Box Midfielder",
    "Advanced Playmaker",
    "Attacking Midfielder",
    "Advanced Forward",
    "Poacher",
    "Target Forward",
    "Ball Winning Midfielder"
}

def sanity_check_instructions(instructions):
    out_pos = instructions.get('out_of_possession', {})
    in_pos = instructions.get('in_possession', {})
    transition = instructions.get('in_transition', {})

    # Defensive Line vs Line of Engagement
    def_line = out_pos.get('Defensive Line', 'Standard')
    engagement = out_pos.get('Line of Engagement', 'Standard')
    trigger_press = out_pos.get('Trigger Press', 'Standard')

    # Rule 1: Avoid High Line + Low Block
    if def_line in ['Higher', 'Much Higher'] and engagement == 'Low Block':
        out_pos['Line of Engagement'] = 'Mid Block'

    # Rule 2: High Line needs at least Standard Pressing
    if def_line in ['Higher', 'Much Higher'] and trigger_press in ['Much Less Often', 'Less Often']:
        out_pos['Trigger Press'] = 'Standard'

    # Rule 3: Tempo and Passing Directness synergy
    tempo = in_pos.get('Tempo', 'Standard')
    passing = in_pos.get('Passing Directness', 'Standard')
    if tempo in ['Higher', 'Much Higher'] and passing in ['Much Shorter', 'Shorter']:
        in_pos['Passing Directness'] = 'Standard'

    # Rule 4: Transition logic
    lost = transition.get('When Possession Lost', 'Regroup')
    won = transition.get('When Possession Won', 'Hold Shape')
    if lost == 'Counter-Press' and won == 'Hold Shape':
        transition['When Possession Won'] = 'Counter'

    # Update instructions
    instructions['out_of_possession'] = out_pos
    instructions['in_possession'] = in_pos
    instructions['in_transition'] = transition

    return instructions

def analyze_formation_gaps(lineup):
    analysis = []

    # Gather all zones covered
    all_zones = set()
    for p in lineup:
        all_zones.update(p.get("zones", []))

    # Define critical zone clusters
    lateral_midfield_zones = {"B2", "B3", "C3", "G2", "G3", "F3"}
    central_midfield_zones = {"D2", "E2", "D3", "E3"}
    final_third_zones = {"D4", "E4", "C4", "F4", "G4", "H4", "A4", "B4"}

    # Check lateral midfield coverage
    if lateral_midfield_zones - all_zones:
        analysis.append({
            "Area": "Midfield lateral coverage",
            "Verdict": "⚠️ Slight risk",
            "Fix": "Flex a CM to Carrilero or Mezzala to cover wide midfield zones"
        })

    # Check central midfield density
    cm_count = sum(1 for p in lineup if "Midfielder" in p["position"] or "Playmaker" in p["position"])
    if cm_count < 2:
        analysis.append({
            "Area": "Central midfield density",
            "Verdict": "⚠️ Thin",
            "Fix": "Add a connector like BBM or DLP to stabilize transitions"
        })

    # Check AM role duty
    am_roles = {"Attacking Midfielder", "Advanced Playmaker", "Shadow Striker", "Trequartista", "Enganche"}
    am_players = [p for p in lineup if p["position"] in am_roles]
    for am in am_players:
        if am.get("duty") == "Support":
            analysis.append({
                "Area": "Transition link",
                "Verdict": "⚠️ Passive AM",
                "Fix": "Switch AM to Attack duty or use Shadow Striker for vertical threat"
            })

    # Check fullback aggression
    fb_roles = {"Full Back", "Wing Back", "Complete Wing Back"}
    fb_support_count = sum(1 for p in lineup if p["position"] in fb_roles and p.get("duty") == "Support")
    if fb_support_count == len([p for p in lineup if p["position"] in fb_roles]):
        analysis.append({
            "Area": "Wide overlap",
            "Verdict": "⚠️ Conservative",
            "Fix": "Change one FB to Attack duty to stretch wide zones"
        })

    # Check final third presence
    if final_third_zones - all_zones:
        analysis.append({
            "Area": "Final third threat",
            "Verdict": "⚠️ Limited penetration",
            "Fix": "Add an extra forward or push AM to Attack duty"
        })

    # Fallback if no issues
    if not analysis:
        analysis.append({
            "Area": "Overall",
            "Verdict": "✅ Balanced",
            "Fix": "No major gaps detected"
        })

    return analysis

def is_side_compatible(player_sides, target_side, role):
    player_sides = [s.upper() for s in player_sides]  # normalize case
    target_side = target_side.upper()

    if role in CENTRAL_ROLES:
        return "C" in player_sides or target_side in player_sides
    return target_side in player_sides


class TacticGenerator:
    def __init__(self, players):
        """
        players: list of dicts with keys like:
        {
            'Name': 'John Smith',
            'Position': 'MC',
            'Attributes': {'Passing': 13, 'Tackling': 9, ...}
        }
        """
        self.players = players
        self.full_squad = list(players)  # Preserve original squad for substitutions
        self.formation = None
        self.mentality = None
        self.instructions = {
            "in_possession": {},
            "in_transition": {},
            "out_of_possession": {}
        }
        self.player_roles = {}  # key = player name, value = (role, duty)
        self.role_weights = ROLE_ATTRIBUTES
    def match_side(self, side_a, side_b):
        if isinstance(side_b, list):
            return side_a in side_b
        elif isinstance(side_b, str):
            return side_a in side_b.split("/")
        else:
            return False

    def score_player_for_role(self, attributes, weights, formation=None, role=None):
        multipliers = {}
        if formation and role:
            multipliers = formation.get("attribute_multipliers", {}).get(role, {})

        score = 0
        for attr, weight in weights.items():
            multiplier = multipliers.get(attr, 1.0)
            score += attributes.get(attr, 0) * weight * multiplier

        return round(score, 2)

    def assign_best_players_to_formation(self, formation, variants):
        squad = []
        used_players = set()
        formation_roles = formation["roles"]

        for slot in formation_roles:
            role = slot["role"]
            side = slot["side"]
            duty = slot["duty"]

            # Filter matching variants not already assigned
            candidates = [
                v for v in variants
                if (
                    v["role"] == role and
                    v["duty"] == duty and
                    is_side_compatible(v["side"], side, role) and
                    v["name"] not in used_players
                )
            ]

            best = None
            best_score = -1

            for v in candidates:
                weights = self.role_weights[v["role"]][v["duty"]]
                score = self.score_player_for_role(
                    v["attributes"],
                    weights,
                    formation=formation,
                    role=v["role"]
                )
                if score > best_score:
                    best = v
                    best_score = score

            if best:
                squad.append({
                    "position": role,
                    "side": side,
                    "duty": duty,
                    "player": best["name"],
                    "score": best_score,
                    "attributes": best["attributes"]
                })
                used_players.add(best["name"])

        return squad
       
    def _parse_position_string(self, position_str):
        import re
        import sys
        role_segment = re.split(r'\s*/\s*', position_str.split('(')[0].strip())
        side_match = re.search(r'\((.*?)\)', position_str)
        sides = list(side_match.group(1)) if side_match else ['C']

        tokens = []
        full_sides = []
        
        for role in role_segment:
            role = role.strip()
            
            for side in sides:
                full_token = f"{role}{'' if side == 'C' else side}"
                tokens.append(full_token)
                full_sides.append(side)
                
        return tokens # Only return the full tokens, no main_pos or side
    
    def _parse_side_string(self, position_str):
        import re
        import sys
        role_segment = re.split(r'\s*/\s*', position_str.split('(')[0].strip())
        side_match = re.search(r'\((.*?)\)', position_str)
        sides = list(side_match.group(1)) if side_match else ['C']

        full_sides = []
        
        for role in role_segment:
            role = role.strip()
            
            for side in sides:
                full_sides.append(side)
                
        return full_sides # Only return the full tokens, no main_pos or side
        
    def generate_player_variants(self, players):
        variants = []

        for player in players:
            for pos_str in player.get("Positions", []):
                tokens = self._parse_position_string(pos_str)  # e.g. "AM (LC)" → ["AML", "AMC"]
                sides = self._parse_side_string(pos_str)  # e.g. "AM (LC)" → ["AML", "AMC"]
                for role, valid_positions in ROLE_POSITION_MAP.items():
                    if any(token in valid_positions for token in tokens):
                        for duty, weights in ROLE_ATTRIBUTES.get(role, {}).items():
                            score = self.score_player_for_role(player["attributes"], weights)

                            variant = {
                                "name": player["Name"],
                                "role": role,
                                "side": sides,
                                "duty": duty,
                                "score": round(score, 2),
                                "position": pos_str,
                                "attributes": player["attributes"]
                            }
                            variants.append(variant)

        return sorted(variants, key=lambda x: x["score"], reverse=True)
    
    
    
    def suggest_mentality(self, instructions=None):
        # Attribute-based mobility score
        pace_scores = [p['attributes'].get('Pace', 0) for p in self.players]
        otb_scores  = [p['attributes'].get('Off The Ball', 0) for p in self.players]
        avg_attr = (sum(pace_scores) + sum(otb_scores)) / (2 * len(self.players))

        # Role-based aggression score
        aggressive_roles = {
            "Poacher", "Advanced Forward", "Shadow Striker",
            "Mezzala", "Inside Forward", "Inverted Winger"
        }
        role_aggression = sum(
            1 for p in self.players
            if p.get("position") in aggressive_roles or
            (p.get("position") in {"Wing Back", "Full Back"} and p.get("duty") == "Attack")
        )

        # Zone-based attacking presence
        final_third_zones = {"D4", "E4", "F4", "G4", "H4", "C4", "B4", "A4"}
        zone_coverage = set(zone for p in self.players for zone in p.get("zones", []))
        final_third_presence = len(final_third_zones & zone_coverage)

        # Base score from mobility
        score = avg_attr + 0.6 * role_aggression + 0.4 * final_third_presence

        # Instruction-based modifiers
        if instructions:
            tempo = instructions['in_possession'].get('Tempo', 'Standard')
            passing = instructions['in_possession'].get('Passing Directness', 'Standard')
            pressing = instructions['out_of_possession'].get('Trigger Press', 'Standard')
            defensive_line = instructions['out_of_possession'].get('Defensive Line', 'Standard')
            transition = instructions['in_transition'].get('When Possession Lost', 'Regroup')
            final_third = instructions['in_possession'].get('Final Third', {})
            creative_freedom = instructions['in_possession'].get('Creative Freedom', 'Off')

            score += {'Lower': -2, 'Slightly Lower': -1, 'Standard': 0, 'Slightly Higher': 1, 'Higher': 2}.get(tempo, 0)
            score += {'Much Shorter': -2, 'Shorter': -1, 'Standard': 0, 'More Direct': 1, 'Much More Direct': 2}.get(passing, 0)
            score += {'Much Less Often': -2, 'Less Often': -1, 'Standard': 0, 'More Often': 1, 'Much More Often': 2}.get(pressing, 0)
            score += {'Much Lower': -2, 'Lower': -1, 'Standard': 0, 'Higher': 1, 'Much Higher': 2}.get(defensive_line, 0)
            score += 1 if transition == 'Counter-Press' else -1
            score += 1 if 'Shoot on Sight' in final_third else 0
            score -= 1 if 'Work Ball Into Box' in final_third else 0
            score += 1 if creative_freedom == 'Be More Expressive' else -1 if creative_freedom == 'Be More Disciplined' else 0

        # Final mentality decision
        if score >= 16:
            self.mentality = "Attacking"
        elif score >= 13:
            self.mentality = "Positive"
        elif score >= 10:
            self.mentality = "Balanced"
        else:
            self.mentality = "Cautious"

        return self.mentality
    
    def find_best_roles_per_player(self):
        scored_players = []
        full_score_players = []
        for player in self.players:
            attributes = player.get("attributes", {})
            name = player.get("Name", "")

            # Pull positions from "Position", "Sec. Position" or fallback "Positions"
            raw_positions = (
                player.get("Position", "").split(",") +
                player.get("Sec. Position", "").split(",") +
                player.get("Positions", [])
            )

            normalized_positions = [
                self.normalize_position(pos.strip()) for pos in raw_positions if pos.strip()
            ]

            roles = set()
            for norm_pos in normalized_positions:
                matched_roles = self.detect_roles_from_positions(norm_pos)

                if norm_pos == "GK":
                    matched_roles += ["Sweeper Keeper"]

                roles.update(matched_roles)
            

            best_score = -1
            best_role = None
            best_duty = None

            for role in roles:
                duties = ROLE_ATTRIBUTES.get(role, {})
                for duty, weights in duties.items():
                    score = sum(attributes.get(attr, 0) * weight for attr, weight in weights.items())
                    
                    
                    if score > best_score:
                        best_score = score
                        best_role = role
                        best_duty = duty
                
                full_score_players.append({
                    "name": name,
                    "position": normalized_positions,
                    "role": role,
                    "duty": duty,
                    "attributes": attributes,
                    "score": round(score, 2)

                })

            if best_role and best_duty:
                scored_players.append({
                    "name": name,
                    "position": normalized_positions,
                    "role": best_role,
                    "duty": best_duty,
                    "attributes": attributes,
                    "score": best_score
                })

        

        # 🎯 Final selection: 1 GK + Top 10 outfielders
        scored_players.sort(key=lambda p: p["score"], reverse=True)
        gks = [p for p in scored_players if "GK" in p["position"]]
        outfield = [p for p in scored_players if "GK" not in p["position"]]
        final_squad = gks[:1] + outfield[:10]
        
        return full_score_players
    
    def normalize_position(self, pos_str):
        """
        Converts a raw position string like 'D (C)' to 'DC'
        """
        return pos_str.replace(" ", "").replace("(", "").replace(")", "").upper()
    
      
    def generate_instructions(self, best_formation_name):
        # Formation checks
        is_wide_formation = best_formation_name in [
            "4-3-3", "3-4-3", "4-2-3-1 Wide", "4-2-4", "4-4-2", "4-5-1", "4-4-1-1", "3-1-4-2"
        ]

        is_narrow_formation = best_formation_name in [
            "4-4-2 Diamond", "4-1-2-1-2 Narrow", "4-3-1-2", "4-2-2-2 Narrow", "4-3-2-1 Christmas Tree"
        ]

        is_back_three = best_formation_name.startswith("3-") or best_formation_name in [
            "3-4-3", "3-5-2", "3-4-2-1", "3-4-1-2", "3-1-4-2"
        ]

        # Role counters and groups
        attacking_roles = 0
        creative_roles = 0
        pressing_roles = 0
        wide_roles_count = 0
        central_roles_count = 0
        defenders = []
        full_backs = []
        gk = None

        # Attribute accumulators
        total_pace = total_work_rate = total_crossing = total_shooting = 0

        for p in self.players:
            position = p.get('position', '')
            duty = p.get('duty', '')
            attributes = p.get('attributes', {})

            total_pace += attributes.get('Pace', 0)
            total_work_rate += attributes.get('Work Rate', 0)
            total_crossing += attributes.get('Crossing', 0)
            total_shooting += attributes.get('Finishing', 0)

            if position == 'Goalkeeper':
                gk = {'name': p.get('player', ''), 'attributes': attributes}

            category = ROLE_CATEGORIES.get(position, '')
            if category == 'Attacker':
                attacking_roles += 1
            elif category == 'Midfielder':
                creative_roles += 1
            elif category == 'Defender':
                defenders.append(p)

            if 'Pressing' in position or 'Ball Winning' in position:
                pressing_roles += 1

            if position in ['Winger', 'Wing-Back', 'Inverted Winger']:
                wide_roles_count += 1

            if position in ['Wing-Back', 'Full-Back']:
                full_backs.append(p)

            if position in ['Central Midfielder', 'Attacking Midfielder', 'Defensive Midfielder']:
                central_roles_count += 1

        # Averages
        avg_tempo = total_pace / max(1, len(self.players))
        avg_work_rate = total_work_rate / max(1, len(self.players))
        avg_def_pace = sum(p['attributes'].get('Pace', 0) for p in defenders) / max(1, len(defenders))
        cb_avg_passing = sum(p['attributes'].get('Passing', 0) for p in defenders) / max(1, len(defenders))
        fb_avg_passing = sum(p['attributes'].get('Passing', 0) for p in full_backs) / max(1, len(full_backs))
        avg_crossing = total_crossing / max(1, wide_roles_count)
        avg_shooting = total_shooting / max(1, attacking_roles)

        # Role presence
        playmaker_present = any(p.get('position') in ['Deep-Lying Playmaker', 'Advanced Playmaker'] for p in self.players)
        target_forward_present = any(p.get('position') == 'Target Forward' for p in self.players)

        # GK Distribution
        distribution_area = "No Setting"
        distribution_type = "No Setting"

        if gk:
            a = gk['attributes']
            composure = a.get('Composure', 0)
            vision = a.get('Vision', 0)
            kicking = a.get('Kicking', 0)
            throwing = a.get('Throwing', 0)

            if playmaker_present:
                distribution_area = "Distribute to Playmaker"
            elif wide_roles_count >= 2:
                distribution_area = "Distribute to Flanks"
            elif target_forward_present:
                distribution_area = "Distribute to Target Forward"
            elif kicking > 14 and vision > 13:
                distribution_area = "Distribute Over Opposition Defence"
            elif len(full_backs) >= 2 and fb_avg_passing > 12:
                distribution_area = "Distribute to Full-Backs" if composure <= 12 else "Distribute to Centre-Backs and Full-Backs"
            elif composure > 12 and cb_avg_passing > 12:
                distribution_area = "Distribute to Centre-Backs"

            if throwing > 14:
                distribution_type = "Throw It Long"
            elif kicking > 14:
                distribution_type = "Take Long Kicks"
            elif kicking > 10:
                distribution_type = "Take Short Kicks"
            elif throwing > 10:
                distribution_type = "Roll It Out"

        # Approach Play Logic
        focus_left = wide_roles_count >= 1
        focus_right = wide_roles_count >= 1
        focus_middle = central_roles_count >= 3 and wide_roles_count <= 1

        left_fullback_role = "Attack"  # Placeholder
        right_fullback_role = "Attack"
        left_winger_role = "Support"
        right_winger_role = "Support"

        underlap_left = left_fullback_role == "Support" and left_winger_role == "Attack"
        underlap_right = right_fullback_role == "Support" and right_winger_role == "Attack"
        overlap_left = left_fullback_role == "Attack" and left_winger_role == "Support"
        overlap_right = right_fullback_role == "Attack" and right_winger_role == "Support"

        if underlap_left and overlap_left:
            overlap_left = False
        if underlap_right and overlap_right:
            overlap_right = False

        # Final Third Logic
        shoot_on_sight = avg_shooting >= 13 and creative_roles <= 2
        work_ball_into_box = not shoot_on_sight and avg_tempo >= 12 and creative_roles >= 2
        hit_early_crosses = shoot_on_sight and avg_crossing >= 12

        if is_wide_formation and avg_crossing >= 13:
            cross_type = "Whipped Crosses"
        elif is_narrow_formation or work_ball_into_box:
            cross_type = "Low Crosses"
        elif is_back_three:
            cross_type = "Mixed Crosses"
        else:
            cross_type = "Floated Crosses"

        # IN POSSESSION
        self.instructions['in_possession'] = {
            "Attacking Width": (
                "Wide" if is_wide_formation else
                "Narrow" if is_narrow_formation else
                "Fairly Narrow" if wide_roles_count <= 1 else
                "Standard"
            ),

            # APPROACH PLAY — Only active instructions
            "Approach Play": {
                **{"Pass Into Space": avg_tempo > 13 and attacking_roles >= 3},
                **{k: v for k, v in {
                    "Play Out Of Defence": cb_avg_passing >= 12,
                    "Focus Play Down The Left": focus_left and not focus_middle,
                    "Focus Play Down The Right": focus_right and not focus_middle,
                    "Focus Play Through The Middle": focus_middle,
                    "Underlap Left": underlap_left and not overlap_left,
                    "Underlap Right": underlap_right and not overlap_right,
                    "Overlap Left": overlap_left and not underlap_left,
                    "Overlap Right": overlap_right and not underlap_right
                }.items() if v}
            },

            "Passing Directness": (
                "Much Shorter" if creative_roles >= 3 and is_narrow_formation else
                "Shorter" if creative_roles >= 2 else
                "Standard"
            ),
            "Tempo": (
                "Higher" if avg_tempo >= 15 else
                "Slightly Higher" if avg_tempo >= 13 else
                "Standard" if avg_tempo >= 11 else
                "Slightly Lower" if avg_tempo >= 9 else
                "Lower"
            ),
            "Time Wasting": (
                "Frequently" if avg_work_rate < 10 else
                "Sometimes" if avg_work_rate < 14 else
                "Never"
            ),

            "Final Third": {
                **({"Work Ball Into Box": True} if work_ball_into_box else {}),
                **({"Shoot on Sight": True} if shoot_on_sight else {}),
                **({"Hit Early Crosses": True} if hit_early_crosses else {}),
                "Cross Type": cross_type  # Always set
            },
            
            "Play for Set Pieces": creative_roles <= 1 and attacking_roles <= 2,
            "Dribbling": (
                "Dribble Less" if avg_tempo < 11 else
                "Run at Defence" if attacking_roles >= 3 else
                "Off"
            ),
            "Creative Freedom": (
                "Be More Expressive" if creative_roles >= 3 else
                "Be More Disciplined" if creative_roles <= 1 else
                "Off"
            )            

        }

        # IN TRANSITION
        self.instructions['in_transition'] = {
            "When Possession Lost": "Counter-Press" if pressing_roles >= 2 else "Regroup",
            "When Possession Won": "Counter" if avg_tempo > 12 else "Hold Shape",
            "GK In Possession": "Slow Down Pace" if gk and gk['attributes'].get('Vision', 0) > 13 else "Distribute Quickly",
            "Distribution Area": distribution_area,
            "GK Distribution Type": distribution_type
        }

        # OUT OF POSSESSION
        self.instructions['out_of_possession'] = {
            "Defensive Line": (
                "Much Higher" if avg_def_pace >= 15 else
                "Higher" if avg_def_pace >= 13 else
                "Standard" if avg_def_pace >= 11 else
                "Lower" if avg_def_pace >= 9 else
                "Much Lower"
            ),
            "Line of Engagement": (
                "High Press" if pressing_roles >= 3 else
                "Mid Block" if pressing_roles == 2 else
                "Low Block"
            ),
            "Trigger Press": (
                "Much More Often" if pressing_roles >= 4 else
                "More Often" if pressing_roles == 3 else
                "Standard" if pressing_roles == 2 else
                "Less Often" if pressing_roles == 1 else
                "Much Less Often"
            ),
            "Prevent Short GK": True,
            
            "Tackling": (
                "Get Stuck In" if avg_work_rate > 14 else
                "Stay on Feet" if avg_work_rate < 10 else
                "OFF"
            ),
            "Defensive Line Setup": (
                "Drop Off More" if avg_def_pace < 11 else
                "Step Up More" if avg_def_pace > 14 else
                "OFF"
            ),
            "Pressing Trap": (
                "Trap Inside" if creative_roles >= 2 else
                "Trap Outside" if wide_roles_count >= 2 else
                "OFF"
            ),
             "Cross Engagement": (
                "Stop Crosses" if is_narrow_formation
                else "Invite Crosses" if is_back_three
                else "Invite Crosses" if sum(1 for p in defenders if p["attributes"].get("Heading", 0) >= 14) >= 3
                else None
            )
        }

        return self.instructions
       
    def generate_variants(self):
        """
        Returns a dict of tactic variants: 'Home', 'Away', 'Vs Strong Opponent'
        """
        base_roles = self.player_roles.copy()
        base_instructions = self.generate_instructions()
        base_mentality = self.mentality

        # Variant: Away
        away_instructions = base_instructions.copy()
        away_instructions['in_possession']['Passing Directness'] = "Shorter"
        away_instructions['in_possession']['Tempo'] = "Lower"
        away_instructions['in_possession']['Time Wasting'] = "Sometimes"
        away_instructions['in_transition']['When Possession Won'] = "Hold Shape"
        away_instructions['out_of_possession']['Defensive Line'] = "Standard"
        away_instructions['out_of_possession']['Pressing Intensity'] = "Standard"

        # Variant: Vs Strong Opponent
        tough_instructions = base_instructions.copy()
        tough_instructions['in_possession']['Attacking Width'] = "Very Narrow"
        tough_instructions['in_possession']['Passing Directness'] = "Much Shorter"
        tough_instructions['in_transition']['When Possession Lost'] = "Regroup"
        tough_instructions['in_transition']['When Possession Won'] = "Counter"
        tough_instructions['out_of_possession']['Defensive Line'] = "Lower"
        tough_instructions['out_of_possession']['Line of Engagement'] = "Lower"
        tough_instructions['out_of_possession']['Pressing Intensity'] = "Less Urgent"
        tough_instructions['out_of_possession']['Trigger Press'] = "Less Often"
        tough_instructions['in_possession']['Time Wasting'] = "Frequently"

        return {
            "Home": {
                "formation": self.formation,
                "mentality": base_mentality,
                "roles": base_roles,
                "instructions": base_instructions
            },
            "Away": {
                "formation": self.formation,
                "mentality": "Balanced",
                "roles": base_roles,
                "instructions": away_instructions
            },
            "Vs Strong Opponent": {
                "formation": self.formation,
                "mentality": "Cautious",
                "roles": base_roles,
                "instructions": tough_instructions
            }
        }
    
    def flex_roles_with_zone_coverage(self, lineup):
        from collections import defaultdict, Counter

        # Define which roles are considered midfield
        MIDFIELD_ROLES = [
            "Defensive Midfielder", "Anchor Man", "Half Back", "Regista", "Segundo Volante", "Ball Winning Midfielder",
            "Central Midfielder", "Box-To-Box Midfielder", "Mezzala", "Carrilero", "Deep-Lying Playmaker", "Roaming Playmaker",
            "Attacking Midfielder", "Advanced Playmaker", "Shadow Striker", "Enganche", "Trequartista"
        ]

        # Filter midfielders from lineup
        midfielders = [p for p in lineup if p["position"] in MIDFIELD_ROLES]

        # Group by role
        role_groups = defaultdict(list)
        for p in midfielders:
            role_groups[p["position"]].append(p)

        # Assign sides based on count
        for role, players_in_role in role_groups.items():
            count = len(players_in_role)
            if count == 1:
                sides = ["C"]
            elif count == 2:
                sides = ["L", "R"]
            elif count == 3:
                sides = ["L", "C", "R"]
            else:
                sides = ["C"] * count  # fallback

            for player, side in zip(players_in_role, sides):
                player["side"] = side
                player["zones"] = ZONE_MAP.get(role, {}).get(side) or ZONE_MAP.get(role, {}).get("C", [])

        # Analyze zone coverage
        zone_counter = Counter()
        for p in midfielders:
            zone_counter.update(p.get("zones", []))

        # Detect overlaps and gaps
        overlapping_zones = [z for z, c in zone_counter.items() if c > 1]
        all_midfield_zones = set(
            z for zones in ZONE_MAP.values() for zlist in zones.values() for z in zlist
            if z[1] in ["2", "3"]  # midfield bands
        )
        uncovered_zones = [z for z in all_midfield_zones if z not in zone_counter]



        # Optional: attempt to resolve overlaps by swapping roles
        # (This part can be expanded with smarter logic or synergy scoring)
        for p in midfielders:
            if any(z in overlapping_zones for z in p.get("zones", [])):
                # Try alternative roles for this player
                alternatives = [
                    r for r in ROLE_POSITION_MAP.keys()
                    if r in MIDFIELD_ROLES and r != p["position"]
                ]
                best_alternative = p["position"]
                best_score = p["score"]
                for alt_role in alternatives:
                    alt_side = p.get("side", "C")
                    alt_zones = ZONE_MAP.get(alt_role, {}).get(alt_side) or ZONE_MAP.get(alt_role, {}).get("C", [])
                    overlap_penalty = sum(zone_counter[z] for z in alt_zones if zone_counter[z] > 1)
                    if overlap_penalty == 0:
                        # Accept this alternative if it avoids overlap
                        best_alternative = alt_role
                        break

                if best_alternative != p["position"]:
                    p["position"] = best_alternative
                    p["zones"] = ZONE_MAP.get(best_alternative, {}).get(p["side"], [])

        return lineup

class SquadAnalyzer:
    def __init__(self, squad):
        self.squad = squad
        self.positions = [p.get("position") for p in squad if p.get("position")]
        self.position_counts = self._count_positions()

    def _count_positions(self):
        counts = {}
        for pos in self.positions:
            counts[pos] = counts.get(pos, 0) + 1
        return counts

    def get_role_avg(self, roles, attributes):
        players = [p for p in self.squad if p.get("position") in roles]
        if not players:
            #print(f"⚠️ No players found for roles: {roles}")
            return {attr: 0 for attr in attributes}

        return {
            attr: sum(p["attributes"].get(attr, 0) for p in players) / len(players)
            for attr in attributes
        }

    def get_min_attribute(self, role, attribute):
        values = [p["attributes"].get(attribute, 0) for p in self.squad if p.get("position") == role]
        if not values:
            #print(f"⚠️ No players found for role: {role}")
            return 0
        return min(values)

    def get_max_attribute(self, roles, attribute):
        values = [p["attributes"].get(attribute, 0) for p in self.squad if p.get("position") in roles]
        if not values:
            #print(f"⚠️ No players found for roles: {roles}")
            return 0
        return max(values)

    def has_role(self, role):
        return role in self.positions

    def has_any_role(self, roles):
        return any(role in self.positions for role in roles)

    def get_formation(self):
        # Infer formation from position counts
        def_count = sum(1 for r in self.positions if "Defender" in r)
        mid_count = sum(1 for r in self.positions if "Midfielder" in r)
        fwd_count = sum(1 for r in self.positions if "Forward" in r or "Striker" in r)

        return f"{def_count}-{mid_count}-{fwd_count}"

    def get_position_count(self, role):
        return self.position_counts.get(role, 0)

    def get_attribute_distribution(self, attribute):
        return [p["attributes"].get(attribute, 0) for p in self.squad if attribute in p["attributes"]]

    def get_average_attribute(self, attribute):
        values = self.get_attribute_distribution(attribute)
        return sum(values) / len(values) if values else 0

    def get_squad_summary(self):
        return {
            "Total Players": len(self.squad),
            "Formation": self.get_formation(),
            "Position Counts": self.position_counts,
            "Average Work Rate": self.get_average_attribute("Work Rate"),
            "Average Stamina": self.get_average_attribute("Stamina"),
            "Average Flair": self.get_average_attribute("Flair")
        }


class RoleAdjuster:
    def suggest_role(self, player):
        if player.get("role") == "AM" and player["attributes"].get("Tackling", 0) > 12:
            return "CM(Support)"
        if player.get("role") == "Winger" and player["attributes"].get("Pace", 0) < 11:
            return "Wide Midfielder(Support)"
        if player.get("role") == "ST" and player["attributes"].get("Strength", 0) > 14:
            return "Target Man(Support)"
        return player.get("role", "Unknown")

class OutOfPossessionInstructions:
    def __init__(self, analyzer, opponent):
        self.analyzer = analyzer  # Your team analyzer
        self.opponent = opponent  # Opponent squad list

    def generate(self):
        return {
            "Out of Possession": {
                "Defensive Line": self._defensive_line(),
                "Line of Engagement": self._engagement_line(),
                "Trap": self._trap_logic(),
                "Cross Engagement": self._cross_engagement_logic(),
                "Pressing": self._pressing_intensity(),
                "Compactness": self._compactness(),
                "Marking": self._marking_strategy(),
                "Width": self._defensive_width()
            }
        }

    def _defensive_line(self):
        pacey_defenders = sum(1 for p in self.analyzer.squad if p["attributes"].get("Pace", 0) >= 14)
        fast_opponents = sum(1 for p in self.opponent if p["attributes"].get("Pace", 0) >= 15)

        if pacey_defenders >= 3 and fast_opponents < 2:
            return "Higher Defensive Line"
        elif fast_opponents >= 3:
            return "Lower Defensive Line"
        return "Standard Defensive Line"

    def _engagement_line(self):
        stamina_monsters = sum(1 for p in self.analyzer.squad if p["attributes"].get("Stamina", 0) >= 15)
        press_resistant_opponents = sum(1 for p in self.opponent if p["attributes"].get("Composure", 0) >= 14)

        if stamina_monsters >= 4 and press_resistant_opponents < 2:
            return "High Line of Engagement"
        return "Mid Block"

    def _trap_logic(self):
        weak_central = sum(1 for p in self.opponent if p["position"] in ["Central Midfielder", "Defensive Midfielder"]
                           and p["attributes"].get("Composure", 0) <= 11)
        dangerous_wings = sum(1 for p in self.opponent if p["position"] in ["Winger", "Wide Midfielder"]
                              and p["attributes"].get("Dribbling", 0) >= 14)

        if weak_central >= 2:
            return "Trap Inside"
        elif dangerous_wings >= 2:
            return "Trap Outside"
        return "Neutral Trap"

    def _cross_engagement_logic(self):
        strong_headers = sum(1 for p in self.analyzer.squad if p["attributes"].get("Heading", 0) >= 14)
        opponent_crossers = sum(1 for p in self.opponent if p["attributes"].get("Crossing", 0) >= 14)
        aerial_weakness = sum(1 for p in self.analyzer.squad if p["attributes"].get("Jumping Reach", 0) <= 10)

        if strong_headers >= 3 and opponent_crossers < 2:
            return "Invite Crosses"
        elif opponent_crossers >= 3 or aerial_weakness >= 3:
            return "Stop Crosses"
        return "Neutral"

    def _pressing_intensity(self):
        work_rate_avg = sum(p["attributes"].get("Work Rate", 0) for p in self.analyzer.squad) / len(self.analyzer.squad)
        composure_avg = sum(p["attributes"].get("Composure", 0) for p in self.opponent) / len(self.opponent)

        if work_rate_avg >= 14 and composure_avg <= 12:
            return "More Urgent Pressing"
        elif work_rate_avg <= 10:
            return "Standard Pressing"
        return "Balanced Pressing"

    def _compactness(self):
        aggression_avg = sum(p["attributes"].get("Aggression", 0) for p in self.analyzer.squad) / len(self.analyzer.squad)
        if aggression_avg >= 14:
            return "Very Compact"
        elif aggression_avg <= 10:
            return "Loose Shape"
        return "Balanced Compactness"

    def _marking_strategy(self):
        playmakers = [p for p in self.opponent if p["attributes"].get("Vision", 0) >= 15 and p["attributes"].get("Passing", 0) >= 15]
        if len(playmakers) >= 2:
            return "Man Mark Playmakers"
        dangerous_forwards = [p for p in self.opponent if p["position"] in ["Striker", "Inside Forward"]
                              and p["attributes"].get("Finishing", 0) >= 15]
        if len(dangerous_forwards) >= 2:
            return "Tight Marking on Forwards"
        return "Zonal Marking"

    def _defensive_width(self):
        wide_threats = sum(1 for p in self.opponent if p["position"] in ["Winger", "Wing Back"]
                           and p["attributes"].get("Acceleration", 0) >= 14)
        narrow_threats = sum(1 for p in self.opponent if p["position"] in ["Attacking Midfielder", "Striker"]
                             and p["attributes"].get("Off the Ball", 0) >= 14)

        if wide_threats >= 3:
            return "Wider Defensive Shape"
        elif narrow_threats >= 3:
            return "Narrow Defensive Shape"
        return "Standard Width"
    
class VariantGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.formation = analyzer.get_formation()  # e.g. "4-3-3", "3-5-2"

    def generate(self, scenario):
        if scenario == "ToughOpponent":
            return self._generate_variant(defensive=True)
        elif scenario == "ProtectLead":
            return self._generate_variant(protect=True)
        elif scenario == "LatePush":
            return self._generate_variant(attacking=True)
        return self._generate_variant()

    def _generate_variant(self, defensive=False, protect=False, attacking=False):
        instructions = {}

        # Mentality
        mentality = self._calculate_mentality(defensive, protect, attacking)
        instructions["Mentality"] = mentality

        # Out of Possession
        instructions["Out of Possession"] = self._out_of_possession(defensive, protect, attacking)

        # In Transition
        instructions["In Transition"] = self._in_transition(defensive, protect, attacking)

        # In Possession
        instructions["In Possession"] = self._in_possession(defensive, protect, attacking)

        return instructions

    def _calculate_mentality(self, defensive, protect, attacking):
        def_roles = ["Central Defender", "Defensive Midfielder", "Anchor Man"]
        def_stats = self.analyzer.get_role_avg(def_roles, ["Composure", "Positioning"])
        score = def_stats["Composure"] + def_stats["Positioning"]

        if attacking:
            return "Attacking" if score < 24 else "Positive"
        if protect:
            return "Defensive" if score > 24 else "Cautious"
        if defensive:
            return "Cautious" if score > 24 else "Defensive"
        return "Balanced"

    def _out_of_possession(self, defensive, protect, attacking):
        cb_pace = self.analyzer.get_min_attribute("Central Defender", "Pace")
        wide_roles = ["Full Back", "Wing Back"]
        has_wide_defenders = any(p["position"] in wide_roles for p in self.analyzer.squad)

        line = "Lower" if cb_pace <= 13 else "Higher" if cb_pace >= 15 else "Standard"
        engagement = "Low Block" if defensive or protect else "High Press" if attacking else "Mid Block"
        press_freq = "Much More Often" if attacking else "Much Less Often" if protect else "Balanced"
        tackling = "Get Stuck In" if attacking else "Stay on Feet"
        setup = "Drop Off More" if cb_pace < 11 else "Step Up More" if cb_pace > 14 else "OFF"
        trap = "Trap Outside" if has_wide_defenders else "Trap Inside"
        cross_engagement = self._cross_engagement_logic()

        return {
            "Defensive Line": line,
            "Line of Engagement": engagement,
            "Trigger Press": press_freq,
            "Prevent Short GK": True,
            "Tackling": tackling,
            "Defensive Line Setup": setup,
            "Pressing Trap": trap,
            "Cross Engagement": cross_engagement
        }

    def _in_transition(self, defensive, protect, attacking):
        passing_roles = ["Central Midfielder", "Deep-Lying Playmaker"]
        passing = self.analyzer.get_max_attribute(passing_roles, "Passing")
        accel = self.analyzer.get_role_avg(["Striker", "Box-To-Box Midfielder"], ["Acceleration"])["Acceleration"]

        lost = "Regroup" if defensive or protect else "Counter-Press" if attacking else "Balanced"
        won = "Counter" if passing >= 14 and accel >= 13 else "Hold Shape"
        area = "Quick" if attacking else "Centre Backs" if protect else "Full Backs"
        gk_type = "Take Long Kicks" if attacking else "Take Short Kicks"

        return {
            "When Possession Lost": lost,
            "When Possession Won": won,
            "Distribution Area": area,
            "GK Distribution Type": gk_type
        }

    def _in_possession(self, defensive, protect, attacking):
        tech = self.analyzer.get_role_avg(["Advanced Playmaker", "Attacking Midfielder"], ["Technique"])["Technique"]
        dribbling = self.analyzer.get_role_avg(["Winger", "Attacking Midfielder"], ["Dribbling"])["Dribbling"]
        flair = self.analyzer.get_role_avg(["Advanced Playmaker", "Trequartista"], ["Flair"])["Flair"]
        crossing = self.analyzer.get_role_avg(["Winger", "Wing Back"], ["Crossing"])["Crossing"]

        tempo = "Higher" if attacking else "Lowest" if protect else "Lower" if tech >= 13 else "Standard"
        passing = "Direct" if attacking else "Short" if tech >= 12 else "Mixed"
        width = "Wide" if "3" in self.formation.split("-")[0] else "Narrow" if protect else "Standard"
        cross_type = "Whipped Crosses" if crossing >= 13 else "Low Crosses" if protect else "Mixed Crosses"
        dribble = "Run at Defence" if dribbling >= 13 else "Dribble Less" if dribbling <= 10 else "Balanced"
        creativity = "Be More Expressive" if flair >= 14 else "Be More Disciplined" if flair <= 10 else "Balanced"
        time_wasting = "Maximum" if protect else "Never" if attacking else "Often"
        set_pieces = True if protect else False

        final_third = {
            "Work Ball Into Box": not attacking,
            "Shoot On Sight": attacking,
            "Hit Early Crosses": attacking,
            "Hold Shape": protect,
            "Cross Type": cross_type
        }

        return {
            "Tempo": tempo,
            "Passing": passing,
            "Width": width,
            "Final Third": final_third,
            "Time Wasting": time_wasting,
            "Play for Set Pieces": set_pieces,
            "Dribbling": dribble,
            "Creative Freedom": creativity
        }

    def _cross_engagement_logic(self):
        defenders = [p for p in self.analyzer.squad if p.get("position") in [
            "Central Defender", "Ball Playing Defender", "Full Back", "Wing Back"
        ]]
        if not defenders:
            return "Neutral"

        strong_headers = sum(1 for p in defenders if p["attributes"].get("Heading", 0) >= 14)
        wide_defenders = [p for p in defenders if p.get("position") in ["Full Back", "Wing Back"]]

        if strong_headers >= 3 and not wide_defenders:
            return "Invite Crosses"
        elif wide_defenders:
            return "Stop Crosses"
        return "Neutral"
