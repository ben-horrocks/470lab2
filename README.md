# 470lab2
Information Cascades in the Slums of Cape Town


This lab can be done in groups of 2 or 3. You will submit a written report of the experiments (computer simulations) that you did and the things you found interesting. It won't be grading for grammar and style, but it should be well organized so that a reader can follow what you are saying. Your goal is to describe the models you created and the cool things you observed.

Note: The questions and prompts posed are to help you explore the problem space and reason about what approaches you can use to make an intelligent choice given the information you have.  You don’t have to necessarily include answers to these questions in your report. In your report, you should consider including the following:

Create some sort of program to run a lot of random computer simulations that have agents with good, not so good, and bad private information, who make choices based on Bayes equation (with and without utility)

Use Bayes rule to find a maximum a posteriori estimate and/or maximum expected utility

Use the concept of information cascades to adjust your implementation of Bayes rule to account for partial information that is obtained from observations of other agents

Understand and explain how Bayes rule and information cascades affect populations when they have good private information, not so good private information, and bad private information.

Of course, if you end up seeing something more interesting to study (such as -- how do you stop negative information cascades), you can certainly do so (and could allow you to drop some aspects of written up in this report).

Submit one report for each group. Make sure that each group has the names of all group members.

Read this newspaper article about the plight of the very poor in Cape Town, South Africa. The purpose of this lab is to discover ways that an information cascade model might be used to guide those seeking water to reliable sources.

This lab will integrate the following concepts:

Maximum expected utility

Maximum a posteriori estimate

Bayes rule

Information cascades

Problem Model

Suppose that there are three sources of water within walking distance for the people who live in a slum. Because of the water crisis, only one of the three sources of water works on any given day.

Prompt: There are three states of the world. What are they?

Each morning, each household in the slum must send a slum member to fetch water from one of the water sources. Assume for model simplicity that they must choose between one of the three water sources.

Prompt: There are three actions available to each household. What are they?

Every household has an estimate for which water source is working on that day. For model simplicity, assume that this is represented as a probability over which water source has water that day. This is the prior probability over the states.

Each household has different information, which means that each household has a different prior probability. The differences in prior probabilities are known in the research literature as private information, meaning information that is known by individual agents but not known to all households.

We will treat each household as a decision-making agent.

Problem 1

What happens when each agent chooses to go to the water source that has the highest prior probability? Try some different types of prior probabilities for each agent. Let some be accurate (most agents are correct), some be mixed (some agents are correct and others are incorrect), and some be poor (most agents are incorrect). How often do agents obtain water?

Information Cascades

Suppose that agents make decisions sequentially, meaning that the first agent must make a decision by himself or herself using only his or her prior probability. The second agent gets to observe where the first agent goes (but not whether the first agent returns with water), and can use this observation to update her or his prior probability.

Prompt: What is the likelihood that agent 2 observes agent 1 going to water source i when the actual water source is at location j?

As you consider this question, consider the assumption that each person probabilistically receives correct information about the state of the world.  Let q denote the probability that the private information signal they receive corresponds to the correct state of the world, and with probability 1-q, each person receives a private signal that leads them to believe in an incorrect belief about the world’s state.  The Wikipedia page on information cascades gives the likelihood probabilities for a two-state scenario (in the section “Quantitative description.”  You’ll need to extend this to a three-state case.

Note: You may want to play around with the probability q, and consider that different agents might estimate q differently to further explore the space.

Prompt: What is the posterior probability that the water source is at location j when agent 2 observes agent 1 going to water source i?

Prompt: Notice that except for agent 1, all other agents make their choices using the MAP (maximum a posteriori) estimate, given by arg max p(state | observation).

The third agent gets to observe the first and second agent. The third agent thus uses two observations to update its probability. Assume that agent 3 updates his or her posterior probability first by using Bayes Rule with input about agent 1's choice, and then again updates his or her posterior probability by using Bayes Rule again with input about agent 2's choice.  (Note: this means that the posterior probability turns into the prior probability in the next computation.)

Prompt: What is the posterior probability for agent 3 after sequentially updating his or her probability using an observation of agent 1 and agent 2?

Agent 4 gets to observe agent 1, 2, and 3. And so on.

An information cascade occurs when the information from previous agents shapes the decision made by subsequent agents.

Problem 2

Suppose that the first few agents have accurate private information. What happens to the decisions of subsequent agents? How often do agents find the correct water source? Is this better or worse than the results from the first problem? Why?

Suppose that the first few agent have inaccurate private information. What happens to the decisions of subsequent agents? How often do agents find the correct water source? Is this better or worse than the results from the first problem? Why?

Try different numbers of agents, some different likelihood models, and different qualities of prior information. Report interesting results.

Maximum Expected Utility

In the first problem, agents make decisions using an estimate of which state is most probable given their prior information. In the second information, the first agent makes his or her decision using an estimate of which state is most probable given her or his prior information, but all subsequent agents make their decisions using MAP estimates.

Suppose that an agent has a utility for each consequence that results for each state-action pair. For example, suppose that one of the water sources is far away, so if the agent chooses to go to that location and there is no water, the agent won't have time to do other tasks in the day like forage for food or seek day labor. As another example, suppose that one of the water sources requires walking through a dangerous part of the slum.

Problem 3

Repeat problem 2, but suppose that each agent has utilities. Suppose for simplicity that all agents have the same or very similar utilities. Assume that agent 1 makes his or choice using maximum expected utility, where the expectation is taken with respect to agent 1's prior probability.

Agent 2 uses the observation of agent 1 to update his or her posterior probability, and then makes his or her decision using maximum expected utility where the expectation is take with respect to agent 2's posterior probability. And so on.

When agents use maximum expected utility instead of MAP estimates, do you see different patterns of choices of the agents? How often do agents choose the correct water source? How would you modify the likelihood, p(o|s), if you knew that other agents were using maximum expected utility instead of MAP estimates?

