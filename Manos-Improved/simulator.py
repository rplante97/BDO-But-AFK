import numpy as np
from multiprocessing import Pool, cpu_count


class simulator():

    tiers = {}
    gem_cost = []
    gem_price = 0
    dura_cost = []
    dura_price = 0

    NB_SIM = 10000
    data = []

    def __init__(self):
        if not len(self.tiers):
            raise Exception('Lenght of tier list is 0')
        if len(self.gem_cost) != len(self.tiers) - 1:
            raise Exception('Lenght of gem_cost should be lenght of tiers - 1')
        if self.gem_price == 0:
            raise Exception('Nothing is free not even gems')
        if len(self.dura_cost) != len(self.tiers) - 1:
            raise Exception('Lenght of dura_cost should be lenght of tiers - 1')
        if self.dura_price == 0:
            raise Exception('Nothing is free not even durability')

    def enhance(self, tier):
        """override me"""
        return tier

    def simulate(self, base, goal, limit=0):
        nb = [0] * len(self.tiers)
        fails = [0] * len(self.tiers)
        total = 0
        current = base
        while current != goal and (total < limit or limit == 0):
            nb[current] += 1
            total += 1
            new = self.enhance(current)
            if new <= current:
                fails[current] += 1
            current = new
        return {
            'total_attempts': total,
            'attempts': nb,
            'failed_attempts': fails,
            'final_tier': current,
            'total_cost': np.sum(
                [nb[tier] * self.gem_cost[tier] * self.gem_price + fails[tier] * self.dura_cost[tier] * self.dura_price
                 for tier in range(len(self.tiers)-1)]
            )
        }

    def tiers_by_idx(self, idx):
        for k, v in self.tiers.items():
            if idx == v:
                return k
        raise Exception(f'Index: {idx} not found in tier list: {self.tiers}')

    def run(self, base, goal, limit=0):
        nb_batch = cpu_count() - 1
        with Pool(processes=nb_batch) as pool:
            self.data = pool.starmap(self.simulate, list(
                zip([base], [goal], [limit])) * self.NB_SIM, nb_batch)

    def print_result(self, percentiles=[0, 25, 50, 75, 100]):
        ptotal = np.percentile([simulation['total_attempts']
                                for simulation in self.data], percentiles)
        print(f'#Total attempts:')
        for i, total in enumerate(ptotal):
            print(f'\t{percentiles[i]}% < {int(total)}')

        pattempts = [np.percentile([simulation['attempts'][tier]
                                    for simulation in self.data], percentiles) for tier in range(len(self.tiers))]
        print('#Attempts by tier:')
        for t, patt in enumerate(pattempts[:-1]):
            if any([int(att) != 0 for att in patt]):
                print(
                    f"\t{self.tiers_by_idx(t)}->{self.tiers_by_idx(t + 1)}:\t{[f'{percentiles[p]}% < {int(att)}' for p, att in enumerate(patt)]}")

        pcost = np.percentile([simulation['total_cost']
                               for simulation in self.data], percentiles)
        print('#Cost:')
        for i, cost in enumerate(pcost):
            print(f'\t{percentiles[i]}% < {int(cost):,}')

        pfinal = np.percentile([simulation['final_tier']
                                for simulation in self.data], percentiles)
        print('#Final Tier:')
        for i, final in enumerate(pfinal):
            print(f'\t{percentiles[i]}% < {self.tiers_by_idx(int(final))}')
