import json
import random
from fastapi import FastAPI, Path, HTTPException
from schemas import Character

def load_characters(file_path: str = "data.json"):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return {k: v for k, v in enumerate(data, start=1)}


characters_list = load_characters()

app = FastAPI(
    title="Super Smash Bros. Ultimate API",
    version="1.0.0",
    openapi_prefix="/api/v1"
)

def get_character_or_404(char_id: int):
    character = characters_list.get(char_id)

    if not character:
        raise HTTPException(
            status_code=404,
            detail="Character does not exist"
        )

    return Character(**character)

@app.get("/total_characters")
def get_total_characters() -> dict:
    return {"total_characters": len(characters_list)}

@app.get("/all_characters")
def get_all_characters() -> list[Character]:
    return [
        Character(**char)
        for char in characters_list.values()
    ]

@app.get("/character/{id}")
def get_character_by_id(id: int = Path(ge=1)) -> Character:
    return get_character_or_404(id)

@app.get("/character/search/{name}")
def search_character(name: str):
    results = []

    for char in characters_list.values():
        if name.lower() in char["name"].lower():
            results.append(char)

    return results

@app.get("/characters/filter")
def filter_characters(
    tier: str | None = None,
    archetype: str | None = None,
    difficulty: str | None = None
):
    results = []

    for char in characters_list.values():
        if tier and char["tier"] != tier:
            continue

        if archetype and archetype not in char["archetype"]:
            continue

        if difficulty and char["difficulty"] != difficulty:
            continue

        results.append(char)

    return results

@app.get("/random_character")
def random_character():
    char = random.choice(list(characters_list.values()))
    return char

@app.get("/all_archetypes")
def get_all_archetypes() -> list[str]:
    archetypes = set()

    for character in characters_list.values():
        for archetype in character["archetype"].split("/"):
            archetypes.add(archetype.replace(" ", ""))

    return sorted(archetypes)

@app.get("/characters/archetype/{archetype}")
def filter_by_archetype(archetype: str):
    return [
        char
        for char in characters_list.values()
        if archetype.lower() in char["archetype"].lower()
    ]
    
@app.get("/characters/tier/{tier}")
def filter_by_tier(tier: str):
    return [
        char
        for char in characters_list.values()
        if char["tier"].lower() == tier.lower()
    ]
    
@app.get("/matchup/{id}")
def get_matchups(id: int):
    char = get_character_or_404(id)

    return {
        "character": char.name,
        "strong_against": char.matchup_tendencies.strong_against,
        "weak_against": char.matchup_tendencies.weak_against
    }
    
@app.get("/difficulty/{id}")
def get_difficulty(id: int):
    char = get_character_or_404(id)

    return {
        "name": char.name,
        "difficulty": char.difficulty,
        "secondary_required": char.secondary_required
    }
    
@app.get("/tier-list")
def tier_list():
    tiers = {}

    for char in characters_list.values():
        tier = char["tier"]

        if tier not in tiers:
            tiers[tier] = []

        tiers[tier].append(char["name"])

    order = ["S+", "S", "S-", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E+", "E", "E-"]

    return {
        t: tiers[t]
        for t in order
        if t in tiers
    }

@app.get("/compare/{id1}/{id2}")
def compare(id1: int, id2: int):
    c1 = get_character_or_404(id1)
    c2 = get_character_or_404(id2)

    def score(char, opponent):
        s = 0

        # tier advantage
        tier = {"S": 3, "A": 2, "B": 1, "C": 0}
        s += tier.get(char.tier.upper(), 0)

        # matchup advantage
        if opponent.name in char.matchup_tendencies.strong_against:
            s += 2
        if opponent.name in char.matchup_tendencies.weak_against:
            s -= 1

        return s

    s1 = score(c1, c2)
    s2 = score(c2, c1)

    return {
        "matchup": {
            c1.name: s1,
            c2.name: s2
        },
        "winner": c1.name if s1 > s2 else c2.name
    }
