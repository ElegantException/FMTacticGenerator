# parse_squad.html.py
import pandas as pd
from bs4 import BeautifulSoup

# Short-to-full attribute name mapping for FM24 compatibility
ATTRIBUTE_NAME_MAP = {
    "1v1": "1v1",
    "Acc": "Acceleration",
    "Aer": "Aerial Ability",
    "Agg": "Aggression",
    "Agi": "Agility",
    "Ant": "Anticipation",
    "Bal": "Balance",
    "Bra": "Bravery",
    "Cmd": "Command of Area",
    "Cnt": "Concentration",
    "Cmp": "Composure",
    "Com": "Communication",
    "Cor": "Corners",
    "Cro": "Crossing",
    "Dec": "Decisions",
    "Det": "Determination",
    "Dri": "Dribbling",
    "Ecc": "Eccentricity",
    "Fin": "Finishing",
    "Fir": "First Touch",
    "Fre": "Free Kick Taking",
    "Fla": "Flair",
    "Han": "Handling",
    "Hea": "Heading",
    "Jum": "Jumping Reach",
    "Kic": "Kicking",
    "L Th": "Long Throws",
    "Ldr": "Leadership",
    "Lon": "Long Shots",
    "Nat": "Natural Fitness",
    "Mar": "Marking",
    "OtB": "Off The Ball",
    "Pac": "Pace",
    "Pas": "Passing",
    "Pen": "Penalty Taking",
    "Pos": "Positioning",
    "Pun": "Punching",
    "Ref": "Reflexes",
    "Sta": "Stamina",
    "Str": "Strength",
    "Tck": "Tackling",
    "Tea": "Teamwork",
    "Tec": "Technique",
    "Thr": "Throwing",
    "TRO": "Throwing",
    "Vis": "Vision",
    "Wor": "Work Rate"
}

def parse_squad_html(html_str):
    soup = BeautifulSoup(html_str, "html.parser")
    table = soup.find("table")
    if not table:
        raise ValueError("No table found in HTML")

    # Extract headers
    header_row = table.find("tr")
    headers = [th.get_text(strip=True) for th in header_row.find_all("th")]

    # Extract data rows
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = tr.find_all(["td", "th"])
        if len(cells) != len(headers):
            continue
        row = [cell.get_text(strip=True) for cell in cells]
        rows.append(row)

    df = pd.DataFrame(rows, columns=headers)

    # Standardize position column
    if 'Position' in df.columns:
        df.rename(columns={'Position': 'Positions'}, inplace=True)
    elif 'Position(s)' in df.columns:
        df.rename(columns={'Position(s)': 'Positions'}, inplace=True)
    else:
        df['Positions'] = None

    # Parse positions into list
    df['Positions'] = df['Positions'].apply(lambda x: [p.strip() for p in x.split(',')] if pd.notna(x) else [])

    # Convert raw short-named columns to full attribute names
    for short, full in ATTRIBUTE_NAME_MAP.items():
        if short in df.columns:
            try:
                df[full] = pd.to_numeric(df[short], errors='coerce').fillna(0).astype(int)
            except Exception as e:
                print(f"Could not convert {short} → {full}: {e}")

    # ✅ Drop this check BEFORE building the player list
    expected_attributes = list(ATTRIBUTE_NAME_MAP.values())
    missing_cols = [col for col in expected_attributes if col not in df.columns]
    if missing_cols:
        print("🧯 Missing attributes:", missing_cols)

    # 🛠️ Now your normalization loop
    players = []
    for _, row in df.iterrows():
        attributes = {
            full_name: row.get(full_name, 0)
            for full_name in ATTRIBUTE_NAME_MAP.values()
        }

        if not any(attributes.values()):
            print(f"⚠️ Player missing attribute datafff: {row.get('Name', 'Unknown')}")

        player = {
            'Name': row.get('Name', ''),
            'Positions': row['Positions'],  # Keep full list
            'attributes': attributes
        }
        players.append(player)

    return players