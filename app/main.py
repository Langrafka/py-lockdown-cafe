from typing import List, Dict
from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError

def go_to_cafe(friends: List[Dict], cafe: Cafe) -> str:
    masks_to_buy = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # Якщо хоча б у одного друга проблема з вакциною
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            # Підрахунок скільки не має масок
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
