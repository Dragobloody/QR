import numpy as np
import states as st
import transitions as tr
import graph as gr
import pydotplus


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


# generate all possible states
S = st.generate_all_possible_states(Q,val_domain,der_domain)
# remove the states that cannot be possible
validS = st.remove_invalid_states(S,I,P,Max_eq,Zero_eq)

# from an initial state (here 4) generate a file in DOT in order to make it graphical
# the output is the states that are possible from transitions with different label
mapping = gr.states_to_graph(validS, 4)

# make the state graph from the DOT file
state_graph = pydotplus.graph_from_dot_file('Graph.dot')
# write the graph as avg format
state_graph.write_svg('State_Graph.svg')

# printing the states of the graph
print("\t  Im  Id  Vm  Vd  Hm  Hd  Pm  Pd  Om  Od")
for key in mapping.keys():
       my_str = ''
       for i in range(10):
              if validS[key][i] >= 0:
                     my_str += ' ' + str(validS[key][i]) + '  '
              else:
                     my_str += str(validS[key][i]) + '  '
       print("State %2d: %s"%(mapping[key], my_str))
