print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

import networkx as nx
graph = nx.nx_agraph.read_dot("roadmap.dot")
print(graph.nodes["london"])