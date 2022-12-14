print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

import networkx as nx
from typing import NamedTuple

class City(NamedTuple):
    name: str
    country: str
    year: int
    latitude: float
    longitude: float


@classmethod
def from_dict(cls, attrs):
    return cls(
        name=attrs["xlabel"],
        country=attrs["country"],
        year=int(attrs["year"]) or None,
        latitude=float(attrs["latitude"]),
        longitude=float(attrs["longitude"]),
    )


def load_graph(filename, node_factory):
    graph = nx.nx_agraph.read_dot(filename)
    nodes = {
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    return nodes, nx.Graph(
        (nodes[name1], nodes[name2], weights)
        for name1, name2, weights in graph.edges(data=True)
    )