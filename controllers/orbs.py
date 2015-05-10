
import models.orbs
import random


def get_random_orb():
    rand = random.randint(1,6)

    if rand == 1:
        return models.orbs.Fire()
    elif rand == 2:
        return models.orbs.Water()
    elif rand == 3:
        return models.orbs.Earth()
    elif rand == 4:
        return models.orbs.Light()
    elif rand == 5:
        return models.orbs.Dark()
    elif rand == 6:
        return models.orbs.Heart()
