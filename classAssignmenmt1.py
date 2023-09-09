import networkx as nx
import matplotlib.pyplot as plt

class GraphWithPlot:
  def __init__(self):
    self.all_nodes = {}
    self.all_edgeWeight = [[]]

  def addNode(self, new_node, adj_nodes):
    self.all_nodes[new_node] = adj_nodes
    self.all_edgeWeight = [[]]

  def addWeightDouble(self, weight, nodeA, nodeB):
    self.all_edgeWeight = self.all_edgeWeight.append[[weight, nodeA, nodeB]]

  def getAdjNodes(self, target_node):
    return self.all_nodes[target_node]

  def plotSingleNode(self, target_node):
    if not self.checkNodeExistHelper(target_node):
      print("Node is not in current graph!")
      return
    if not self.all_nodes[target_node]:
      print("Node has no adjacent node")
      G = nx.Graph()
      G.add_edges_from(target_node)
    curr_node_edges = []
    for curr_adj_node in self.all_nodes[target_node]:
      curr_node_edges.append([target_node,curr_adj_node])
    G = nx.Graph()
    G.add_edges_from(curr_node_edges)
    nx.draw_networkx(G)
    plt.show()

  def plotGraph(self):
    G = nx.Graph()
    G.add_edges_from(self.getAllEdgesHelper())
    nx.draw_networkx(G)
    plt.show()

  def plotAsDirectedGraph(self):
    G = nx.DiGraph()
    G.add_edges_from(self.getAllEdgesHelper())
    nx.draw_networkx(G)
    plt.show()

  def checkNodeExistHelper(self, target_key)-> bool:
    if target_key in self.all_nodes:
      return True
    return False

  def getAllEdgesHelper(self):
    all_node_edges = []
    for curr_node in self.all_nodes:
      curr_node_edges = []
      for curr_adj_node in self.all_nodes[curr_node]:
        curr_node_edges.append([curr_node,curr_adj_node])
      all_node_edges.extend(curr_node_edges)
    return all_node_edges

G = GraphWithPlot()
G.addNode("A",("B","C","D","E"))
G.addNode("B",("A","C","D","E"))
G.addNode("C",("A","B","D","E"))
G.addNode("D",("A","B","C","E"))
G.addNode("E",("A","B","C","D"))
G.addWeightDouble(3,"A", "B")
G.addWeightDouble(3,"B", "C")
G.addWeightDouble(3,"C", "D")

print("Target node has adjacent nodes:")
print(G.getAdjNodes("C"))
G.plotSingleNode("C")