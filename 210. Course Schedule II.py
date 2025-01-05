"""
Algorithm:
Build the prerequisites map:
    Create a dictionary preMap where each key represents a course, and the value is a list of courses that are prerequisites for that course.
    
State Representation:
    Use an array state to track the state of each course: UNVISITED (0), VISITING (1), and VISITED (2).
    
DFS (Depth-First Search) for cycle detection and ordering:
    Perform DFS on each course.
    If the course is already in the current DFS stack (VISITING), a cycle is detected.
    If the course has already been fully explored (VISITED), we don't need to explore it again.
    If a course is valid, push it to the result list (in reverse order).
    
Return the course order:
    If a cycle is detected, return an empty list.
    If all DFS calls are successful, return the result list with courses in reverse order (because the course needs to be finished after its prerequisites).
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Build the prerequisites map (adjacency list)
        preMap = {}  # A dictionary to store the list of prerequisites for each course
        for course, pre in prerequisites:
            if course not in preMap:
                preMap[course] = []  # Initialize empty list if not already present
            preMap[course].append(pre)  # Add the prerequisite to the course's list
        
        # Step 2: Define the states for each course
        UNVISITED, VISITING, VISITED = 0, 1, 2
        state = [UNVISITED] * numCourses  # Initially, all courses are unvisited
        
        # List to store the course order (the result)
        result = []
        
        # Step 3: Define the DFS function to detect cycles and build the course order
        def dfs(course):
            # If the course is currently being visited (in the DFS stack), we've found a cycle
            if state[course] == VISITING:
                return False
            
            # If the course has already been fully explored, no need to explore again
            if state[course] == VISITED:
                return True
            
            # Mark the course as VISITING (currently in the DFS stack)
            state[course] = VISITING
            
            # Step 4: Explore all prerequisites of the current course
            if course in preMap:  # Only visit the prerequisites if the course has any
                for pre in preMap[course]:
                    if not dfs(pre):  # If any prerequisite causes a cycle, return False
                        return False
            
            # Mark the course as VISITED (fully explored)
            state[course] = VISITED
            
            # Step 5: Add the course to the result list (order will be reversed later)
            result.append(course)
            return True
        
        # Step 6: Perform DFS for each course
        for course in range(numCourses):
            if state[course] == UNVISITED:  # Start DFS if the course is unvisited
                if not dfs(course):  # If DFS detects a cycle, return an empty list
                    return []
        
        # Step 7: Return the course order in reverse (since we've added courses after finishing them)
        return result
