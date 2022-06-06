# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:19:43 2022

@author: anmol
"""

import networkx as nx
import pylab as plt

# Create blank graph
D=nx.DiGraph()

# Feed page link to graph
#D.add_weighted_edges_from([('A','B',1),('A','C',1),('C','A',1),('B','C',1)])

D.add_edges_from([('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'A'),
				('D', 'C'), ('E', 'D'), ('E', 'B'), ('E', 'F'),
				('E', 'C'), ('F', 'C'), ('F', 'H'), ('G', 'A'),
				('G', 'C'), ('H', 'A')])
# Print page rank for each pages
print (nx.pagerank(D))

# Plot graph
nx.draw(D, with_labels=True)
plt.show()