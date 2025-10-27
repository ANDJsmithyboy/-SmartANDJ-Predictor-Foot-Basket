from pydantic import BaseModel, Field
from typing import Optional


class FootballPredictionRequest(BaseModel):
    home_team: str = Field(..., description="Nom de l'équipe à domicile")
    away_team: str = Field(..., description="Nom de l'équipe à l'extérieur")
    match_date: Optional[str] = Field(None, description="Date du match (YYYY-MM-DD)")


class FootballPredictionResponse(BaseModel):
    home_win_prob: float
    draw_prob: float
    away_win_prob: float
    recommendation: str


class BasketballPredictionRequest(BaseModel):
    home_team: str
    away_team: str
    match_date: Optional[str] = None


class BasketballPredictionResponse(BaseModel):
    home_win_prob: float
    away_win_prob: float
    recommendation: str

