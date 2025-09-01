from fastapi import APIRouter
from ..models.schemas import (
    FootballPredictionRequest,
    FootballPredictionResponse,
    BasketballPredictionRequest,
    BasketballPredictionResponse,
)
import hashlib
import random


router = APIRouter()


def _deterministic_rng_seed(*parts: str) -> int:
    payload = "|".join(parts)
    digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return int(digest[:16], 16)


@router.post("/football", response_model=FootballPredictionResponse)
def predict_football(payload: FootballPredictionRequest) -> FootballPredictionResponse:
    seed = _deterministic_rng_seed(payload.home_team, payload.away_team, payload.match_date or "")
    rng = random.Random(seed)

    # Simple mock probabilities that sum to 1.0
    home = rng.uniform(0.3, 0.6)
    draw = rng.uniform(0.1, 0.3)
    away = max(0.0, 1.0 - home - draw)

    # Normalize to be safe
    total = home + draw + away
    home /= total
    draw /= total
    away /= total

    recommendation = "home_win" if home >= max(draw, away) else ("away_win" if away >= max(home, draw) else "draw")

    return FootballPredictionResponse(
        home_win_prob=round(home, 4),
        draw_prob=round(draw, 4),
        away_win_prob=round(away, 4),
        recommendation=recommendation,
    )


@router.post("/basketball", response_model=BasketballPredictionResponse)
def predict_basketball(payload: BasketballPredictionRequest) -> BasketballPredictionResponse:
    seed = _deterministic_rng_seed(payload.home_team, payload.away_team, payload.match_date or "")
    rng = random.Random(seed)

    home = rng.uniform(0.4, 0.7)
    away = 1.0 - home
    recommendation = "home_win" if home >= away else "away_win"

    return BasketballPredictionResponse(
        home_win_prob=round(home, 4),
        away_win_prob=round(away, 4),
        recommendation=recommendation,
    )

