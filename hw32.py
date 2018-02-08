#Problem 2: Expected Health Utility(Weight 1). Modify the decision tree classes we
#implemented in classsuch that you can also get the expected health utility of
#alternatives in addition to the expected cost. Test your code on the decision
#tree below and print the expected cost and expected health utility of nodes C1 and C3.
#(Note: first download Intro.pyfile from the P4_DecisionTreebranch of the Labs_IntroOOP
#repositoryto your local hard drive so that you can modify
#them and push them to your own repository).



class Node:
    """ base class """
    def __init__(self, name, cost,utility):
        """
        :param name: name of this node
        :param cost: cost of this node
        """
        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        """ abstract method to be overridden in derived classes
        :returns expected cost of this node """
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")
    def get_expected_utility(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class ChanceNode(Node):

    def __init__(self, name, cost, future_nodes, probs, utility):
        """
        :param future_nodes: future nodes connected to this node
        :param probs: probability of the future nodes
        """
        Node.__init__(self, name, cost, utility)
        self.futureNodes = future_nodes
        self.probs = probs

    def get_expected_cost(self):
        """
        :return: expected cost of this chance node
        """
        exp_cost = self.cost  # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_cost += self.probs[i]*node.get_expected_cost()
            i += 1
        return exp_cost
    def get_expected_utility(self):
        """
        :return: expected utility of this chance node
        """
        exp_utility = self.utility # expected cost initialized with the cost of visiting the current node
        i = 0
        for node in self.futureNodes:
            exp_utility += self.probs[i]*node.get_expected_utility()
            i += 1
        return exp_utility


class TerminalNode(Node):

    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        """
        :return: cost of this chance node
        """
        return self.cost
    def get_expected_utility(self):
        """
        :return: cost of this chance node
        """
        return self.utility


class DecisionNode(Node):

    def __init__(self, name, cost, future_nodes,utility):
        Node.__init__(self, name, cost,utility)
        self.futureNode = future_nodes

    def get_expected_cost(self):
        """ returns the expected costs of future nodes"""
        outcome = dict()       # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            outcome[node.name] = node.get_expected_cost()

        return outcome
    def get_expected_utility(self):
        """ returns the expected costs of future nodes"""
        utility_outcomes = dict() # dictionary to store the expected cost of future nodes along with their names as keys
        for node in self.futureNode:
            utility_outcomes[node.name] = node.get_expected_utility()

        return utility_outcomes

#######################
# See figure DT3.png (from the project menu) for the structure of this decision tree
########################

# create the terminal nodes
T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)

# create C2 #make place holder for utility
C2 = ChanceNode('C2', 15, [T1, T2], [0.1, 0.9], 0)
# create C1
C1 = ChanceNode('C1', 0, [C2, T3], [0.4, 0.6], 0)
# create C3
C3 = ChanceNode('C3', 2, [T4, T5], [0.2, 0.8], 0)

# create D1
D1 = DecisionNode('D1', 0, [C1, C3], 0)

# print the expect cost of C1
print(D1.get_expected_cost())
print(D1.get_expected_utility())
