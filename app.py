# app.py
import streamlit as st
import pandas as pd
from parse_squad_html import parse_squad_html  # or wherever your parser is
from tactic_generator import TacticGenerator,analyze_formation_gaps,sanity_check_instructions,SquadAnalyzer, VariantGenerator
from role_positions import ROLE_POSITION_SHORT
from roles import ROLE_FLEX_MAP
from synergy import calculate_synergy, select_best_pairing
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from formations import formations, ZONE_MAP  # or define directly above if it's short
from collections import defaultdict
import base64

def render_pitch(lineup, roles, formation_name):
    player_data = []
    role_side_tracker = defaultdict(lambda: defaultdict(list))

    # Step 1: Organize player data
    for player in lineup:
        role = player["position"]
        side = player["side"].upper()
        role_side_tracker[role][side].append(player)

    formation_roles = {
        (r["role"], r["side"].upper()): r["position"]
        for r in roles
    }

    position_lookup = {}
    for player in lineup:
        role = player["position"]
        side = player["side"].upper()
        key = (role, side)

        if key in formation_roles:
            position_lookup[key] = formation_roles[key]
        elif key in ROLE_FLEX_MAP:
            position_lookup[key] = ROLE_FLEX_MAP[key]
        else:
            position_lookup[key] = (50, 50)  # fallback center

    for role, side_groups in role_side_tracker.items():
        for side, group in side_groups.items():
            for player in group:
                x, y = position_lookup.get((role, side), (0, 0))
                name = player["player"]
                initials = "".join([word[0].upper() for word in name.split() if word])
                position_codes = ROLE_POSITION_SHORT.get(role, ["?"])
                position_label = "/".join(position_codes)

                if len(position_codes) == 1 and not any(s in position_label for s in ["R", "L"]):
                    position_label += f" ({player['side'][0]})"

                player_data.append({
                    "x": y,
                    "y": x,
                    "Initials": initials,
                    "Full Name": name,
                    "PositionLabel": position_label,
                    "FullPosition": role,
                    "FullDuty": player["duty"],
                    "Duty": player["duty"][0]
                })

    df = pd.DataFrame(player_data)

    # Step 2: Create pitch layout
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=[0, 0, 100, 100, 0], y=[0, 100, 100, 0, 0],
                             mode='lines', line=dict(color="green", width=2), showlegend=False))

    # Shadow layer
    fig.add_trace(go.Scatter(
        x=df["x"], y=df["y"],
        mode="markers",
        marker=dict(size=52, color="rgba(0, 0, 0, 0.3)"),
        hoverinfo="skip",
        showlegend=False
    ))

    # Player markers
    fig.add_trace(go.Scatter(
        x=df["x"], y=df["y"],
        mode="markers",
        marker=dict(size=44, color="blue"),
        hovertext=df["Full Name"] + "<br>" + df["FullPosition"] + "<br>" + df["FullDuty"],
        hoverinfo="text",
        showlegend=False
    ))

    # Initials
    fig.add_trace(go.Scatter(
        x=df["x"], y=df["y"] + 2,
        mode="text",
        text=df["Initials"],
        textposition="middle center",
        textfont=dict(color="white", size=14, family="Arial"),
        showlegend=False
    ))

    # Position label
    fig.add_trace(go.Scatter(
        x=df["x"], y=df["y"] - 1.2,
        mode="text",
        text=df["PositionLabel"],
        textposition="middle center",
        textfont=dict(color="white", size=8, family="Arial"),
        showlegend=False
    ))

    # Duty label
    fig.add_trace(go.Scatter(
        x=df["x"], y=df["y"] - 4,
        mode="text",
        text="(" + df["Duty"] + ")",
        textposition="middle center",
        textfont=dict(color="white", size=8, family="Arial"),
        showlegend=False
    ))

    # Background pitch image
    with open("assets/fpitch.jpg", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    fig.update_layout(
        images=[dict(
            source="data:image/jpg;base64," + encoded_image,
            xref="x",
            yref="y",
            x=0,
            y=100,
            sizex=100,
            sizey=100,
            sizing="stretch",
            layer="below"
        )],
        xaxis=dict(range=[0, 100], showgrid=False, visible=False),
        yaxis=dict(range=[0, 100], showgrid=False, visible=False),
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(t=20, b=20, l=20, r=20)
    )

    # Step 5: Display in Streamlit
    st.plotly_chart(fig, use_container_width=True, key=f"pitch_{formation_name}")



def format_value(value):
    return f"""
        <div style='display: flex; align-items: center; height: 100%;'>
            <span style='background-color: #eee; padding: 4px 10px; border-radius: 6px; font-weight: bold;'>
                {str(value)}
            </span>
        </div>
    """

def format_cell(content, bold=False, pill=False, indent=False):
    # Convert booleans to Yes/No
    if isinstance(content, bool):
        content = "Yes" if content else "No"

    indent_style = "margin-left: 16px;" if indent else ""
    weight = "font-weight: bold;" if bold else "font-weight: normal;"
    pill_style = (
        "background-color: #eee; padding: 4px 10px; border-radius: 6px; font-weight: bold;"
        if pill else f"{weight} {indent_style}"
    )
    return f"""
        <div style='display: flex; align-items: center; min-height: 48px;'>
            <span style='{pill_style}'>{content}</span>
        </div>
    """

def display_instruction_block(title, emoji, instruction_data):
    with st.expander(f"{emoji} {title}"):
        for key, value in instruction_data.items():
            if isinstance(value, dict):
                # Section header
                st.markdown(format_cell(key, bold=True), unsafe_allow_html=True)
                for sub_key, sub_value in value.items():
                    col1, col2 = st.columns([1.5, 2.5])
                    col1.markdown(format_cell(f"• {sub_key}", indent=True), unsafe_allow_html=True) 
                    # Convert boolean to Yes/No
                    display_value = "Yes" if sub_value is True else "No" if sub_value is False else str(sub_value)
                    col2.markdown(format_cell(display_value, pill=True), unsafe_allow_html=True)
                    st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)
            else:
                col1, col2 = st.columns([1.5, 2.5])
                col1.markdown(format_cell(key, bold=True), unsafe_allow_html=True)
                display_value = "Yes" if value is True else "No" if value is False else str(value)
                col2.markdown(format_cell(display_value, pill=True), unsafe_allow_html=True)
                st.markdown("<hr style='margin: 4px 0;'>", unsafe_allow_html=True)

import copy

def apply_role_flex(lineup):
    role_pool = {
        "CM": ["Central Midfielder", "Box-To-Box Midfielder", "Deep-Lying Playmaker", "Mezzala"],
        "DM": ["Defensive Midfielder", "Anchor Man", "Half Back", "Regista"],
        "AM": ["Attacking Midfielder", "Advanced Playmaker", "Trequartista", "Shadow Striker"]
    }

    best_score = -float("inf")
    best_roles = None

    for cm in role_pool["CM"]:
        for dm in role_pool["DM"]:
            for am in role_pool["AM"]:
                score = 0
                if cm in ["Box-To-Box Midfielder", "Deep-Lying Playmaker"]: score += 2
                if dm == "Regista": score += 1
                if am == "Advanced Playmaker": score += 1
                if dm == "Anchor Man" and am == "Shadow Striker": score -= 2

                if score > best_score:
                    best_score = score
                    best_roles = (dm, cm, am)

    # Apply best roles only to the midfield trio
    flexed_lineup = copy.deepcopy(lineup)

    dm_index = next((i for i, p in enumerate(flexed_lineup) if p["position"] in role_pool["DM"]), None)
    cm_index = next((i for i, p in enumerate(flexed_lineup) if p["position"] in role_pool["CM"]), None)
    am_index = next((i for i, p in enumerate(flexed_lineup) if p["position"] in role_pool["AM"]), None)

    if best_roles:
        if dm_index is not None: flexed_lineup[dm_index]["position"] = best_roles[0]
        if cm_index is not None: flexed_lineup[cm_index]["position"] = best_roles[1]
        if am_index is not None: flexed_lineup[am_index]["position"] = best_roles[2]

    return flexed_lineup

# 🎨 Inject scrollbar CSS
st.markdown("""
    <style>
        /* Force scroll only on the entire body */
        html, body {
            overflow: auto !important;
        }

        /* Prevent internal components from hijacking scroll */
        .element-container, .main, .block-container {
            overflow: unset !important;
        }

        /* Optionally show the scrollbar */
        ::-webkit-scrollbar {
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Football Manager Tactic Generator")

# Title block with popup
col1, col2 = st.columns([0.12, 0.05])


with col1:
    st.markdown("### Upload your FM squad HTML export")

with col2:
    with st.popover("❓"):
        st.markdown("""
        1. Download and extract the squad view that contains all attributes:   
        <a href="/assets/FMTacticGenerator-all_attributes.zip" download style="text-decoration: none; color: #1E90FF;">
            📄 FMTacticGenerator-all_attributes.zip</a> <br>
        2. In Football Manager, go to your Squad screen.  <br>
        3. Go to the View and Import the downloaded file from step 1.  <br>
        4. Click your shortcut to select all the players on the screen (Win: CTRL + A OR MAC: ⌘ + A). All players should have a green checkmark next to them. <br>
        5. Click the print shortcut (Win: CTRL + P OR MAC: ⌘ + P). <br> 
        6. From the Print Dialog, select 'Web Page' and click 'OK'. <br>
        7. Save your html file somewhere you have access to. <br>
        8. Upload the HTML file here to generate your tactic. <br>
               
        """, unsafe_allow_html=True)

  
# Uploader sits just below the header row
uploaded_file = st.file_uploader(" ", type=["html", "htm"])


if uploaded_file:
    html = uploaded_file.read().decode("utf-8")

    # Parse squad HTML into DataFrame or list of players
    players = parse_squad_html(html)
    
    #st.write("Squad parsed:", players)
    
    
    tg = TacticGenerator(players)
    
    variants = tg.generate_player_variants(players)
    #st.write("Generated player variants:", variants)
    
    best_lineup = None
    best_score = float('-inf')
    best_formation_name = ""
    formation_scores = []

    for formation in formations:
        roles = formation["roles"]
        name = formation["name"]

        lineup = tg.assign_best_players_to_formation(formation, variants)
        
        # Extract midfield roles
        midfield_roles = [p["position"] for p in lineup if p["position"] in [
            "Defensive Midfielder", "Anchor Man", "Half Back", "Regista", "Segundo Volante", "Ball Winning Midfielder",
            "Central Midfielder", "Box-To-Box Midfielder", "Mezzala", "Carrilero", "Deep-Lying Playmaker", "Roaming Playmaker",
            "Attacking Midfielder", "Advanced Playmaker", "Shadow Striker", "Enganche", "Trequartista"
        ]]

        def evaluate_midfield_connectivity(roles):
            has_connector = any(r in ["Central Midfielder", "Box-To-Box Midfielder", "Deep-Lying Playmaker", "Roaming Playmaker"] for r in roles)
            has_deep = any(r in ["Defensive Midfielder", "Anchor Man", "Half Back", "Regista"] for r in roles)
            has_attacking = any(r in ["Attacking Midfielder", "Advanced Playmaker", "Shadow Striker", "Trequartista"] for r in roles)

            if has_connector:
                return "Strong"
            if has_deep and has_attacking:
                return "Weak"
            return "Moderate"

        connectivity = evaluate_midfield_connectivity(midfield_roles)

        if connectivity == "Weak":
            lineup = apply_role_flex(lineup)
            lineup = tg.flex_roles_with_zone_coverage(lineup)

        # Now assign zones based on updated roles
        for player in lineup:
            role = player["position"]
            side = player.get("side", "C")
            player["zones"] = ZONE_MAP.get(role, {}).get(side) or ZONE_MAP.get(role, {}).get("C", [])
                            
        # Score role fit
        role_score = sum(player["score"] for player in lineup if player["score"] > 0)

        # Extract midfield players
        midfield_players = [p for p in lineup if p["position"] in [
            "Box-To-Box Midfielder", "Ball Winning Midfielder", "Central Midfielder",
            "Defensive Midfielder", "Advanced Playmaker", "Attacking Midfielder"
        ]]

        # Generate pairings
        possible_pairings = []
        for i in range(len(midfield_players)):
            for j in range(i + 1, len(midfield_players)):
                possible_pairings.append({
                    "roles": (midfield_players[i]["position"], midfield_players[j]["position"]),
                    "player1": midfield_players[i],
                    "player2": midfield_players[j]
                })

        # Score synergy
        from synergy import calculate_synergy
        synergy_score = 0
        if possible_pairings:
            best_pairing = max(possible_pairings, key=lambda pair: calculate_synergy(
                *pair["roles"],
                pair["player1"]["attributes"],
                pair["player2"]["attributes"]
            ))
            synergy_score = calculate_synergy(
                *best_pairing["roles"],
                best_pairing["player1"]["attributes"],
                best_pairing["player2"]["attributes"]
            )
        
        # Combine scores
        total_score = role_score + synergy_score * 20  # Weight synergy as needed

        # Store formation details for later analysis
        formation_scores.append({
            "name": name,
            "score": total_score,
            "lineup": lineup,
            "roles": roles,
            "formation": formation,
            "synergy_pairing": best_pairing["roles"],
            "synergy_score": synergy_score

        })

        # Track best-performing formation
        if total_score > best_score:
            best_score = total_score
            best_lineup = lineup
            best_formation_name = name
            tactic_data = formation
            
            best_formation_roles = roles
            tg_final = TacticGenerator(players=best_lineup)
            tg_final.player_roles = {
                player["player"]: best_formation_roles[player["name"]]
                for player in best_lineup
                if player["player"] in best_formation_roles
            }



            best_formation = formation  # not just formation["roles"]
            used_players = {p["player"] for p in best_lineup}
            remaining_variants = [v for v in variants if v["name"] not in used_players]
            second_best = tg.assign_best_players_to_formation(best_formation, remaining_variants)

            
            tactic_data["instructions"] = tg_final.generate_instructions(best_formation_name)
            tactic_data["instructions"] = sanity_check_instructions(tactic_data["instructions"])

            mentality = tg_final.suggest_mentality(tactic_data["instructions"])
    


    # Calculate strength percentage relative to best
    for entry in formation_scores:
        entry["relative_strength"] = round((entry["score"] / best_score) * 100, 2)
    
 
    tactic_metadata = {
        "formation": tactic_data.get("formation", best_formation_name),
        "mentality": mentality,
        "instructions": tactic_data.get("instructions", {}),
        "variants": tactic_data.get("variants", []),
        "score": best_score
        }    
    # Match best formation name to find its relative strength
    selected_strength = next(
        (entry["relative_strength"] for entry in formation_scores if entry["name"] == tactic_metadata.get("formation")),
        None
        )
    # Now show it in your UI
    formation_name = tactic_metadata.get("formation", "N/A")
    top_score = tactic_metadata.get("score", 0)

    # Sort formations by score in descending order
    sorted_formations = sorted(formation_scores, key=lambda x: x["score"], reverse=True)

    # Second best tactic
    second_best_entry = sorted_formations[1]
    second_best_lineup = second_best_entry["lineup"]
    second_best_roles = second_best_entry["roles"]
    second_best_name = second_best_entry["name"]
    second_best_score = second_best_entry["score"]

    # Third best tactic — FIXED
    third_best_entry = sorted_formations[2]
    third_best_lineup = third_best_entry["lineup"]
    third_best_roles = third_best_entry["roles"]
    third_best_name = third_best_entry["name"]
    third_best_score = third_best_entry["score"]

    col1, col2 = st.columns([1, 1.2])  # Adjust width ratio as needed

    gap_analysis = analyze_formation_gaps(best_lineup)

    with col1:
        # Formation Summary Card
        st.markdown(f"""
        <div style='border: 2px solid #4CAF50; padding: 10px; border-radius: 10px; background-color: #f9f9f9'>
            <h3 style='color: #2e7d32; margin: 0px 0;'>🥇{formation_name}</h2>
            <p style='margin: 2px 0;'><strong>🧠 Mentality:</strong> {tactic_metadata.get("mentality", "N/A")}</p>
            <p style='margin: 2px 0;'><strong>✅ Top Score:</strong> {top_score:.2f}</p>
            <p style='margin: 2px 0;'><strong>📌 Top Rank:</strong> 1st of {len(formation_scores)} formations</p>
        </div>
        """, unsafe_allow_html=True)

        # Tactical Instructions
        st.markdown("### Tactic Instructions")
        
        display_instruction_block("In Possession", "🟢", tactic_data["instructions"]["in_possession"])
       
        display_instruction_block("In Transition", "🟡", tactic_data["instructions"]["in_transition"])

        display_instruction_block("Out of Possession", "🔴", tactic_data["instructions"]["out_of_possession"])

    with col2:

        # Step 1: Organize player data
        player_data = []
        role_side_tracker = defaultdict(lambda: defaultdict(list))

        for player in best_lineup:
            role = player["position"]
            side = player["side"].upper()
            role_side_tracker[role][side].append(player)

        # Build position lookup with fallback to ROLE_FLEX_MAP
        formation_roles = {
            (r["role"], r["side"].upper()): r["position"]
            for r in tactic_data["roles"]
        }

        position_lookup = {}
        for player in best_lineup:
            role = player["position"]
            side = player["side"].upper()
            key = (role, side)

            if key in formation_roles:
                position_lookup[key] = formation_roles[key]
            elif key in ROLE_FLEX_MAP:
                position_lookup[key] = ROLE_FLEX_MAP[key]
            else:
                position_lookup[key] = (50, 50)  # fallback center

        for role, side_groups in role_side_tracker.items():
            for side, group in side_groups.items():
                for player in group:
                    x, y = position_lookup.get((role, side), (0, 0))
                    name = player["player"]
                    initials = "".join([word[0].upper() for word in name.split() if word])
                    position_codes = ROLE_POSITION_SHORT.get(role, ["?"])
                    position_label = "/".join(position_codes)

                    if len(position_codes) == 1 and not any(s in position_label for s in ["R", "L"]):
                        position_label += f" ({player['side'][0]})"

                    player_data.append({
                        "x": y,
                        "y": x,
                        "Initials": initials,
                        "Full Name": name,
                        "PositionLabel": position_label,
                        "FullPosition": role,
                        "FullDuty": player["duty"],
                        "Duty": player["duty"][0]
                    })

        df = pd.DataFrame(player_data)

        # Step 2: Create pitch layout
        fig = go.Figure()

        # Pitch outline
        fig.add_trace(go.Scatter(x=[0, 0, 100, 100, 0], y=[0, 100, 100, 0, 0],
                                mode='lines', line=dict(color="green", width=2), showlegend=False))

        # Step 3a - Shadow layer
        fig.add_trace(go.Scatter(
            x=df["x"], y=df["y"],
            mode="markers",
            marker=dict(size=52, color="rgba(0, 0, 0, 0.3)"),
            hoverinfo="skip",
            showlegend=False
        ))

        # Step 3b: Player markers
        fig.add_trace(go.Scatter(
            x=df["x"], y=df["y"],
            mode="markers",
            marker=dict(size=44, color="blue"),
            hovertext=df["Full Name"] + "<br>" + df["FullPosition"] + "<br>" + df["FullDuty"],
            hoverinfo="text",
            showlegend=False
        ))

        # Step 3c: Bold initials
        fig.add_trace(go.Scatter(
            x=df["x"], y=df["y"] + 2,
            mode="text",
            text=df["Initials"],
            textposition="middle center",
            textfont=dict(color="white", size=14, family="Arial"),
            showlegend=False
        ))

        # Step 3d: Position label
        fig.add_trace(go.Scatter(
            x=df["x"], y=df["y"] - 1.2,
            mode="text",
            text=df["PositionLabel"],
            textposition="middle center",
            textfont=dict(color="white", size=8, family="Arial"),
            showlegend=False
        ))

        # Step 3e: Duty label
        fig.add_trace(go.Scatter(
            x=df["x"], y=df["y"] - 4,
            mode="text",
            text="(" + df["Duty"] + ")",
            textposition="middle center",
            textfont=dict(color="white", size=8, family="Arial"),
            showlegend=False
        ))

        # Step 4: Layout cleanup
        with open("assets/fpitch.jpg", "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode()

        fig.update_layout(
            images=[dict(
                source="data:image/jpg;base64," + encoded_image,
                xref="x",
                yref="y",
                x=0,
                y=100,
                sizex=100,
                sizey=100,
                sizing="stretch",
                layer="below"
            )],
            xaxis=dict(range=[0, 100], showgrid=False, visible=False),
            yaxis=dict(range=[0, 100], showgrid=False, visible=False),
            plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(t=20, b=20, l=20, r=20)
        )

        # Step 5: Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)
        

    #Analyze formation gaps
    st.markdown("### 🚧 Formation — Gap Analysis")
    for item in gap_analysis:
        with st.expander(f"{item['Area']} — {item['Verdict']}"):
            st.write(f"**Suggested Fix:** {item['Fix']}")

    
    analyzer = SquadAnalyzer(best_lineup)
    variant_generator = VariantGenerator(analyzer)
    tough_variant = variant_generator.generate("ToughOpponent")

    st.markdown("### 🛡️ Tough Opponent Variant")
    st.markdown(f"**Mentality:** {tough_variant['Mentality']}")
    display_instruction_block("In Possession", "🛡️", tough_variant["In Possession"])
    display_instruction_block("In Transition", "🛡️", tough_variant["In Transition"])
    display_instruction_block("Out of Possession", "🛡️", tough_variant["Out of Possession"])

    st.markdown("### ➕ Additional Formations")
    #2ND BEST FORMATION
    tg_second = TacticGenerator(players=second_best_lineup)
    tg_second.player_roles = {
        player["player"]: second_best_roles[player["name"]]
        for player in second_best_lineup
        if player["player"] in second_best_roles
    }
    second_best_entry["instructions"] = sanity_check_instructions(
        tg_second.generate_instructions(second_best_name)
    )
    second_best_entry["mentality"] = tg_second.suggest_mentality(second_best_entry["instructions"])

    with st.expander(f"🥈 Second Best Tactic: {second_best_name} (Score: {second_best_score:.2f})"):
        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.markdown(f"""
            <div style='border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f0f8ff'>
                <h3 style='color: #1565C0; margin: 0px 0;'>{second_best_name}</h3>
                <p><strong>🧠 Mentality:</strong> {second_best_entry['mentality']}</p>
                <p><strong>📊 Score:</strong> {second_best_score:.2f}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Tactic Instructions")
            display_instruction_block("In Possession", "🟢", second_best_entry["instructions"]["in_possession"])
            display_instruction_block("In Transition", "🟡", second_best_entry["instructions"]["in_transition"])
            display_instruction_block("Out of Possession", "🔴", second_best_entry["instructions"]["out_of_possession"])

        with col2:
            render_pitch(second_best_lineup, second_best_roles, formation_name=f"{second_best_name}_2nd")
    
        second_gap_analysis = analyze_formation_gaps(second_best_lineup)
        
        st.markdown("### 🚧 Second Best Formation — Gap Analysis")
        for item in second_gap_analysis:
            with st.expander(f"{item['Area']} — {item['Verdict']}"):
                st.write(f"**Suggested Fix:** {item['Fix']}")


    
    #3rd BEST FORMATION
    tg_third = TacticGenerator(players=third_best_lineup)
    tg_third.player_roles = {
        player["player"]: third_best_roles[player["name"]]
        for player in third_best_lineup
        if player["player"] in third_best_roles
    }
    third_best_entry["instructions"] = sanity_check_instructions(
        tg_third.generate_instructions(third_best_name)
    )
    third_best_entry["mentality"] = tg_third.suggest_mentality(third_best_entry["instructions"])

    with st.expander(f"🥉 Third Best Tactic: {third_best_name} (Score: {third_best_score:.2f})"):
        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.markdown(f"""
            <div style='border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f0f8ff'>
                <h3 style='color: #1565C0; margin: 0px 0;'>{third_best_name}</h3>
                <p><strong>🧠 Mentality:</strong> {third_best_entry['mentality']}</p>
                <p><strong>📊 Score:</strong> {third_best_score:.2f}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Tactic Instructions")
            display_instruction_block("In Possession", "🟢", third_best_entry["instructions"]["in_possession"])
            display_instruction_block("In Transition", "🟡", third_best_entry["instructions"]["in_transition"])
            display_instruction_block("Out of Possession", "🔴", third_best_entry["instructions"]["out_of_possession"])

        with col2:
            render_pitch(third_best_lineup, third_best_roles, formation_name=f"{third_best_name}_3rd")

        third_gap_analysis = analyze_formation_gaps(third_best_lineup)
        st.markdown("### 🚧 Third Best Formation — Gap Analysis")
        for item in third_gap_analysis:
            with st.expander(f"{item['Area']} — {item['Verdict']}"):
                st.write(f"**Suggested Fix:** {item['Fix']}")

    #BEST 11 LINEUP
    st.markdown("### Starting XI")
    clean_lineup = pd.DataFrame(best_lineup).drop(columns=['attributes','zones'])
    clean_lineup = clean_lineup[['player', *[c for c in clean_lineup.columns if c != 'player']]]
    st.dataframe(clean_lineup)  
    
    #SUBSTITUTES
    clean_lineup = pd.DataFrame(second_best).drop(columns=['attributes'])
    clean_lineup = clean_lineup[['player', *[c for c in clean_lineup.columns if c != 'player']]]
    st.markdown("### Substitutes")
    st.dataframe(pd.DataFrame(clean_lineup))
