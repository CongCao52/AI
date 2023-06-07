# Include your imports here, if any are used.

import collections
#import util
# 1. Value Iteration
class ValueIterationAgent:
    """Implement Value Iteration Agent using Bellman Equations."""

    def __init__(self, game, discount):
        """Store game object and discount value into the agent object,
        initialize values if needed.
        """
        # TODO
        self.game = game
        self.discount = discount
        self.states = game.states
        self.values = {state: 0 for state in self.states}
        
    def get_value(self, state):
        """Return value V*(s) correspond to state.
        State values should be stored directly for quick retrieval.
        """
        return self.values.get(state,0)  # TODO
    def get_q_value(self, state, action):
        """Return Q*(s,a) correspond to state and action.
        Q-state values should be computed using Bellman equation:
        Q*(s,a) = Σ_s' T(s,a,s') [R(s,a,s') + γ V*(s')]
        """
        q_value = 0
        for nextState, prob in self.game.get_transitions(state, action).items():
            q_value = q_value + prob * (self.game.get_reward(state, action, nextState) + self.discount * self.get_value(nextState))

        return q_value

    def get_best_policy(self, state):
        """Return policy π*(s) correspond to state.
        Policy should be extracted from Q-state values using policy extraction:
        π*(s) = argmax_a Q*(s,a)
        """
        max_action = None 
        max_value = -99999
        for action in self.game.get_actions(state):
            current_q = self.get_q_value(state, action)
            if current_q > max_value:
                max_value = current_q
                max_action = action 
        return max_action  # TODO

    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        # TODO
        self.values = {state: self.get_q_value(state, self.get_best_policy(state)) for state in self.states}

# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function or
    override ValueIterationAgent's methods, you can add them as well.
    """

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until |V_{k+1}(s) - V_k(s)| < ε
        """
        epsilon = 1e-6
        my_policy = {state: self.get_best_policy(state) for state in self.states}
        while True:
            thevalues  = {}
            lst = []
            for state, action in my_policy.items():
                v =self.get_q_value(state,action)
                lst.append(abs(v-self.get_value(state)))
                thevalues[state] = v
                self.values[state] = v
            if max(lst)<epsilon:
                break
            
            


# 3. Bridge Crossing Analysis
def question_3():
    discount = 0.9
    noise = 0.01
    return discount, noise

# 4. Policies
def question_4a():
    discount = 0.3
    noise = 0.01
    living_reward = 0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4b():
    discount = 0.3
    noise = 0.2
    living_reward = 0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4c():
    discount = 0.8
    noise = 0.1
    living_reward = -0.1
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4d():
    discount = 0.9
    noise = 0.4
    living_reward = -0.1
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4e():
    discount = 1
    noise = 0
    living_reward = 1
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'
