from collections import defaultdict, deque
from itertools import chain, combinations, islice

from numpy.typing import ArrayLike

from ..classes.graph import Graph
from ..utils import not_implemented_for

__all__ = [
    "find_cliques",
    "find_cliques_recursive",
    "make_max_clique_graph",
    "make_clique_bipartite",
    "graph_clique_number",
    "graph_number_of_cliques",
    "node_clique_number",
    "number_of_cliques",
    "cliques_containing_node",
    "enumerate_all_cliques",
    "max_weight_clique",
]

def enumerate_all_cliques(G: Graph): ...
def find_cliques(G: Graph, nodes=None): ...

# TODO Should this also be not implemented for directed graphs?
def find_cliques_recursive(G: Graph, nodes=None): ...
def make_max_clique_graph(G: Graph, create_using=None): ...
def make_clique_bipartite(G: Graph, fpos: bool | None = None, create_using=None, name=None): ...
def graph_clique_number(G: Graph, cliques: ArrayLike | None = None) -> int: ...
def graph_number_of_cliques(G: Graph, cliques: ArrayLike | None = None) -> int: ...
def node_clique_number(G: Graph, nodes=None, cliques=None, separate_nodes=False) -> int | dict: ...
def number_of_cliques(G: Graph, nodes=None, cliques=None): ...
def cliques_containing_node(G: Graph, nodes=None, cliques=None): ...

class MaxWeightClique:
    def __init__(self, G: Graph, weight): ...
    def update_incumbent_if_improved(self, C, C_weight): ...
    def greedily_find_independent_set(self, P): ...
    def find_branching_nodes(self, P, target): ...
    def expand(self, C, C_weight, P): ...
    def find_max_weight_clique(self): ...

def max_weight_clique(G: Graph, weight="weight") -> tuple[ArrayLike, int]: ...