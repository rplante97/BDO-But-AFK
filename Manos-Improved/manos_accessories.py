from simulator import simulator
from random import choices


class manos_accessories(simulator):

    tiers = {'T0': 0, 'PRI': 1, 'DUO': 2, 'TRI': 3, 'TET': 4, 'PEN': 5}

    success_rates = [0.75, 0.45, 0.30, 0.15, 0.05]
    gem_cost = [100, 110, 130, 160, 200]
    gem_price = 800000
    dura_cost = [1, 1, 1, 1, 1]
    dura_price = 210000000

    def enhance(self, tier):
        if choices([True, False], [self.success_rates[tier], 1 - self.success_rates[tier]])[0]:
            return tier + 1
        else:
            return self.tiers['T0']
