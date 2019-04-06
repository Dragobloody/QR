import numpy as np
import itertools


def generate_all_possible_states(Q,val_domain,der_domain):
    lists = [val_domain['I'],der_domain['I'],
             val_domain['V'],der_domain['V'],
             val_domain['H'],der_domain['H'],
             val_domain['P'],der_domain['P'],
             val_domain['O'],der_domain['O']]
    
    S = np.array(list(itertools.product(*lists)))
    return S

def valid_state(state,I,P,Max_eq,Zero_eq):  
    # remove states that contradict the the parabola shaped inflow function
    if state[0] == 0 and state[1] == -1:
        return 0
    
    # remove states that contradict max or zero dependencies
    for i in range(np.shape(Max_eq)[0]):
        for j in range(np.shape(Max_eq)[1]):
            if Max_eq[i,j] == 1 and state[2*i] == 2 and state[2*j] != 2:
                return 0
            if Zero_eq[i,j] == 1 and state[2*i] == 0 and state[2*j] != 0:
                return 0
    
    # remove states that contradict proportional or influence dependencies
    for j in range(np.shape(P)[1]):
        auxP = set()
        auxI = set()
        aux = 0
        for i in range(np.shape(P)[0]):
            if P[i,j] !=0 or I[i,j] !=0:
                aux = 1
            if P[i,j] != 0 and state[2*i+1] != 0:
                auxP.add(np.sign(P[i,j]*state[2*i+1]))
            if I[i,j] != 0 and state[2*i] != 0:
                auxI.add(np.sign(I[i,j]*state[2*i]))
                
        if aux!=0 and len(auxP) == 0 and len(auxI) == 0 and state[2*j+1] !=0:
            return 0
        if len(auxP) == 1 and state[2*j+1] != auxP.pop():
            return 0
        if len(auxI) == 1 and state[2*j+1] != auxI.pop():
            return 0   
        
    return 1


def remove_invalid_states(S,I,P,Max_eq,Zero_eq):
    newS = []
    for i in range(np.shape(S)[0]):
        if valid_state(S[i,:],I,P,Max_eq,Zero_eq) == 1:
            newS.append(S[i,:])
    return np.array(newS)
        
        
        
        
        
        