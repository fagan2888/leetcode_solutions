## https://leetcode.com/problems/employee-importance

## only twist here is that we have employees by ID, 
## rather than by their index in the employees data
## structure.  so we build a dictionary to do that 
## conversion once, so we don't have to do it again.

## then we just use a stack to keep track of subordiantes
## to touch, and then we're done.  

## comes in at 75th percentile for runtime and ~41st 
## for memory.


"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        ids_to_idx = {emp.id: idx for idx, emp in enumerate(employees)}
                
        value = 0
        todo = [employees[ids_to_idx[id]]]
        while len(todo):
            emp = todo.pop()
            value += emp.importance
            for sub in emp.subordinates:
                todo.append(employees[ids_to_idx[sub]])
        return value
        