from pulp import *
import numpy as np
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"

    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def uSTP(V,E,T,C):
    """Given a graph G(V,E) with terminal set T and the set of edge weights C, return a list of edges used in the Steiner tree"""

    n = len(V)
    m = len(E)
    x_v = {}
    stp = LpProblem("STP", LpMinimize)

    # for each x_i, initiaize a variable
    for i in range(0,m):
        x_v["x{0}".format(i)] = LpVariable("x"+i,0,1) 

    # set up the ILP
    optimize = np.matmul(np.array(C).transpose(), np.asarray(x_v))
    stp += optimize

    # get V \ T
    V_T = []
    for item in V:
        if item not in T: V_T.append(item)

    # x(S(w)) >= 1
    W = list(powerset(V_T)) # TODO: W is not a proper subset
    W_l = {}
    for i in W:
        W_l["w{}".format()] = LpVariable("w"+i,1)




    # solve the STP and return all variables as a list
    stp.solve()
    return x_v