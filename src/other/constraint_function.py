import numpy as np

# Three-bar truss design problem

# Constants
L = 100 # cm
P = 2 # KN / cm^2
SIGMA = 2 # KN / cm^2

def objective_function(solution):
    def g1(x):
        return (np.sqrt(2*x[0]) + x[1]/(np.sqrt(2*(x[0]**2)))*P + 2*x[0]*x[1]) - SIGMA
    def g2(x):
        return (x[1]/(np.sqrt(2*(x[0]**2)) + 2*x[0]*x[1]))*P - SIGMA   
    def g3(x):
        return (1/(np.sqrt(2*x[1]) + x[0]))*P - SIGMA

    def violate(value):
        return 0 if value <= 0 else value

    fx = (2 * np.sqrt(2*solution[0]) + np.sqrt(solution[1]))*L

    ## Increase the punishment to boost the algorithm 
    fx += violate(g1(solution)) + violate(g2(solution)) + violate(g3(solution))
            
    return fx