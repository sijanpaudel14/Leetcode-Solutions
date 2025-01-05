""" 
Algorithm:
Build the prerequisites map:
    Create a dictionary preMap where each key represents a course, and the value is a list of prerequisites for that course. For each prerequisite pair [course, pre], add pre to preMap[course].
    
State Representation:
    Use an array state of size numCourses to keep track of the state of each course. The states are:
    UNVISITED (0): The course has not been explored.
    VISITING (1): The course is currently being explored in the DFS stack.
    VISITED (2): The course has been fully explored and doesn't lead to a cycle.
    
DFS Function:
    For each course, perform a DFS to check for cycles. If a cycle is detected, return False.
    Mark the course as VISITING when entering it.
    Recursively visit all prerequisites of the course. If a prerequisite leads to a cycle, return False.
    After exploring all prerequisites, mark the course as VISITED.
    
Check for all courses:
    Iterate through all courses, and if a course has not been visited, perform DFS on it.
    If any DFS returns False, return False indicating it's impossible to finish all courses due to a cycle.
    If all DFS calls are successful, return True.
"""

def canFinish(numCourses, prerequisites):
    # Step 1: Build the prerequisites map (adjacency list)
    preMap = {}
    for course, pre in prerequisites:
        if course not in preMap:
            preMap[course] = []  # Initialize empty list if not present
        preMap[course].append(pre)  # Add the prerequisite to the list of the course

    # Step 2: Define the states for each course
    UNVISITED, VISITING, VISITED = 0, 1, 2
    state = [UNVISITED] * numCourses  # Initially all courses are unvisited
    
    # Step 3: Define the DFS function to detect cycles
    def dfs(course):
        # If the course is in the VISITING state, a cycle is detected
        if state[course] == VISITING:
            return False
        
        # If the course has already been fully explored, no need to explore again
        if state[course] == VISITED:
            return True
        
        # Mark the course as VISITING (in the current DFS stack)
        state[course] = VISITING
        
        # Explore all prerequisites of the current course
        if course in preMap:  # Check if the course has prerequisites
            for pre in preMap[course]:
                if not dfs(pre):  # Recursively visit the prerequisite course
                    return False  # Cycle detected in the prerequisites
        
        # After exploring all prerequisites, mark the course as VISITED (explored fully)
        state[course] = VISITED
        return True

    # Step 4: Perform DFS for each course
    for course in range(numCourses):
        if state[course] == UNVISITED:  # Only start DFS if the course has not been visited
            if not dfs(course):
                return False  # If any DFS detects a cycle, return False
    
    # Step 5: If no cycle is detected, all courses can be finished
    return True

# Example usage
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(canFinish(numCourses, prerequisites))  # Should return False (due to cycle)
