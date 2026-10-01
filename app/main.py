import datetime
import errors
from cafe import Cafe


def go_to_cafe(friends: list, cafe: object) -> str:
    masks_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except errors.NotWearingMaskError:
            masks_to_buy += 1
        except errors.VaccineError:
            return "All friends should be vaccinated"
    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    return f"Friends can go to {cafe.name}"
