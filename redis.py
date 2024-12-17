"""
guild:
- uuid, str
- guild id, int
- channel id, int
- users, [str (uuid)
- games, [str (uuid)]

user:
- uuid, str
- steam id, int
- authentication code, str
- game ids, [str (uuid)]
- last match token, str

game:
- uuid, str
- match token: str
- match id: str
- outcome id: str
- token id: str
- demo name: str
- steam ids, [int]
"""

from redis_om import (
    JsonModel,
    Field,
)


class Guild(JsonModel):
    guild_id: int = Field(index=True)
    channel_id: int
    users: list[str] = Field(index=True)
    processed_games: list[str]


class User(JsonModel):
    steam_id: int = Field(index=True)
    auth_code: str
    game_ids: list[str]
    last_match_token: str


class Game(JsonModel):
    match_token: str = Field(index=True)
    match_id: str = Field(index=True)
    outcome_id: str
    token_id: str
    demo_name: str
    steam_ids: list[int]
