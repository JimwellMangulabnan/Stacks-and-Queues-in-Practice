print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

from graph4 import City, load_graph

nodes, graph = load_graph("roadmap.dot", City.from_dict)

for neighbor in graph.neighbors(nodes["london"]):
    print("/t/t", neighbor.name)
