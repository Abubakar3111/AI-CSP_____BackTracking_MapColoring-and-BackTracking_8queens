print("AbubakarAsif FA20-BCE-013")
#AbubakarAsif FA20-BCE-013
#abubakarasif3111@gmail.com
#https://github.com/Abubakar3111
#https://www.linkedin.com/in/abubakar-asif-b3b94021a/
class CSP():
def __init__(self, variables, domains,constraints):
self.variables = variables  # variables to be constrained
self.domains = domains  # domain of each variable
self.constraints = constraints


            # if variable not in self.domains:
            #     raise LookupError(
            #         "Every variable should have a domain assigned to it.")


defadd_constraint(self, constraint):
        #pass
        #for each variable involved in the contstraint
        #append the contraint to the variable's contraint list in the dictionary
        for v in self.constraints:
self.constraints[v].append(constraint)


defconsistent(self, variable, assignment):
        pass

        #Check if the value assignment is consistent by checking all constraints
        #for the given variable against it
        #for each contraint of the variable in the contraints dictionary      
        #if constraint not statisfied return false

        for c in self.constraints[variable]:
            if not c.satisfied(assignment):
                return False
        return True
        #otherwise return true


defbacktracking_search(self, assignment={}):
        #pass

        # if assignment is complete if every variable is assigned (our base case) then return it
        if len(assignment) == len(self.variables):
            return assignment     

        # get all variables in the CSP but not in the assignment
        unassigned = [v  for v in self.variables if v not in assignment]      
        first = unassigned[0]

        for value in self.domains[first]:
local_assignment=assignment.copy()
local_assignment[first]=value

            if self.consistent(first,local_assignment):
                result=self.backtracking_search(local_assignment)
                if result != None:
                    return result     
        return None

class queen_constraint:



def satisfied(self,assignment):
        for i in assignment:
            for j in assignment:
                if i != j or j>i:
                    if assignment[i]==assignment[j]:
                        return False
                    if abs(i - j)== abs(assignment[i] - assignment[j]):
                        return False
        return True



defcharconv(char):
      number=ord(char)-96
      return number



variables=[1,2,3,4,5,6,7,8]
domains={}
for v in variables:
    domains[v]=[1,2,3,4,5,6,7,8]


constraints={}
for v in variables:
    constraints[v]=[]

csp=CSP(variables,domains,constraints)
csp.add_constraint(queen_constraint())
#print(csp.constraints)
solution=csp.backtracking_search()
if solution != None:
    print(solution) 
else: print("No Solution found")
print("AbubakarAsif FA20-BCE-013")
