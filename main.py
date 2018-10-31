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

trust_matrix = [
    [.6, .2, .2],
    [.2, .6, .2],
    [.2, .2, .6],
]

trust_matrix_well_one = [
    [.8, .1, .1],
    [.4, .5, .1],
    [.4, .1, .5],
]

trust_matrix_well_two = [
    [.5, .4, .1],
    [.1, .8, .1],
    [.1, .4, .5],
]

trust_matrix_well_three = [
    [.5, .1, .4],
    [.1, .5, .4],
    [.1, .1, .8],
]

wells = [
    [],
    [],
    []
]


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
        self.trust = trust_matrix
        pass

    def set_trust(self):
        maxi = self.get_max()
        if maxi == -1:
            self.trust = trust_matrix
        elif maxi == 0:
            self.trust = trust_matrix_well_one
        elif maxi == 1:
            self.trust = trust_matrix_well_two
        else:
            self.trust = trust_matrix_well_three

    def get_max(self):
        maxi = 0
        if self.probabilities[1] > self.probabilities[maxi]:
            maxi = 1
        if self.probabilities[2] > self.probabilities[maxi]:
            maxi = 2
        return maxi


def generate_water(water_sources, water_type):
    if water_type == WaterType.COUNTING:
        if water_sources.source_with_water == -1:
            water_sources[0].has_water = True
            water_sources.source_with_water = 0
        else:
            water_sources.water[water_sources.source_with_water] = False
            water_sources.source_with_water = (water_sources.source_with_water + 1) % len(water_sources.water)
            water_sources.water[water_sources.source_with_water] = True
    elif water_type == WaterType.RANDOM:
        if water_sources.source_with_water != -1:
            water_sources.water[water_sources.source_with_water] = False
        water_sources.source_with_water = randint(0, len(water_sources.water) - 1)
        water_sources.water[water_sources.source_with_water] = True
    elif water_type == WaterType.SET:
        water_sources.source_with_water = 0
        water_sources.water[water_sources.source_with_water] = True
    else:
        print("Unknown Water Type")


def information_cascade(agents):
    results = dict()
    make_action(agents[0])
    agents_gone = [agents[0]]
    results[0] = agents[0].action
    for agent in range(1, len(agents)):
        for agent_gone in range(0, len(agents_gone)):
            past_action = agents_gone[agent_gone].action
            agnt = agents[agent]
           # agnt.set_trust()
            #if agent_gone == 0:
            #    print(str(agnt.trust))
            agnt.probabilities[0] = agnt.trust[past_action][0]*agnt.probabilities[0]
            agnt.probabilities[1] = agnt.trust[past_action][1]*agnt.probabilities[1]
            agnt.probabilities[2] = agnt.trust[past_action][2]*agnt.probabilities[2]
        make_action(agents[agent])
        agents_gone.append(agents[agent])
        results[agent] = agents[agent].action
    return results


def make_action(agent):
    best_action = 0
    if agent.probabilities[1] > agent.probabilities[best_action]:
        best_action = 1
    if agent.probabilities[2] > agent.probabilities[best_action]:
        best_action = 2
    agent.action = best_action
    if best_action == 0:
        wells[0].append(agent)
    elif best_action == 1:
        wells[1].append(agent)
    else:
        wells[2].append(agent)


def set_probs(correct_source, agent, n1, n2, n3):
    if correct_source == 0:
        agent.probabilities = [n1, n2, n3]
    elif correct_source == 1:
        agent.probabilities = [n2, n1, n3]
    else:
        agent.probabilities = [n2, n3, n1]


def generate_probabilities(correct_source, information_type, agent):
    n1 = np.random.randint(100)
    n2 = np.random.randint(100)
    n3 = np.random.randint(100)
    d = n1 + n2 + n3
    n1 = n1 / d
    n2 = n2 / d
    n3 = n3 / d
    if information_type.GOOD_INFORMATION:
        if np.random.randint(1, 101) % 10 < 8:
           # print("got here")
            if n1 > n2:
                if n1 > n3:
                    set_probs(correct_source, agent, n1, n2, n3)
                else:
                    set_probs(correct_source, agent, n3, n1, n2)
            elif n2 > n3:
                set_probs(correct_source, agent, n2, n3, n1)
            else:
                set_probs(correct_source, agent, n3, n2, n1)
        else:
            agent.probabilities = [n1, n2, n3]
    elif information_type.BAD_INFORMATION:
        if np.random.randint(1, 101) % 10 < 8:
            if n1 < n2:
                if n1 < n3:
                    set_probs(correct_source, agent, n1, n2, n3)
                else:
                    set_probs(correct_source, agent, n3, n2, n1)
            elif n2 < n3:
                set_probs(correct_source, agent, n2, n3, n1)
            else:
                set_probs(correct_source, agent, n3, n2, n1)
        else:
            agent.probabilities = [n1, n2, n3]
    else:
        agent.probabilities = [n1, n2, n3]


# Returns a list that contains a percentage of people who got water for each day
def run_simulation(information_type,
                   water_type,
                   number_of_agents):
    water_sources = WaterSources()
    agents = []
    for each in range(number_of_agents):
        agents.append(Agent())
    # First day
    generate_water(water_sources, water_type)
    # initial agent decision
    print("water source is at: " + str(water_sources.source_with_water))
    generate_water(water_sources, water_type)
    for agent in range(0, number_of_agents):
        generate_probabilities(water_sources.source_with_water, information_type, agents[agent])
        #print("agent: " + str(agent) + "\nprobabilities: " + str(agents[agent].probabilities))
    return water_sources.source_with_water, information_cascade(agents)


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


correct_answer, sim_results = run_simulation(StartingInformation.BAD_INFORMATION, WaterType.RANDOM, 100)
print(str(sim_results))
print("well Zero: " + str(len(wells[0])) + "\nWell One: " + str(len(wells[1])) + "\nWell Two: " + str(len(wells[2])))
#plot_data(sim_results)
#sim_results = run_simulation(StartingInformation.OKAY_INFORMATION, WaterType.RANDOM, 30, 10)
#plot_data(sim_results)
#sim_results = run_simulation(StartingInformation.BAD_INFORMATION, WaterType.RANDOM, 30, 10)
#plot_data(sim_results)

#input("Press Enter to continue...")
