from pydantic import BaseModel

class Attribute(BaseModel):
    weight_class: str
    run_speed: str
    air_speed: str


class CompetitiveTool(BaseModel):
    neutral_tools: list[str]
    out_of_shield_options: list[str]
    kill_confirms: list[str]


class AdvantageState(BaseModel):
    juggling: str
    ledge_trapping: str
    tech_chasing: str
    edge_guarding: str


class DisadvantageStage(BaseModel):
    landing: str
    escape_options: str
    out_of_shield: str
    recovery: str


class StagePreference(BaseModel):
    best_stages: list[str]
    worst_stages: list[str]


class MatchupTendencie(BaseModel):
    strong_against: list[str]
    weak_against: list[str]


class Character(BaseModel):
    fighter_number: int
    name: str
    archetype: str
    tier: str
    difficulty: str
    secondary_required: bool
    signature_moves: list[str]

    attributes: Attribute
    competitive_tools: CompetitiveTool
    advantage_state: AdvantageState
    disadvantage_state: DisadvantageStage
    stage_preferences: StagePreference
    matchup_tendencies: MatchupTendencie