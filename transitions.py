import numpy as np

def valid_transition(state1,state2):
    if list(state1) == list(state2):
        return 0
    # exclude invalid transitions due to the inflow parabola shape function
    if state1[0] == 0 and state1[1] == 0 and (state2[0] != 0 or state2[1] != 0):
        return 0
    if state1[0] == 0 and state1[1] == 1 and (state2[0] != 1 or state2[1] != 1):
        return 0
    if state1[0] == 1 and state1[1] == 0 and (state2[0] != 1 or state2[1] != -1):
        return 0
    if state1[0] == 1 and state1[1] == 1 and (state2[0] != 1 or state2[1] != 1) and  (state2[0] != 1 or state2[1] != 0):
        return 0
    if state1[0] == 1 and state1[1] == -1 and (state2[0] != 1 or state2[1] != -1) and  (state2[0] != 0 or state2[1] != 0):
        return 0   
    
   
    for i in range(int(len(state1)/2)):
        # exclude transitions which invalid derivative sign change: + -> - or - -> +
        if abs(state1[2*i+1] - state2[2*i+1]) == 2:
            return 0
        # exclude transitions which invalid value change: 0 -> Max or Max -> 0
        if abs(state1[2*i] - state2[2*i]) == 2:
            return 0
        # exclude transitions which invalid value change according to the derivative
        if state1[i*2+1] == 1 and state2[2*i] < state1[2*i]:
            return 0
        if state1[i*2+1] == -1 and state2[2*i] > state1[2*i]:
            return 0
        if state1[i*2+1] == 0 and state2[2*i] != state1[2*i]:
            return 0
   
        
    # exclude transitions that change the derivative without changing the value when the inflow is the same 
    # or the magnitude or the derivative of the inflow is 0 
    if state1[0] == state2[0] and state1[1] == state2[1] or state1[0] == 0 or state1[1] == 0:
        for i in range(1,int(len(state1)/2)):
            if state1[2*i] == state2[2*i] and state1[2*i+1] != 0 and state1[2*i+1] != state2[2*i+1] :
                return 0           
        
         
    return 1

def transition_states(state,validS):
    result = []
    for i in range(np.shape(validS)[0]):
        if valid_transition(state,validS[i,:]) == 1:
            result.append(validS[i,:])
    
    return np.array(result)


    
            
            

            
            
            
            
            
            
            
            
    