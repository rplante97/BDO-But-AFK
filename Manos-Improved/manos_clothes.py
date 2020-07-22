from simulator import simulator
from random import choices


class manos_clothes(simulator):

    tiers = {
        'T0': 0,
        'T1': 1,
        'T2': 2,
        'T3': 3,
        'T4': 4,
        'T5': 5,
        'T6': 6,
        'T7': 7,
        'T8': 8,
        'T9': 9,
        'T10': 10,
        'T11': 11,
        'T12': 12,
        'T13': 13,
        'T14': 14,
        'T15': 15,
        'PRI': 16,
        'DUO': 17,
        'TRI': 18,
        'TET': 19,
        'PEN': 20
    }

    success_rates = [1, 1, 1, 1, 1, 0.9, 0.8, 0.7, 0.6, 0.5,
                     0.4, 0.3, 0.2, 0.15, 0.1, 0.30, 0.25, 0.2, 0.15, 0.06]

    gem_cost = [1, 1, 1, 1, 1, 2, 2, 2,
                3, 3, 3, 4, 4, 5, 5, 10, 10, 10, 10, 10]

    dura_cost = [5, 5, 5, 5, 5, 5, 5, 5,
                 5, 5, 5, 5, 5, 5, 5, 10, 10, 10, 10, 10]

    dura_price = 1800000
    gem_price = 800000

    def enhance(self, tier):
        if choices([True, False], [self.success_rates[tier], 1 - self.success_rates[tier]])[0]:
            return tier + 1
        elif tier <= self.tiers['PRI']:
            return tier
        else:
            return tier - 1
