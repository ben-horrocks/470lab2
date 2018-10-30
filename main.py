

class WaterSource:
    def __init__(self, p):
        self.has_water = False
        self.p = p

    def it_has_water(self):
        self.has_water = True

    def get_water_state(self):
        return self.has_water

    def get_water_probability(self):
        return self.p


class Agent:
    def __init__(self):
        pass

    def run_with_prior(self):
        pass

    def run_with_max_expected_utility(self):
        pass

    def run_with_multiple_utilities(self):
        pass
