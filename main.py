import numpy as np
import states as st
import transitions as tr


# quantities
Q = ['I','V','H','P','O']
# quatity spaces
val_domain = {'I':[0,1],'V':[0,1,2],'H':[0,1,2],'P':[0,1,2],'O':[0,1,2]}
# derivatives
der_domain = {'I':[-1,0,1],'V':[-1,0,1],'H':[-1,0,1],'P':[-1,0,1],'O':[-1,0,1]}
# influence dependencies: 1 = I+, -1 = I-, 0 = nothing
I = np.array([[0,1,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0],
              [0,-1,0,0,0]])
# proportionality dependencies: 1 = P+, -1 = P-, 0 = nothing
P = np.array([[0,0,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,0],
              [0,0,0,0,1],
              [0,0,0,0,0]])
# max dependencies: 1 = equality, 0 = nothing
Max_eq = np.array([[0,0,0,0,0],
              [0,0,1,0,0],
              [0,1,0,1,0],
              [0,0,1,0,1],
              [0,0,0,1,0]])
# zero dependencies: 1 = equality, 0 = nothing
Zero_eq = np.array([[0,0,0,0,0],
              [0,0,1,0,0],
              [0,1,0,1,0],
              [0,0,1,0,1],
              [0,0,0,1,0]])



S = st.generate_all_possible_states(Q,val_domain,der_domain)
validS = st.remove_invalid_states(S,I,P,Max_eq,Zero_eq)








