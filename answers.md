# CMPS 2200 Recitation 09

## Answers

**Name:** Mohini Yadav
**Name:**_________________________


Place all written answers from `recitation-09.md` here for easier grading.



- **2) In the worst case, the graph has k connected components. The algorithm runs Prim's algorithm seperately on each connected component. For each component with V vercies and E edges, Prims algorithm performs O(E log V) work using a binary heap. In the overall worst case, the toral number of edges in the full graph, the work is O(E log V). 

- **4) Work of the mst_from_points. The algorithm builds a fully connected, undirected graph in which each pair of n points is connected by an edge which uses Euclidean distance. This requires O(N^2) + O(n^2 log n) = O(n^2 log n) total work.
