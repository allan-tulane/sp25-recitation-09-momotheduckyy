from collections import defaultdict
from heapq import heappush, heappop 
from math import sqrt

def prim(graph):
    """
    ### TODO:
    Update this method to work when the graph has multiple connected components.
    Rather than returning a single tree, return a list of trees,
    one per component, containing the MST for each component.

    Each tree is a set of (weight, node1, node2) tuples.    
    """
       frontier = []
        tree = set()
        heappush(frontier, (0, start_node, start_node))
        while frontier:
            weight, node, parent = heappop(frontier)
            if node in visited:
                continue
            tree.add((weight, node, parent))
            visited.add(node)
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heappush(frontier, (w, neighbor, node))
        return tree

    visited = set()
    all_trees = []

    for node in graph:
        if node not in visited:
            tree = prim_helper(node, visited)
            # Remove the 0-weight self-loop we added at the start
            tree = {edge for edge in tree if edge[1] != edge[2]}
            all_trees.append(tree)

    return all_trees
    def prim_helper(visited, frontier, tree):
        if len(frontier) == 0:
            return tree
        else:
            weight, node, parent = heappop(frontier)
            if node in visited:
                return prim_helper(visited, frontier, tree)
            else:
                print('visiting', node)
                # record this edge in the tree
                tree.add((weight, node, parent))
                visited.add(node)
                for neighbor, w in graph[node]:
                    heappush(frontier, (w, neighbor, node))    
                    # compare with dijkstra:
                    # heappush(frontier, (distance + weight, neighbor))                

                return prim_helper(visited, frontier, tree)
        
    # pick first node as source arbitrarily
    source = list(graph.keys())[0]
    frontier = []
    heappush(frontier, (0, source, source))
    visited = set()  # store the visited nodes (don't need distance anymore)
    tree = set()
    prim_helper(visited, frontier, tree)
    return tree

def test_prim():    
    graph = {
            's': {('a', 4), ('b', 8)},
            'a': {('s', 4), ('b', 2), ('c', 5)},
            'b': {('s', 8), ('a', 2), ('c', 3)}, 
            'c': {('a', 5), ('b', 3), ('d', 3)},
            'd': {('c', 3)},
            'e': {('f', 10)}, # e and f are in a separate component.
            'f': {('e', 10)}
        }

    trees = prim(graph)
    assert len(trees) == 2
    # since we are not guaranteed to get the same order
    # of edges in the answer, we'll check the size and
    # weight of each tree.
    len1 = len(trees[0])
    len2 = len(trees[1])
    assert min([len1, len2]) == 2
    assert max([len1, len2]) == 5

    sum1 = sum(e[0] for e in trees[0])
    sum2 = sum(e[0] for e in trees[1])
    assert min([sum1, sum2]) == 10
    assert max([sum1, sum2]) == 12
    ###



def mst_from_points(points):
    """
    Return the minimum spanning tree for a list of points, using euclidean distance 
    as the edge weight between each pair of points.
    See test_mst_from_points.

    Params:
      points... a list of tuples (city_name, x-coord, y-coord)

    Returns:
      a list of edges of the form (weight, node1, node2) indicating the minimum spanning
      tree connecting the cities in the input.
    """
    ###TODO
   graph = defaultdict(set)
    for i, (name1, x1, y1) in enumerate(points):
        for j, (name2, x2, y2) in enumerate(points):
            if i != j:
                dist = euclidean_distance((name1, x1, y1), (name2, x2, y2))
                graph[name1].add((name2, dist))

    # Our graph format is {node: set of (neighbor, weight)}, but prim expects (neighbor, weight)
    # We can adapt prim to take this format or just reformat here.

    # Reformat into {node: set of (neighbor, weight)} format (the same as your test_prim uses)
    g = defaultdict(set)
    for (name1, x1, y1) in points:
        for (name2, x2, y2) in points:
            if name1 != name2:
                dist = euclidean_distance((name1, x1, y1), (name2, x2, y2))
                g[name1].add((name2, dist))
    
    # prim returns a list of trees, but we have only 1 component (fully connected graph)
    trees = prim(g)
    # Return the first (and only) tree
    return list(trees[0])

def euclidean_distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def test_euclidean_distance():
    assert round(euclidean_distance(('a', 5, 10), ('b', 7, 12)), 2) == 2.83

def test_mst_from_points():
    points = [('a', 5, 10), #(city_name, x-coord, y-coord)
              ('b', 7, 12),
              ('c', 2, 3),
              ('d', 12, 3),
              ('e', 4, 6),
              ('f', 6, 7)]
    tree = mst_from_points(points)
    # check that the weight of the MST is correct.
    assert round(sum(e[0] for e in tree), 2) == 19.04


