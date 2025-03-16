# SAS_A2
A repository for grid-based pathfinding algorithms.

## Assignment Overview
This assignment involves implementing a grid-based pathfinding algorithm and submitting it to the **GPPC server**.

### **Requirements**
- Implement a **best-first search** algorithm.
- Ensure the solution correctly solves all problems in the selected track.

### **Approach Options**
- **Abstraction & Refinement** (suitable for the dynamic track)
- **Online Search Heuristics** (e.g., differential or fastmap)
- **Constraints** (reach, bounding boxes)
- **Jump Point Search (JPS)**
- **Precomputed Shortest Paths** (e.g., all-pairs shortest-path data)

### **Evaluation Criteria**
- **50%** - Correct implementation solving all competition problems.
- **50%** - Report detailing approach and results.
- **Bonus (10%)**:
  - Entry on the **Pareto-optimal frontier**.
  - Submission to the **dynamic track**.

### **Suggested Strategies**
- **Dynamic Track**: Optimize abstraction/refinement and caching.
- **Classic Track**: Use precomputed paths in an abstract graph.
- **General Optimization**: Enhance JPS with heuristics and reach constraints.

For details, visit: [GPPC Website](https://gppc.search-conference.org)
