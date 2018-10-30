from random import randint
from enum import Enum
import numpy as np
import matplotlib.pyplot as plt


class StartingInformation(Enum):
    GOOD_INFORMATION = 1
    OKAY_INFORMATION = 2
    BAD_INFORMATION = 3


class WaterType(Enum):
    RANDOM = 1
    COUNTING = 2
    SET = 3


class DecisionTypes(Enum):
    BAYES = 1
    INFORMATION_CASCADE = 2


class UtilityType(Enum):
    pass


class WaterSource:
    def __init__(self):
        self.has_water = False


class WaterSources:
    def __init__(self):
        self.water = [WaterSource(), WaterSource(), WaterSource()]
        self.source_with_water = -1


class Agent:
    def __init__(self):
        self.action = -1
        self.probabilities = [-0.0, -0.0, -0.0]
        pass

    def bayes_rule(self):
        pass

    def maximum_expected_utility(self):
        pass

    def maximum_posteriori(self):
        pass

    def run_with_prior(self):
        pass

    def run_with_max_expected_utility(self):
        pass

    def run_with_multiple_utilities(self):
        pass


def generate_water(water_sources, water_type):
    if water_type == WaterType.COUNTING:
        if water_sources.source_with_water == -1:
            water_sources[0].has_water = True
            water_sources.source_with_water = 0
        else:
            water_sources[water_sources.source_with_water] = False
            water_sources.source_with_water = (water_sources.source_with_water + 1) % len(water_sources.water)
            water_sources[water_sources.source_with_water] = True
    elif water_type == WaterType.RANDOM:
        if water_sources.source_with_water != -1:
            water_sources[water_sources.source_with_water] = False
        water_sources.source_with_water = randint(0, len(water_sources.water) - 1)
        water_sources[water_sources.source_with_water] = True
    elif water_type == WaterType.SET:
        water_sources.source_with_water = 0
        water_sources[water_sources.source_with_water] = True
    else:
        print("Unknown Water Type")


def generate_probabilities(water_sources, information_type, agent):
    if information_type is StartingInformation.GOOD_INFORMATION:
        for water in range(len(water_sources.water)):
            if water == water_sources.source_with_water:
                agent.probabilities[water] = 1.0
            else:
                agent.probabilities[water] = 0.0
    elif information_type is StartingInformation.OKAY_INFORMATION:
        for water in range(len(water_sources.water)):
            agent.probabilities[water] = 0.33
    elif information_type is StartingInformation.BAD_INFORMATION:
        for water in range(len(water_sources.water)):
            if water == water_sources.source_with_water:
                agent.probabilities[water] = 0.0
            else:
                agent.probabilities[water] = 0.5
    else:
        print("Information error")


# Returns a list that contains a percentage of people who got water for each day
def run_simulation(information_type,
                   water_type,
                   number_of_days,
                   number_of_agents):
    water_sources = WaterSources()
    agents = []
    for each in range(number_of_agents):
        agents.append(Agent())
    # First day
    generate_water(water_sources, water_type)
    generate_probabilities(water_sources, information_type, agents[0])
    # initial agent decision
    results = []
    for day in range(1, number_of_days):
        generate_water(water_sources, water_type)
        for agent in range(0, number_of_agents):
            generate_probabilities(water_sources, information_type, agents[agent])
            # agent decision
    return results


def plot_data(sim_data):
    days = []
    for x in range(1, 31):
        days.append(x)

    plt.bar(sim_results, days, align='center', alpha=0.5)
    plt.xticks(days)
    plt.xlabel('Days')
    plt.ylabel('Number of people that got water')
    plt.title('Information Cascades')
    plt.show()


sim_results = run_simulation(StartingInformation.GOOD_INFORMATION, WaterType.RANDOM, 30, 1000)
plot_data(sim_results)
sim_results = run_simulation(StartingInformation.OKAY_INFORMATION, WaterType.RANDOM, 30, 1000)
plot_data(sim_results)
sim_results = run_simulation(StartingInformation.BAD_INFORMATION, WaterType.RANDOM, 30, 1000)
plot_data(sim_results)
